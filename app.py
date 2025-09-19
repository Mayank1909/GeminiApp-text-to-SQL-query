from dotenv import load_dotenv
load_dotenv() # load all env var


import streamlit as st
import os
import sqlite3 

import google.generativeai as genai


#configure 
genai.configure(api_key=os.getenv("API_KEY"))


#function to load gemini model and provide sql query as response 

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response=model.generate_content([prompt[0],question])

    return response.text

# function to retreive the query from sql db 

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows


#define your prompt

prompt=["""
    You are an expert in converting English question in SQL query! 
        The SQL database has the name Student and has the following 
        columns-  Name , Class, Section, and Marks \n\n
        For example: Example1: How many recors are present in the table student
        the sql command will be something like this SELECT COUNT(*) FROM STUDENT;
        Example 2: Tell me all the students student sstudying Data science?,
        the sql command will be : Slect * from STUDENT where class="Data Science"
        , also the sql code should not have ''' in the begining or end  and ghe sql word in the output.
"""]

## strealit app

st.set_page_config(page_title="I can retrive any SQL query ")
st.header("Gemini App to retrive SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question ")



# if  submit is clicked 

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The response is : ")
    for row in data:
        print(row)
        st.header(row)





