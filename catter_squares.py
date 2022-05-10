import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,s=1,c=y_values,cmap=plt.cm.Blues)

ax.set_title('squres',fontsize=24)
ax.set_xlabel('number',fontsize=14)
ax.set_ylabel('values',fontsize=14)

ax.tick_params(axis='both',which='major',labelsize=14)

ax.axis([0,1100,0,1100000])

#plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()