import pickle
import numpy as np

f_inte_path=r'alluserinterest.txt'
f_in_fenxi_path=r'interest_number_fenxi'
def mod(x):
    if not isinstance(x,np.ndarray):
        raise TypeError('bad operand type')
    i=len(x[0])
    j=0
    a=[]
    while i:
        i=i-1
        a.append(np.argmax(np.bincount(x[:,j])))
        j=j+1
    return a

def interest():
    with open(f_inte_path,'rb') as f_interest:
        in_fenxi_dict=dict()
        intere=pickle.load(f_interest)
        a=list(intere.values())
        np_a=np.array(a)
        in_fenxi_dict['max']=np.max(np_a,axis=0).tolist()
        in_fenxi_dict['mean']=np.mean(np_a,axis=0).tolist()
        in_fenxi_dict['median']=np.median(np_a,axis=0).tolist()
        in_fenxi_dict['var']=np.var(np_a,axis=0).tolist()
        in_fenxi_dict['mode']=mod(np_a)
    return in_fenxi_dict

def load(fpath=f_in_fenxi_path):
    with open(fpath,'rb') as f:
        data=pickle.load(f)
    return data
#a=interest()
#f=open("interest_number_fenxi",'wb')
#pickle.dump(a,f)
#f.close()
#print(a)
