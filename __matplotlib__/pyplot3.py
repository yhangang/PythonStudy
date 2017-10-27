# -*- coding: utf-8 -*-  
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

func = np.poly1d(np.array([1,2,3,4]))
func1 = func.deriv(m=1)  # 求一阶导数
func2 = func.deriv(m=2)  # 求二阶导数

#初始化数据
x = np.linspace(-10,10,30)
y = func(x)
y1 = func1(x)
y2 = func2(x)

#正常绘图
plt.plot(x,y,'ro',x,y1,'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

'''添加子图'''
plt.subplot(311)
plt.plot(x,y,c='r',linestyle='-')
plt.title('Polynomial')

plt.subplot(312)
plt.plot(x,y1,c='b',linestyle='',marker='^')
plt.title('First Derivative')

plt.subplot(313)
plt.plot(x,y2,c='g',linestyle='',marker='o')
plt.title('Second Derivative')


'''对数坐标'''
plt.semilogx(x,y)  # 对x取对数
plt.semilogy(x,y)  # 对y取对数
plt.loglog(x,y)    # 同时取对数
plt.show()


'''颜色填充'''
fig = plt.figure()
ax = fig.add_subplot(211)
ax.fill_between(x,y,y1,facecolor='b')
ax.grid(True)
ax2 = fig.add_subplot(212)
ax2.fill(x,y,facecolor='b',alpha=0.3)
ax2.fill(x,y1,facecolor='g',alpha=0.3)
ax2.grid(True)
plt.show()


'''三维绘图'''
u = np.linspace(-1,1,100)
x,y = np.meshgrid(u,u)     # 网格坐标生成函数
z = x**2+y**2
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z,rstride=4,cstride=4,cmap='rainbow')
plt.show()


'''三维绘等高线图'''
u = np.linspace(-1,1,100)
x,y = np.meshgrid(u,u)     # 网格坐标生成函数
z = x**2+y**2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(x,y,z)
plt.show()











