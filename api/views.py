from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

import requests
import os
import json
import datetime

from stormreplay import StormReplayAnalyzer, heroes, battlegrounds

from tasks import LocallyStoredReplayParsingTask
from tasks import S3StoredReplayParsingTask
from tempfile import NamedTemporaryFile

import base64
import hmac, hashlib

import random



def buildS3UploadFormPolicy(successActionRedirectUrl):
 
    expiration = (datetime.date.today()+datetime.timedelta(days=2)).isoformat() + 'T12:00:00.000Z'
    bucket = os.environ.get('AWS_BUCKET_NAME')
    key = ("%04x" % random.randint(0,1<<16-1)) + datetime.datetime.now().strftime('-%y%m%d%H%M%S/file.StormReplay')
    maxReplayFileSizeBytes = os.getenv('MAX_REPLAY_FILE_SIZE', 1048576)

    policyDocument = ('{{"expiration":"{0}",'
                      ' "conditions": ['
                      '   {{"bucket": "{1}"}},'
                      '   {{"acl": "private"}},'
                      '   ["eq", "$key", "{2}"],'
                      '   {{"success_action_redirect": "{3}"}},'
                      '   ["eq", "$Content-Type", "application/octet-stream"],'
                      '   ["content-length-range", 0, {4}]'
                      ' ]'
                      '}}'
                     ).format(expiration, bucket, key, successActionRedirectUrl, maxReplayFileSizeBytes)

    policy = base64.b64encode(policyDocument)
    signature = base64.b64encode(hmac.new(os.environ.get('AWS_SECRET_ACCESS_KEY'), policy, hashlib.sha1).digest())

    return {
        'bucket': bucket,
        'key': key,
        'AWSAccessKeyId': os.environ.get('AWS_ACCESS_KEY_ID'),
        'acl': 'private',
        'success_action_redirect': successActionRedirectUrl,
        'policy': policy,
        'signature': signature,
        'Content-Type': 'application/octet-stream',
    }

def uploadToS3Page(request):
    successUrl = request.build_absolute_uri('/api/process')
    s3 = buildS3UploadFormPolicy(successUrl)
    s3['Content_Type'] = s3['Content-Type']
    return render(request, 'api/file-upload-s3.html', {'s3': s3})

def uploadToS3Form(request):
    successUrl = request.build_absolute_uri('/api/process')
    return HttpResponse(json.dumps(buildS3UploadFormPolicy(successUrl)), content_type="application/json")

def processReplayThatWasUploadedToS3(request):
    key = request.GET.get('key')
    bucket = request.GET.get('bucket')
    # todo: do we need to validate bucket here?
    asyncResult = S3StoredReplayParsingTask.delay(key)
    content = json.dumps({
        'result_url': request.build_absolute_uri('result?id='+asyncResult.id)
    })
    return HttpResponse(content, content_type="application/json")

def debug(request):
    allFieldNames = StormReplayAnalyzer.getAllFieldMappingNames()
    if request.method == "POST":
        if not request.FILES.has_key('file'):
            content = json.dumps({'error':'Missing "file" parameter with uploaded replay file data'})
            Result = {'status': 'No file chosen', 'result_url': request.META.get('HTTP_REFERER'), 'url_text': 'Back',}
            Result_html = 'back.html'
        else:
            replayFile = request.FILES.get('file')
            savedReplayFile = NamedTemporaryFile(delete=False)
            for chunk in replayFile.chunks():
                savedReplayFile.write(chunk)
            savedReplayFileName = savedReplayFile.name
            savedReplayFile.close()
            fieldNamesToParse = []
            for name in allFieldNames:
#                if name == 'RawReplayDetails':
#                    fieldNamesToParse.append(name)
                if bool(request.POST.get(name, False)):
                    fieldNamesToParse.append(name)
            asyncResult = LocallyStoredReplayParsingTask.delay(savedReplayFileName, fieldNamesToParse)
#            content = json.dumps({
#                'result_url': (request.META.get('HTTP_REFERER') + '/result?id=' + asyncResult.id),
#            })
            Result = {'status': 'Successfully uploaded', 'result_url': request.META.get('HTTP_REFERER') + '/result?id=' + asyncResult.id, 'url_text': 'Proceed to result',}
            Result_html = 'proceed.html'
#        ^_^
        return render_to_response('response/' + Result_html, Result)
        #return HttpResponse(content, content_type="application/json")

    return render(request, 'api/file-upload.html', {'all_field_names': allFieldNames})

def getProcessedReplayResult(request):
    celeryTaskId = request.GET.get('id', '')
    result = LocallyStoredReplayParsingTask.AsyncResult(celeryTaskId)
    if (result.status == 'FAILURE'):
        return HttpResponse(json.dumps({'status':'FAILURE','exception':str(result.result)}), content_type="application/json")
    if (result.status == 'SUCCESS'):
        mapname = result.get()['raw']['details']['m_title']['utf8']
        players = result.get()['raw']['details']['m_playerList']
        herolist = []
        for player in players:
           for hero in heroes:
                if (player['m_hero']['utf8'] == hero['name']) or (player['m_hero']['utf8'] == hero['name_cyr']):
                    herolist.append({'id': player['m_workingSetSlotId'], 'name': hero['name'], 'replayname': player['m_hero']['utf8'], 'player': player['m_name']['utf8']})
        if players[0]['m_result'] == 1:
            team1 = 'Victory'
            team2 = 'Defeat'
        else:
            team1 = 'Defeat'
            team2 = 'Victory'            
#        herolist = [{'name': hero['name'], 'replayname': player['m_hero']['utf8'], 'player': player['m_name']['utf8']} for hero in heroes for player in players if (player['m_hero']['utf8'] == hero['name']) or (player['m_hero']['utf8'] == hero['name_cyr'])]
        bglist = [bg['name'] for bg in battlegrounds]
        #indentValue = int(request.GET.get('indent')) if request.GET.has_key('indent') else None
        return render_to_response('response/result.html' ,{'mapname': mapname, 'herolist': herolist, 'players': players, 'team1': team1, 'team2': team2, })
        #return HttpResponse(json.dumps({'status':'SUCCESS','data':result.get()}, indent=int(request.GET.get('indent')) if request.GET.has_key('indent') else None), content_type="application/json")
    return HttpResponse(json.dumps({'status':'PENDING'}), content_type="application/json")

