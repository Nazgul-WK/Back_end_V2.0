from datetime import datetime
current_datetime = datetime.now()
day = (current_datetime.day)
month = (current_datetime.month)
print ("Пожалуйста введите текущую температуру воздуха на улице")
temperature = int(input())
if temperature > 0:
    print ("Сегодня " + str(day) + "." + str(month) + "."  + "2023. " + "На улице " + str(temperature) + " градуса.")
else:
    print ("Сегодня " + str(day) + "." + str(month) + "."  + "2023. " + "На улице " + str(temperature) + " градуса. Холодно, лучше остаться дома.")

