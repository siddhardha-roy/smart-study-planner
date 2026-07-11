import streamlit as st
import math
import k_means
import hill_climbing
import pandas as pd
done=False
st.title("📚Welcome to Smart study planner ")
if "subjects" not in st.session_state :
    st.session_state.subjects=[]

with st.form("subjects_form") :
   subject=st.text_input("enter the subjects seperated by commas...\n(not more than 6) ")
  
   subtimitted=st.form_submit_button("Generate")

if subtimitted :
   st.session_state.subjects=[  s.strip() for s in subject.split(",")]

  #  for i in st.session_state.subjects :
  #      st.write(i)
# if subtimitted :
#     dic_1=dict.fromkeys(st.session_state.subjects)
#     st.write(dic_1)

if st.session_state.subjects :
   with st.form("append") :
      difficulty=[]
      time=[]
      for i in st.session_state.subjects :
       
       st.header(f"for the subject {i}")
       level=st.radio(f"diffculty level for {i}",("1","2","3"),key=f"diff_{i}")
       study_time=st.number_input("Enter time to learn the basics of the subject[not for the time table,generally](hours)", 1, 24, 2,key=f"time_{i}")
       difficulty.append(level)
       time.append(study_time)

      done=st.form_submit_button("submit")

if done :
   dic_1={}
   for i,k,j in zip(st.session_state.subjects,difficulty,time) :
      dic_1[i]=(int(k),float(j))
   # st.write(dic_1)
# -->2
# kmean-->subjects,dic_1(needed)
# return we will get sorted levels of subjects 
   diff_1=[]
   diff_2=[]
   diff_3=[]
   diff_1,diff_2,diff_3=k_means.k_mean(st.session_state.subjects,dic_1)
   final_time_table=hill_climbing.final(st.session_state.subjects,diff_1,diff_2,diff_3)
   # st.write(final_time_table)
   df=pd.DataFrame(final_time_table).T
   st.subheader("🧬generated time table : :-")
   st.dataframe(df)

 

     