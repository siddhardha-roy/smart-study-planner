import random
import copy
days=["Mon","Tue","Wed","Thu","Fri"]
 
def final (subjects,diff_1,diff_2,diff_3) :
 def neigbhour(table,subjects) :
     #change the hours
     # change the subjects
     # small change in time table
      new_table=copy.deepcopy(table)
      gamble=random.randint(1,2)

      if gamble==1 :
          # for i in days :
          #      count=0
          #      for value in new_table[i].keys() :
          #           coin=random.randint(1,2)
          #           count+=1
          #           if coin==1 :
          #                new_table[i][value]+=random.randint(1,2)
          #           else :
          #                 new_table[i][value]=max(1,abs(new_table[i][value]-random.randint(1,2)))
          #      if count==random.randint(1,3) :
          #           break
          i=random.choice(days)
          sub=new_table[i].keys()
          a=random.choice(list(sub))
          new_table[i][a]+=random.randint(-2,2)
      elif gamble==2 :
           i=random.choice(days)
           old=random.choice(list(new_table[i].keys()))
           available=[sub for sub in subjects
                      if sub not in new_table[i]]
           if available :
               hours=new_table[i].pop(old)
               new=random.choice(available)
               new_table[i][new]=hours
           
      return new_table
     #  else :
     #      a,b=random.sample(days,2)
     #      temp=new_table[a]
     #      new_table[a]=table[b]
     #      new_table[b]=temp

 def time_table() :
     study_planner=dict()
     # study_planner=print(study_planner)
     study_planner = {day:{} for day in days}
     for sub in subjects:
      day = random.choice(days)

      while len(study_planner[day]) >= 2:
        day = random.choice(days)

      study_planner[day][sub] = random.randint(1, 6)

     for i in days :
         if len(study_planner[i])<=1 :
              b=random.randint(1,6)
              avaiable=[sub for sub in subjects
                        if sub not in study_planner[i] ]
              c=random.choice(avaiable)
              study_planner[i][c]=b
     # for i in study_planner :
     #     a=random.randint(1,6)
     #     b=random.randint(1,6)
     #     c=random.sample(subjects,2)
     #     d={
     #          c[0]:a,
     #          c[1]:b
     #        }
     #     study_planner[i]=d
     return study_planner

 def score(work) :
     # subject repetation --> - 
# diff +more hours --> +
# included all subjects --> +
     #if both are diff score --> -
     #if one is diff and other is easy --> +
     #if time >6 --> -
     #not good enough
     score=100
     repeat=dict.fromkeys(subjects,0)
     for i in work :
          count=0
          a=list(work[i].keys())
          if len(a)<2 :
              score-=20
              continue
          else :
               repeat[a[0]]+=1
               repeat[a[1]]+=1
          if a[0]==a[1] :
               score-=15   #repetation in single day
          
          if a[0] in diff_3 :
               if a[1] in diff_3 :
                    score-=20
               elif a[1] in diff_2 :
                    if work[i][a[0]]>work[i][a[1]] :
                         score+=15
                    score+=10
               else :
                    score+=20
          b=list(work[i].values())
          # if sum(b) >6 :
          #      score -=20
          # elif sum(b)==6 :
          #      score+=10
          # else :
          #      score +=25
          if sum(b) > 6:
             score -= 35
          elif 4 <= sum(b) <= 6:
             score += 20
          else:
             score -= 10
          
          result=all(value>3 for value in work[i].values())
          

          if result :
               score-=20
     
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
          new_table=neigbhour(table,subjects)
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
 return best_schedule
#  print(best_schedule)
#  print("Best Score:", score(best_schedule))
 