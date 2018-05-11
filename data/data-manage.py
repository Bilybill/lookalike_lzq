import pickle

fpath = r'userFeature.data'
fapath = r'user_group0'

def interest_cal(struser):
    if not isinstance(struser,str):
        raise TypeError("bad operand type")
    s=str(struser)
    feature = 'interest'
    a=[]
    for i in range(1,6):
        feas=feature+str(i)
        if s.count(feas):
            begin=s.index(feas)
            end=s.index('|',begin)
            s_clip=s[begin+len(feas):end]
            a.append(s_clip.count(" "))
        else:
            a.append(0)
    return a

with open(fpath,'r',encoding='utf-8') as f:
    user_intere_dict=dict()
    i=0
    j=1
    for aline in f:
        i=i+1
        if i==100000:
            print(str(j)+"00000 times")
            j=j+1
            i=0
        aline=str(aline)
        end=aline.index('|')
        userid=aline[4:end]
        user_intere_dict[userid]=interest_cal(aline)
    f_intere=open('alluserinterest.txt','wb')
    pickle.dump(user_intere_dict,f_intere)
    f_intere.close()
    print("have done")
   # print(user_intere_dict)
