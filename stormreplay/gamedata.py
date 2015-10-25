#!/usr/bin/python
# -*- coding: utf-8 -*-

heroes = [
          {'name': 'Abathur', 'name_cyr': 'Абатур', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': "Anub'arak", 'name_cyr': "Ануб'арак", 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Arthas', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Azmodan', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Valla', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Gazlowe', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Chen', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Diablo', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'E.T.C.', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Falstad', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Brightwing', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Illidan', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Jaina', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': 'Johanna', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': "Kael'thas", 'name_cyr': "", 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
         ]
