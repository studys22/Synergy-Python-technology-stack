# А теперь мы с тобой напишем форму ввода ответа на тест по биологии для студентов. Он должен запрашивать по порядку этапы развития человека (проверим твое умение гуглить, что тоже очень важно для программиста. ) и в конце вывести все стадии, разделенные знаком =>, что будет означать постепенный переход от одного к другому. В следующих уроках мы дополним эту форму до полноценного теста, который будет проверять правильность ответов, а пока - начнем с малого. Напоминаем, что разделить эти данные тебе поможет команда sep внутри команды print, например, чтобы разделить переменные знаком + нужно ввести:
#
# print(a1, a2, a3, sep='+')
#
# Подсказка: последняя стадия развития - Homo sapiens sapiens.

""" 
stages = [
     "Hominoidea",
     "Hominidae",
     "Homininae",
     "Hominini",
     "Australopithecus ",
     "Homo erectus",
     "Homo heidelbergensis",
     "Homo sapiens sapiens",
 ]
 print(*stages, sep=" => ")
 """

s1 = input('Enter the 1st stage of human development "Homo...": ')
s2 = input('Enter the 2nd stage of human development "Homo...": ')
s3 = input('Enter the 3rd stage of human development "Homo...": ')

print(s1, s2, s3, sep=" => ")
