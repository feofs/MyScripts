
import MyModules.MyBinaryFile as BF
import os
if os.path.exists("mybikes.data"):
    os.remove("mybikes.data")
data=BF.BikeStock("mybikes.data")
bike=BF.Bike('1001','Formula',1,120.29)
data.append(bike)
bike=BF.Bike('1002','Leyla',1,142.44)
data.append(bike)
bike=BF.Bike('1003','America',1,142.44)
data.append(bike)

bike=BF.Bike('1004','Scarpa',1,142.44)
data.append(bike)

bike=BF.Bike('1005','Euorope',1,142.44)
data.append(bike)

bike=BF.Bike('1006','Asia',1,142.44)
data.append(bike)

del data['1004']
print(data.__dict__)
for bike in data:
    print(bike.name)
