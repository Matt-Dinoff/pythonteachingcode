import os

os.system("curl -k https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt")

print("Matt Dinoff")

mean_temp = open('mean_temp.txt','a+')
mean_temp.write("\nRio de Janerio,Brazil,30.0,18.0\n")

mean_temp.seek(0,0)
headings = mean_temp.readline()
headings = headings.split(',')

city_temp = mean_temp.readline().strip("\n")
while city_temp:
    city_temp = city_temp.split(',')
    print(headings[0],"of", city_temp[0],headings[2], "is",city_temp[2], "Celsius")
    city_temp = mean_temp.readline().strip("\n")

mean_temp.close()