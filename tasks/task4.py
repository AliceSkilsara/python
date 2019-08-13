# В городе N проезд в трамвае осуществляется по бумажным отрывным билетам. Каждую неделю
# трамвайное депо заказывает в местной типографии рулон билетов с номерами от 000001 до 999999.
# \«Счастливым» считается билетик у которого сумма первых трёх цифр номера равна сумме
# последних трёх цифр, как, например, в билетах с номерами 003102 или 567576. Трамвайное
# депо решило подарить сувенир обладателю каждого счастливого билета и теперь раздумывает,
# как много сувениров потребуется. С помощью программы подсчитайте сколько счастливых билетов
#

count = 0
for i in range(1, 1000000):
    string = "{0:0=6d}".format(i)
    sum1 = 0
    sum2 = 0
    for j in string[0:3]:
        sum1 += int(j)
    for j in string[3:6]:
        sum2 += int(j)
    if sum1 == sum2:
        count += 1
#        print(string)
print("count=", count)
