import numpy as np
import matplotlib.pyplot as plt
s=100
# x1 is uniformly distributed between 1,10
test_x1=np.random.uniform(1,10,s);
#x2 is unifomly distributed between 2,5
test_x2=np.random.uniform(2,5,s);
test_target=[]
for i in range(s):
    t=4+test_x1[i]+3*test_x2[i];
    test_target.append(t)

def array_split(arr, k):
    length = int(len(arr)/k) 
    folds = []
    for i in range(k-1):
        folds += [arr[i*length:(i+1)*length]]
    folds += [arr[(k-1)*length:len(arr)]]
    return folds



def newTheta(theta,eta,Z,Y):
    a=np.transpose(Z)
    b=np.dot(Z,theta)
    c=np.subtract(b,Y)
    d=np.dot(a,c)
    d=2*eta*d;
    return np.subtract(theta,d)

def gradientJ(theta,Z,Y):
    a=np.transpose(Z)
    b=np.dot(a,Z)
    c=np.dot(a,Y)
    d=np.dot(b,theta)
    gradient=2*d-2*c;
    return gradient;


def training_set(n):
    x1=np.random.uniform(1,10,n);
    x2=np.random.uniform(2,5,n);
    training_dataset=[]
    for i in range(n):
        training_ele=[x1[i],x2[i]]
        t=4+x1[i]+3*x2[i];
        
        #noice added which is as normal distribution
        t=t+np.random.uniform(0,0.25);
        training_ele.append(t)
        training_dataset.append(training_ele)
    
    np.random.shuffle(training_dataset)
    ten_datasets=array_split(training_dataset,10);
    theta_array=[];
    for ele in ten_datasets:
        theta=np.vstack([[0.0],[0.0],[0.0]]);
        Y=[]
        for i in range(len(ele)):
            Y.append(ele[i][2]);
        Y=np.vstack(Y);
        Z=[]
        for i in range(len(ele)):
            x=[1.0,ele[i][0],ele[i][1]];
            Z.append(x);
        Z=np.vstack(Z);
        eta=1e-4
        for i in range(5000):
            # if(i<400):
            #     eta=1e-3
            theta=newTheta(theta=theta,eta=eta,Z=Z,Y=Y)
            f=gradientJ(theta=theta,Z=Z,Y=Y);
            det=f[0]-f[1]+f[2]
            det=abs(det)
            if(det<0.01):
                break;
        theta_array.append(theta);

    return theta_array
    
bias_array=[]
varience_array=[]
for z in range(100,1001,100):
    theta_array=training_set(z)
    bias_all=0;
    varience_all=0
    for k in range(0,s):
        ym=0;
        y_predicted=[];
        for e in theta_array:
            y1=e[0]+e[1]*test_x1[k]+e[2]*test_x2[k];
            y_predicted.append(y1);
            ym+=y1;

        ym=ym/10;
        bias_x=(test_target[k]-ym)**2
        bias_all+=bias_x
                
        varience_x=0;
        for e in y_predicted:
            varience_x+=(e-ym)**2

        varience_x=varience_x/10;
        varience_all+=varience_x

    print("bias for size ",z,": ",(bias_all/s)[0])
    print("varience for size",z,": ",(varience_all/s)[0]);
    bias_array.append(bias_all/s)
    varience_array.append(varience_all/s)
    
print(bias_array)
print(varience_array)

n_array=[100,200,300,400,500,600,700,800,900,1000]
plt.plot(n_array,bias_array)
plt.plot(n_array,varience_array)
plt.show()