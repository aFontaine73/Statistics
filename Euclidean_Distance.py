from math import sqrt


plot1 = []
print("please input the x value for plot 1")
plot1.append(int(input()))
print("please input the y value for plot 1")
plot1.append(int(input()))

plot2 = []
print("please input the x value for plot 2")
plot2.append(int(input()))
print("please input the y value for plot 2")
plot2.append(int(input()))

euclidean_distance = sqrt((plot1[0] - plot2[0]) ** 2
                          + (plot1[1] - plot2[1]) **2)

print(euclidean_distance)
