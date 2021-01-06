import matplotlib as plt
%matplotlib inline
fig, ax = plt.subplots(1,1,figsize=(1,1),dpi=120)

x = np.linspace(0,1,1000)
taf = lambda x:tf(x,0.4)

ax.plot(x,f(x), label='original')
ax.plot(x,taf(x), label='aproximacion')
ax.scatter(0.4,f(0.4), color='red')
ax.legend()
plt.show()