# TODO  Напишите функцию count_letters

def count_letters(a):
    c = ""
    s = []
    freq = []

#проверка на букву
    for i in a:
        if i.isalpha():
            c+=i.lower()
#Составление списков символов и их количеств в тексте
    for i in range (0, 32):
        s.append(chr(i+1072))
        freq.append(c.count(chr(i+1072)))

#Частота встреч буквы
    for i in range(len(freq)):
        freq[i] = freq[i]/(len(c))
        freq[i] = round(freq[i], 2)

#Объединение двух массивов в один
    for i in range(32):
        s[i] = ([s[i], freq[i]])
    return [s]

# TODO Напишите функцию calculate_frequency
#Не придумал, как нормально написать через две функции, поэтому объеденил в одну

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте

a = count_letters(main_str)
a = a[0]    #Сброс дополнительного измерения массива, образовавшегося после работы функции
for i in a:
    print(str(i[0])+" : " + str(i[1]))