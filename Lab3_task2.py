# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(a, b, separator = ','):
    common_people = []
    a = a.split(separator)
    b = b.split(separator)

    for i in a:
        for j in b:
            if i == j:
                common_people.append(i)
    common_people.sort()
    return(common_people)




print(find_common_participants(participants_first_group, participants_second_group, separator = "|"))