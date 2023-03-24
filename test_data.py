from pprint import pprint

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def patriot_filter():
    new_geo_log = []
    for visit in geo_logs:
        for location in visit.values():
            if location[1] == 'Россия':
                new_geo_log.append(visit)
    return new_geo_log


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def id_filter():
    unique_list = []
    for num in ids.values():
        for point in num:
            if point not in unique_list:
                unique_list.append(point)
    return unique_list


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def stat_review():
    stat_dict = {}
    stat_dict_correct = {}
    count = 0
    for string in queries:
        point = len(string.split())
        if point in stat_dict.keys():
            num = int(stat_dict[point])
            stat_dict[point] = num + 1
            count += 1
        else:
            stat_dict[point] = 1
            count += 1
    for i in stat_dict:
        stat_dict_correct[f'Процентная доля запросов из {i} слов: '] = f'{round(int(stat_dict[i])/count*100, 2)} %'
    print(count)

    return stat_dict_correct
