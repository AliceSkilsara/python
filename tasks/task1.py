# В американской армии считается несчастливым число 13, а в японской — 4.
# Перед международными учениями штаб российской армии решил исключить номера боевой техники,
# содержащие числа 4 или 13 (например, 40123, 13313, 12345 или 13040), чтобы не смущать
# иностранных коллег. Если в распоряжении армии имеется 100 тыс. единиц боевой техники и
# каждая боевая машина имеет номер от 00001 до 99999, то сколько всего номеров придётся
# исключить?

count=0
for i in range(1, 100000):
    if "4" in str(i) or "13" in str(i):
        count+=1
print("count=",count)



