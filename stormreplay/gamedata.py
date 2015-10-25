#!/usr/bin/python
# -*- coding: utf-8 -*-

heroes = [
          {'name': 'Abathur', 'name_cyr': 'Абатур', 'title': 'Evolution Master', 'title_cyr': 'Мастер эволюции', 'universe': 'StarCraft', 'role': 'Specialist', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': "Anub'arak", 'name_cyr': "Ануб’арак", 'title': 'Traitor King', 'title_cyr': 'Король-предатель', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Arthas', 'name_cyr': 'Артас', 'title': 'The Lich King', 'title_cyr': 'Король-лич', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Azmodan', 'name_cyr': 'Азмодан', 'title': 'Lord of Sin', 'title_cyr': 'Владыка Греха', 'universe': 'Diablo', 'role': 'Specialist', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Valla', 'name_cyr': 'Валла', 'title': 'Demon Hunter', 'title_cyr': 'Охотница на демонов', 'universe': 'Diablo', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Gazlowe', 'name_cyr': 'Газлоу', 'title': 'Boss of Ratchet', 'title_cyr': 'Шеф Кабестана', 'universe': 'WarCraft', 'role': 'Specialist', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Chen', 'name_cyr': 'Чэнь', 'title': 'Legendary Brewmaster', 'title_cyr': 'Легендарный хмелевар', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Diablo', 'name_cyr': 'Диабло', 'title': 'Lord of Terror', 'title_cyr': 'Владыка Ужаса', 'universe': 'Diablo', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'E.T.C.', 'name_cyr': 'E.T.C.', 'title': 'Rock God', 'title_cyr': 'Икона рока', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Falstad', 'name_cyr': 'Фалстад', 'title': 'Wildhammer Thane', 'title_cyr': 'Тан клана Громового Молота', 'universe': 'WarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Brightwing', 'name_cyr': 'Светик', 'title': 'Faerie Dragon', 'title_cyr': 'Чудесный дракончик', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Illidan', 'name_cyr': 'Иллидан', 'title': 'The Betrayer', 'title_cyr': 'Предатель', 'universe': 'WarCraft', 'role': 'Assassin', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Jaina', 'name_cyr': 'Джайна', 'title': 'Archmage', 'title_cyr': 'Верховный маг', 'universe': 'WarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Johanna', 'name_cyr': 'Джоанна', 'title': 'Crusader of Zakarum', 'title_cyr': 'Крестоносец Закарума', 'universe': 'Diablo', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': "Kael'thas", 'name_cyr': "Кель'тас", 'title': 'The Sun King', 'title_cyr': 'Солнечный король', 'universe': 'WarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Kerrigan', 'name_cyr': 'Керриган', 'title': 'Queen of Blades', 'title_cyr': 'Королева Клинков', 'universe': 'StarCraft', 'role': 'Assassin', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Stitches', 'name_cyr': 'Стежок', 'title': 'Terror of Darkshire', 'title_cyr': 'Ужас Темнолесья', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Li Li', 'name_cyr': 'Ли Ли', 'title': 'World Wanderer', 'title_cyr': 'Странствующая по свету', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'The Lost Vikings', 'name_cyr': 'Потерявшиеся викинги', 'title': 'Triple Trouble', 'title_cyr': 'Три в одном', 'universe': 'Blizzard', 'role': 'Specialist', 'combat_type': 'Melee/Ranged', 'difficulty': ''}
          {'name': 'Malfurion', 'name_cyr': 'Малфурион', 'title': 'Archdruid', 'title_cyr': 'Верховный друид', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Muradin', 'name_cyr': 'Мурадин', 'title': 'Mountain King', 'title_cyr': 'Горный король', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Murky', 'name_cyr': 'Мурчаль', 'title': 'Baby Murloc', 'title_cyr': 'Маленький мурлок', 'universe': 'WarCraft', 'role': 'Specialist', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Nazeebo', 'name_cyr': 'Назибо', 'title': 'Heretic Witch Doctor', 'title_cyr': 'Колдун-ренегат', 'universe': 'Diablo', 'role': 'Specialist', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Nova', 'name_cyr': 'Нова', 'title': 'Dominion Ghost', 'title_cyr': 'Призрак Доминиона', 'universe': 'StarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Raynor', 'name_cyr': 'Рейнор', 'title': 'Renegade Commander', 'title_cyr': 'Лидер мятежников', 'universe': 'StarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Rehgar', 'name_cyr': 'Регар', 'title': 'Shaman of the Earthen Ring', 'title_cyr': 'Шаман Служителей Земли', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Sgt. Hammer', 'name_cyr': 'Сержант Кувалда', 'title': 'Siege Tank Operator', 'title_cyr': 'Оператор осадного танка', 'universe': 'StarCraft', 'role': 'Specialist', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Sonya', 'name_cyr': 'Соня', 'title': 'Wandering Barbarian', 'title_cyr': 'Странствующий варвар', 'universe': 'Diablo', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Sylvanas', 'name_cyr': 'Сильвана', 'title': 'The Banshee Queen', 'title_cyr': 'Королева банши', 'universe': 'WarCraft', 'role': 'Specialist', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Tassadar', 'name_cyr': 'Тассадар', 'title': 'Savior of the Templar', 'title_cyr': 'Спаситель тамплиеров', 'universe': 'StarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Thrall', 'name_cyr': 'Тралл', 'title': 'Warchief of the Horde', 'title_cyr': 'Вождь Орды', 'universe': 'WarCraft', 'role': 'Assassin', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Tychus', 'name_cyr': 'Тайкус', 'title': 'Notorious Outlaw', 'title_cyr': 'Известный преступник', 'universe': 'StarCraft', 'role': 'Assassin', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Tyrael', 'name_cyr': 'Тираэль', 'title': 'Archangel of Justice', 'title_cyr': 'Архангел Справедливости', 'universe': 'Diablo', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Tyrande', 'name_cyr': 'Тиранда', 'title': 'High Priestess of Elune', 'title_cyr': 'Верховная жрица Элуны', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Uther', 'name_cyr': 'Утер', 'title': 'The Lightbringer', 'title_cyr': 'Светоносный', 'universe': 'WarCraft', 'role': 'Support', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Zagara', 'name_cyr': 'Загара', 'title': 'Broodmother of the Swarm', 'title_cyr': 'Мать стаи', 'universe': 'StarCraft', 'role': 'Specialist', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Zeratul', 'name_cyr': 'Зератул', 'title': 'Dark Prelate', 'title_cyr': 'Темный прелат', 'universe': 'StarCraft', 'role': 'Assassin', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'The Butcher', 'name_cyr': 'Мясник', 'title': 'Flesh Carver', 'title_cyr': 'Терзатель плоти', 'universe': 'Diablo', 'role': 'Assassin', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Leoric', 'name_cyr': 'Леорик', 'title': 'The Skeleton King', 'title_cyr': 'Король-скелет', 'universe': 'Diablo', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Kharazim', 'name_cyr': 'Каразим', 'title': 'Veradani Monk', 'title_cyr': 'Монах верадани', 'universe': 'Diablo', 'role': 'Support', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': 'Rexxar', 'name_cyr': 'Рексар', 'title': 'Champion of the Horde', 'title_cyr': 'Герой Орды', 'universe': 'WarCraft', 'role': 'Warrior', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Lt. Morales', 'name_cyr': 'Лейтенант Моралес', 'title': 'Combat Medic', 'title_cyr': 'Боевой медик', 'universe': 'StarCraft', 'role': 'Support', 'combat_type': 'Ranged', 'difficulty': ''}
          {'name': 'Artanis', 'name_cyr': 'Артанис', 'title': 'Hierarch of the Daelaam', 'title_cyr': 'Иерарх дэлаамов', 'universe': 'StarCraft', 'role': 'Warrior', 'combat_type': 'Melee', 'difficulty': ''}
          {'name': '', 'name_cyr': '', 'title': '', 'title_cyr': '', 'universe': '', 'role': '', 'combat_type': '', 'difficulty': ''}
         ]

battlegrounds = [
		 {'name': 'Cursed Hollow', 'name_cyr': 'Проклятая лощина', 'description': 'As one of the first and most ancient realms pulled into the Nexus, the realm of Raven Court has grown large and prosperous over the millennia. The province of Cursed Hollow, a gothic landscape of twisting villages and farmlands, serves as an ideal trial grounds for the Heroes of the Storm.', 'description_cyr': 'Вороний двор — один из самых древних миров, поглощенных Нексусом. За тысячелетия он разросся и достиг процветания. Проклятая лощина — провинция с готическими пейзажами, деревнями и фермерскими угодьями — является идеальным местом сражений для героев Heroes of the Storm.'}
		 {'name': 'Haunted Mines', 'name_cyr': 'Призрачные копи', 'description': 'Far from the Cursed Hollow, on the very borders of Raven Court, lie the Haunted Mines. Sealed beneath a shadowy graveyard, the undead clamor to be released from their earthen prison.', 'description_cyr': 'Вдали от Проклятой лощины, на самом краю Вороньего двора, находятся Призрачные копи. Нежить, оказавшаяся в туннелях под загадочным кладбищем, без устали пытается вырваться на свободу из своей загробной тюрьмы.'}
		 {'name': 'Dragon Shire', 'name_cyr': 'Драконий край', 'description': 'These lush and deceptively peaceful gardens have grown over time, covering the once molten realm known as Dragon Spire. Beneath this verdant paradise, the ancient power of the dragons was sealed away... and their descendants have neither forgotten nor forgiven the trespasses of those who wronged them.', 'description_cyr': 'Цветущие, безмятежные, на первый взгляд, сады Драконьего края выросли на просторах раскаленной пустыни, некогда именуемой Драконьим шпилем. Древняя сила драконов была запечатана в недрах этого райского уголка... и их потомки не забыли и не простили своих давних обидчиков.'}
		 {'name': 'Blackheart’s Bay', 'name_cyr': 'Бухта Черносерда', 'description': 'The ghost pirate Blackheart has staked his claim upon the realm of Mistharbor. His undead pirate crew has poured onto the streets, claiming the once thriving marketplace as their new den of villainy.', 'description_cyr': 'Пират-призрак Черносерд объявил себя владыкой Туманной гавани. Члены его беспутного экипажа, состоящего сплошь из нежити, просочились на улицы, превратив некогда процветающий центр торговли в обитель порока и разбоя.'}
		 {'name': 'Garden of Terror', 'name_cyr': 'Сад Ужасов', 'description': 'Once the royal gardens were a splendor to behold. But lately a shadow has fallen over them... Writhing tendrils creep across the grounds at night, and a number of servants have disappeared while walking its twisting paths. Queen Nightshade claims to be unaware of these incidents, but some are beginning to suspect she has gone mad.', 'description_cyr': 'Когда-то королевские цветники являли собой потрясающее зрелище, но потом их поглотила Тьма... Многие слуги уже сгинули в ночи среди извивающихся живых ростков. Королева Тень утверждает, что не имеет к исчезновениям никакого отношения, но некоторые уже заподозрили, что она сошла с ума.'}
		 {'name': 'Sky Temple', 'name_cyr': 'Небесный храм', 'description': "Floating above the vast desert sands of Luxoria, the Sky Temple serves as a center of worship for the snake god, Ka. He stores his great power within the temples, each of them secured by guardians. With such defenses, no warriors would think to seize the god's power for themselves... or would they?", 'description_cyr': 'Небесный храм, который парит в вышине над бескрайними песками Люксории, служит центром поклонения змеиному богу Ка. В храмах этого священного места сосредоточена великая сила, однако ее зорко оберегают стражи. Чтобы покуситься на эту божественную силу, нужно быть настоящим безумцем... или героем.'}
		 {'name': 'Tomb of the Spider Queen', 'name_cyr': 'Гробница королевы пауков', 'description': 'The long forgotten tombs of Luxoria have found a new master. Deep within their timeworn chambers, the Spider Queen Neithis stirs from her ancient slumber. Present her with the gems of power she seeks, and you may just escape with your lives.', 'description_cyr': 'Глубоко под осыпающимися сводами позабытых гробниц Люксории пробудилась ото сна королева пауков Неитис. Принесите ей кристаллы силы, и, возможно, она вас пощадит.'}
		 {'name': 'Battlefield of Eternity', 'name_cyr': 'Вечная битва', 'description': 'The High Heavens and the Burning Hells clash, quite literally, in a battlefield that represents their everlasting struggle. Two Immortals, ancient warriors locked in a duel to the death, need your help to prevail against their eternal foe. Vanquish the enemy Immortal, and you’ll find yourself charging over hallowed or profane ground—right onto the enemy’s doorstep.', 'description_cyr': 'Небеса и Преисподняя столкнулись (в буквальном смысле) на поле боя, олицетворяющем их вечное противостояние. Бессмертным, двум древним воителям, обреченным вечно сражаться друг с другом, необходима ваша помощь в решении исхода их бесконечной битвы. Уничтожьте Бессмертного вражеской команды, и тогда ничто не сможет помешать вам пронестись опустошительным вихрем по территории противника.'}
		 {'name': 'Infernal Shrines', 'name_cyr': 'Оскверненные святилища', 'description': "Demonic corruption threatens the Gardens of Hope. Called forth by the Shrines, Punishers prowl the battlefield, terrifying creatures that live to destroy heroes. Defeat the Shrines' Guardians before your enemies do, and the next Punisher will fight for you; fail, and face the demon's wrath.", 'description_cyr': 'Скверна собирается проникнуть в Сады Надежды. Каратели, питаемые силой святилищ, наводят ужас на поле боя. Эти ужасные существа живут для того, чтобы уничтожать героев. Одолейте стражей святилища до того, как это сделают противники, и появившийся каратель будет сражаться на вашей стороне. Если же вы не справитесь, вас настигнет гнев Преисподней.'}
		 {'name': '', 'name_cyr': '', 'description': '', 'description_cyr': ''}
		]
