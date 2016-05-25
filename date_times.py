import datetime,time
#Если мы делаем импорт так а не import from то тогда получется к функции today нужно обратиться так т.к она находиться в модуле datetitime в объекте datetime то запишем так
today=datetime.datetime.today()
print('Today is :',today)

#а так как time это просто функция в модуле time а не в объекте то запишем так
start=time.time()
i=1
while i<3:
    time.sleep(1)
    i+=1
end=time.time()
diff=end-start
print('Program exected time :',diff)

#Также есть функции gmtime - время по гринвичу, и localtime - локальное время которые создают объект struct_time с аттрибутами tm_year, tm_day,tm_hour, tm_month и т.д
time_object=time.localtime(start)
gr_time_object=time.gmtime(start)
print('The type of structured time object is :',type(time_object))
print('Year,month,day,hour',time_object.tm_year,time_object.tm_mday,time_object.tm_hour)
print('Time by Grinvich :',gr_time_object.tm_hour,':',gr_time_object.tm_sec)

