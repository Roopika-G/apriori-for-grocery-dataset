import matplotlib.pyplot as plt
plt.plot([100,200,300,400],[1.866, 11.835, 65.344, 313.214])
plt.plot([100,200,300,400],[0.076, 0.778, 1.008, 2.030])
plt.ylabel('Time Taken (Sec)')
plt.xlabel('Number of transaction')
#plt.xlim([100, 400])
#plt.ylim([0.0, 350.0])
plt.title('Time Plot (Brute Force Vs Apriori)')
plt.legend(loc="lower right")

plt.show()





#plt.plot([100,200,300,400],[1.866, 11.835, 65.344, 313.214])
#plt.plot([100,200,300,400],[0.076, 0.778, 1.008, 2.030])