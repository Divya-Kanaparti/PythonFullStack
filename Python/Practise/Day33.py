#MATPLOTLIB
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,50,30]
plt.plot(x,y,marker='*',color='red',linestyle='--')
plt.title("Line-Plot")
plt.xlabel("X-data")
plt.ylabel("Y-data")
plt.grid(True)
plt.show()
#eg:2
months=['jan','feb','mar','apr']
exp=[1000,5000,4000,6000]
inc=[2000,10000,7000,8000]
plt.plot(months,exp,label='exp')
plt.plot(months,inc,label='inc')
plt.title("month-wise inc-exp")
plt.xlabel("months")
plt.ylabel("inc-exp")
plt.legend()
plt.grid(True)
plt.show()
#eg:3
cities=['hyd','ben','vizag','chenai']
sales=[90000,10500,78000,65000]
plt.bar(cities,sales)
plt.title("sales in cities")
plt.xlabel("cities")
plt.ylabel("sales")
plt.grid(True)
plt.show()
#eg:4
l=['banana','apple','mango','grapes']
perc=[30,35,15,20]
plt.pie(perc,labels=l,autopct='%1.1f%%')
plt.grid(True)
plt.show()