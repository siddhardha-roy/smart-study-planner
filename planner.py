import streamlit as st
import math

st.title("Welcome to Smart study planner ")
subjects=[]
subject=input("enter the subjects :")
subjects=subject.split(",")
for i in subjects :
    print(i)
dic_1=dict.fromkeys(subjects)
print(dic_1)
difficulty=[]
time=[]
for i in subjects :
    difficulty.append(input(f"enter the difficulty level of {i} (1-->easy,2-->medium,3-->hard) :"))
    time.append(input(f"enter the time you think  to learn subject :"))

for i,k,j in zip(subjects,difficulty,time) :
    dic_1[i]=int(k),float(j)
print(dic_1)

#k-means     (1-D)

 
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
        break

    k_1,k_2,k_3=new_k_1,new_k_2,new_k_3
# print(diff_1)
# print(diff_2)
# print(diff_3)

#three functions
#1.genatrating a time table
#2.checking the score
#3.hill_climbing function  #3
import random

def time_table() :
     days=["Mon","Tue","Wed","Thu","Fri"]
     study_planner=dict()
     study_planner=dict.fromkeys(days)
     print(study_planner)
     for i in study_planner :
         a=random.randint(1,6)
         b=random.randint(1,6)
         c=random.sample(subjects,2)
         d={
              c[0]:a,
              c[1]:b
            }
         study_planner[i]=d
     return study_planner

def score(work) :
     #if both are diff score --> -
     #if one is diff and other is easy --> +
     #if time >6 --> -
     #not good enough
     score=100
     for i in work :
          a=list(work[i].keys())
          if a[0] in diff_3 :
               if a[1] in diff_3 :
                    score-=30
               elif a[1] in diff_2 :
                    score+=10
               else :
                    score+=20
          b=list(work[i].values())
          if sum(b) >6 :
               score -=30
          else :
               score +=40

     return score
                    
def hill_climbing() :
     #genatrate a time table
     #check it's score
     #genatrate another time table and check it's score too
     #keep the time_table which has high score
     #stop if nothing changes
      table=time_table()
      score_1=score(table)
      count=0
      for _ in range(1000) :
          new_table=time_table()
          new_score=score(new_table)
          if score_1 <new_score :
               score_1=new_score
               table=new_table
               count=0
          else :
               count +=1
          if count == 4 :
               break
      return table

best_schedule = hill_climbing()
print(best_schedule)
print("Best Score:", score(best_schedule))
     