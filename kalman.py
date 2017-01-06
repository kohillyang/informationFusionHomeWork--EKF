#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['YaHei Consolas Hybrid']#
plt.rcParams['axes.unicode_minus']=False #
z=[1.9945,1.9794,1.9554,1.9214,1.8777,1.8250,1.7598,1.6867,
   1.6036,1.5092,1.4076,1.2944,1.1724,1.0399,0.8980,0.7455,
   0.5850,0.4125,0.2318,0.0399]
z = list(map(lambda x:x*1000,z))
x = [];P=[]  #分配空间
A = np.mat([ [ 1, 0 ],
             [-1, 1 ] ]) 
H = np.mat([[0,1]])
R = 1
x.append(np.mat([ [10],[1900] ])) #设定初值
P.append (np.mat([[100 ,0],
                  [0   ,2] ]))
for  i in range(len(z)):
    x_k_plus = A*x[i] + np.mat( [ [1] , [-0.5] ])*9.8#先验估计
#     P_k_plus = A*P[i]*A.T
    K_k =  P_k_plus *H.T* np.linalg.inv(H*P_k_plus*H.T + R)
    x.append(x_k_plus+K_k * (z[i] - H * x[i]))
    P.append( (np.eye(2,2)-K_k*H) * P_k_plus )
    x.append(x_k_plus)
    pass
plt.figure()
plt.grid();
plt.plot(np.linspace(1,21,21),list(map(lambda m:m[1,0],x)),label = "卡尔曼滤波估计")
plt.plot(np.linspace(1,20,20),z,label = '量测值')
plt.legend()
plt.xlabel("Time(s)");plt.ylabel("h(m)");plt.title("原始量测与卡尔曼估计对比")
plt.show()#
