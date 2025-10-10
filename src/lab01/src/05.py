fio = input()
names = fio.split(" ")
names1 = []
for i in range(len(names)):
    if (names[i]!=''):
        names1.append(names[i])
let11 = names1 [0][0]
let21 = names1 [1][0]
let31 = names1 [2][0]
count = 0
for i in range(len(fio)):
    if (fio[i]==' '):
        count= count+1
lastName = names1[0]
firstName = names1[1]
middleName = names1[2]
print("ФИО: " + lastName + " " + firstName + " " + middleName)
print("Инициалы: " + let11 + let21 + let31 + ".")
print("Длина (символов): " + str(len(fio) - count + 2)) 