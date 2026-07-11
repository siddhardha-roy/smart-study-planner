import math
def k_mean(subjects,dic_1) :
     
 k_1=(1.5,2)
 k_2=(2.5,3)
 k_3=(3,5)

 for _ in range(100) :
    k_mean_1=[]
    k_mean_2=[]
    k_mean_3=[]
    diff_1=[]
    diff_2=[]
    diff_3=[]

    for i in subjects :
         j,k = dic_1[i]
         mean=(j,k)
         one_1=math.pow((mean[0]-k_1[0]),2)
         sec_1=math.pow((mean[1]-k_1[1]),2)
         one_2=math.pow((mean[0]-k_2[0]),2)
         sec_2=math.pow((mean[1]-k_2[1]),2)
         one_3=math.pow((mean[0]-k_3[0]),2)
         sec_3=math.pow((mean[1]-k_3[1]),2)
         if abs(math.sqrt(one_1+sec_1)) < abs(math.sqrt(one_2+sec_2)) and abs(math.sqrt(one_1+sec_1)) < abs(math.sqrt(one_3+sec_3)) :
                k_mean_1.append(mean)
                diff_1.append(i)

         elif abs(math.sqrt(one_2+sec_2)) < abs(math.sqrt(one_3+sec_3)) :
                k_mean_2.append(mean)
                diff_2.append(i)
         else :
                k_mean_3.append(mean)
                diff_3.append(i)
     
    if k_mean_1:
        x=0
        y=0
        for i in k_mean_1 :
             x+=i[0]
             y+=i[1]
        new_k_1=(x/len(k_mean_1),y/len(k_mean_1))
    else :
        new_k_1=k_1
    if k_mean_2:
        x=0
        y=0
        for i in k_mean_2 :
             x+=i[0]
             y+=i[1]
        new_k_2=(x/len(k_mean_2),y/len(k_mean_2))
    else :
        new_k_2=k_2
    if k_mean_3:
        x=0
        y=0
        for i in k_mean_3 :
             x+=i[0]
             y+=i[1]
        new_k_3=(x/len(k_mean_3),y/len(k_mean_3))
    else :
        new_k_3=k_3
    
    if abs(math.sqrt(math.pow(new_k_1[0]-k_1[0],2) + math.pow(new_k_1[1]-k_1[1],2)))<0.01 and abs(math.sqrt(math.pow(new_k_2[0]-k_2[0],2) + math.pow(new_k_2[1]-k_2[1],2))) <0.01 and abs(math.sqrt(math.pow(new_k_3[0]-k_3[0],2) + math.pow(new_k_3[1]-k_3[1],2))) <0.01 :
        return diff_1,diff_2,diff_3

    k_1,k_2,k_3=new_k_1,new_k_2,new_k_3
 return diff_1,diff_2,diff_3