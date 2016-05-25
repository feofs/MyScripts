a=input('Enter A number :')
b=input('Enter another number :')
print('Zdes poluchim prosto stroku iz dvuh chisel i strokoviy type(sum)')
sum=a+b
print('Summ i tip dannih :',sum,type(sum))
sum=int(a)+int(b)
print('Summ i tip dannih :',sum,type(sum))
sum=float(sum)
print('Summ i tip dannih :',sum,type(sum))
print('A zdes srazu funkcya v funkcii sum=chr(int(sum))')
sum=chr(int(sum))
print('Summ i tip dannih :',sum,type(sum))
a=10
b=5
print('a=',a,'\t b=',b)
b=a^b
print('Now B =',b)
a=a^b
print('Now A =',a)

print('Zdes mi rassmotrim spiski')
nums=[10,20,30,40,50]
print ('Perviy i vtoroy elementi',nums[0],'\t vtotoy :',nums[1])
quarter=['January','February','Macrh']
print ('The first month is :', quarter[0])
print ('The second month is :', quarter[1])
print ('The third month is :', quarter[2])
print ('esli obratitsya tak 0,0 to vivedem pervyu bukvu mesuaca',quarter[0][0])


array=[[1,2,3],[4,5,6]]
print ('Verhniy element massiva 0,0 :',array[0][0])
print ('Element vtorogo massiva pod nomerom 3 to est 1,2 :',array[1][2])
