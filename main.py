from array import array
from statistics import variance
import numpy as np
import matplotlib.pyplot as plt

def newtheta(theta,eta,m1,m):
    a=m.transpose()
    b=np.dot(m,theta)
    c=np.subtract(b,m1)
    d=np.dot(a,c)
    d=2*eta*d
    return np.subtract(theta,d)

def jGradient(theta,Z,Y):
    a=np.transpose(Y)
    b=np.dot(a,Y)
    c=np.dot(a,Z)
    d=np.dot(b,theta)
    gradient=2*d-2*c
    return gradient

def funct(x1,x2):
    k=4+x1+3*x2
    return k

def addNoise(val):
    noise = np.random.normal(0,0.25)
    val=val+noise
    return val

x1=np.random.uniform(1,10,100)
x2=np.random.uniform(2,5,100)
testSet=[]
for i in range(100):
    v=[]
    v.append(x1[i])
    v.append(x2[i])    
    k=funct(x1[i],x2[i])
    v.append(k)
    testSet.append(v)
bias1=[]
variance1=[]
for i in range(100,1001,100):
    print("For ",i," training dataset value of bias and variance ...")
    x3=np.random.uniform(1,10,i)
    x4=np.random.uniform(2,5,i)
    trainingdata=[]
    for j in range(i):
        v=[]
        v.append(x3[j])
        v.append(x4[j])
        k=funct(x3[j],x4[j])
        v.append(addNoise(k))
        trainingdata.append(v)
        splittraiining=[]
    val=int(i/10)    
    for j in range(0,i,val):
        v=[]
        for k in range(j,j+val):
            v.append(trainingdata[k])
        splittraiining.append(v)
    ycheck=[]  
    print(len(splittraiining))   
    theta_array=[]
    for ele in splittraiining:    
        theta=np.vstack([[0.0],[0.0],[0.0]])
        eta=1e-4
        Y=[]
        Z=[]
        for j in range(len(ele)):
            x=[1,ele[j][0],ele[j][1]]
            y=[ele[j][2]]
            Y.append(x)
            Z.append(y)
        Y=np.vstack(Y)
        Z=np.vstack(Z)
        #   min_j=jGradient(theta,Z,Y)
        #   k1=theta
        #   optheta=k1

        for j in range(5000):
            theta=newtheta(theta,eta,Z,Y)
            f=jGradient(theta,Z,Y)
            det=f[0]-f[1]+f[2]
            det=abs(det)
            if(det<0.01):
                break

        theta_array.append(theta)
    bias_for_space=0
    variance_for_apce=0    
    for e in testSet:
        ym=0  
        yv=0
        y_predicted=[]
        for ele in theta_array:
            ym+=ele[0]+ele[1]*testSet[0][0]+ele[2]*testSet[0][1]
            y_predicted.append(ele[0]+ele[1]*testSet[0][0]+ele[2]*testSet[0][1])
        ym/=10
        # print(ym)
        # print(testSet[0][2])
        bias=0
        bias=(testSet[0][2]-ym)**2
        # print(bias)
        bias_for_space+=bias
        # for ele in ycheck:
        #     k=(ele[0]-ym)**2
        #     yv+=k
        # bias=0   
        # for ele in testSet:
        #     p=(ele[2]-ym)**2
        #     bias+=p
        for ele in y_predicted:
            yv+=(ele-ym)**2
        yv/=10
        # print(yv)
        variance_for_apce+=yv
    
    print("Bias is:",bias_for_space/100)
    print("Variance is: ",variance_for_apce/100)    
    bias1.append(bias_for_space/100)
    variance1.append(variance_for_apce/100)


n=[100,200,300,400,500,600,700,800,900,1000]
plt.plot(n,bias1)
plt.plot(n,variance1)
plt.show()    