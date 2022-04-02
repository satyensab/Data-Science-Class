import matplotlib.pyplot as plt
import numpy as np

#1
time = np.arange(np.pi*-3,np.pi*3+1.5,0.1)
amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)

#sin graph : Implementation Source:https://stackoverflow.com/questions/35372993/can-i-make-a-multi-color-line-in-matplotlib
for time1, time2, amplitude_sin1,amplitude_sin2 in zip(time, time[1:], amplitude_sin, amplitude_sin[1:]):
    if amplitude_sin1 > amplitude_sin2:
        plt.plot([time1, time2], [2* amplitude_sin1, 2* amplitude_sin2], color = 'green')
    elif amplitude_sin1 < amplitude_sin2:
        plt.plot([time1, time2], [2* amplitude_sin1, 2* amplitude_sin2], color = 'red')
           
#cos graph: Implementation Source:https://stackoverflow.com/questions/35372993/can-i-make-a-multi-color-line-in-matplotlib
for time1, time2, amplitude_cos1,amplitude_cos2 in zip(time, time[1:], amplitude_cos, amplitude_cos[1:]):
    if amplitude_cos1 > amplitude_cos2:
        plt.plot([time1, time2], [2* amplitude_cos1, 2* amplitude_cos2], linestyle = 'dotted', color = 'green')
    elif amplitude_cos1 < amplitude_cos2:
        plt.plot([time1, time2], [2* amplitude_cos1, 2* amplitude_cos2], linestyle = 'dotted', color = 'red')
           
plt.xlabel('X',fontsize = 15)
plt.ylabel('Y', fontsize = 15)
plt.ylim([-4,4])
plt.grid(color = 'b', alpha = 0.2)
plt.legend(['2sin(x)','2cos(x)'])

plt.show()


#2
X = np.random.rand(1000) * 100
Y = np.random.normal(50, 10, 1000)

#Mean/Std of X
mean_x = X.mean()
std_x = X.std()

#Mean/Std of Y
mean_y = Y.mean()
std_y = Y.std()

print("Mean of X: " + str(round(mean_x,2)))
print("Standard Dev. of X: " + str(round(std_x,2)))
print()
print("Mean of Y: " + str(round(mean_y,2)))
print("Standard Dev. of Y: " + str(round(std_y,2)))

plt.subplot(1,2,1)
plt.hist(X, bins=20)
plt.title('X Histogram')

plt.subplot(1,2,2)
plt.hist(Y, bins=20)
plt.title('Y Histogram')

plt.show()
