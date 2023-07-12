entry_list = [1,2,3,4,5]
output_dict = {entry_list[i]: entry_list[i] for i in range(len(entry_list))}
#print(output_dict)
#{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


res_list = {x: x**2 for x in range(1,6)}
#print(res_list)
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

multiplication = 1
my_dict = {'data1': 375,'data2':567,'data3': -37,'data4': 21}
all_keys = my_dict.keys()
for key in all_keys:
    multiplication *= my_dict[key]
#print(multiplication)
#problem3 -165209625

symbols = ['.', ',', ':', ';', '!', '?']
count = 0
text = '"Летний день - это день, когда наступает летнее ' \
       'солнцестояние и длительность дня достигает своего максимума. ' \
       'В разных странах и регионах летние дни могут иметь разную продолжительность и характеризоваться разными погодными условиями. ' \
       'Вообще, летние дни обычно ассоциируются с теплой и ясной погодой, зелеными лугами, пляжами, купанием в море или озере, пикниками и барбекю. ' \
       'В летние дни люди часто отдыхают и проводят время на открытом воздухе,занимаются спортом,путешествуют и открывают новые места!"'
for i in range(len(text)):
    if text[i] in symbols:
        count += 1
#print(count)
#problem4 12

given_string = 'kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d'
unique_digits = set()
count_letters = 0
alf = 'abcdefgijklmopqrstuvwxyz'
alf = alf + alf.upper()
alf = set(alf)
for symbol in given_string:
    if ord(symbol) >= 48 and ord(symbol) <=57:
        unique_digits.add(int(symbol))
    if symbol in alf:
        count_letters += 1

unique_digits = sorted(list(unique_digits))
print(unique_digits)
if count_letters == 0:
    print('NO')
#problem5 [1, 2, 4, 5, 6, 7, 8, 9]
