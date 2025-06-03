from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Gemini model with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response (fix: prompt passed as string, not list)
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("models/gemini-pro")
    full_prompt = f"{prompt.strip()}\n\nQuestion: {question.strip()}"
    response = model.generate_content(full_prompt)
    return response.text.strip()

# Function to retrieve query results from SQLite database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# Define prompt as a single string (not a list)
prompt = """
You are an expert in converting English questions to SQL queries!
The SQL database has a table named STUDENT with the following columns: NAME, CLASS, SECTION, and MARKS.

Examples:
1. "How many entries of records are present?"
   -> SELECT COUNT(*) FROM STUDENT;

2. "Tell me all the students studying in Data Science class"
   -> SELECT * FROM STUDENT WHERE CLASS = "Data Science";

Make sure the response contains only the SQL query, without ``` or the word "sql".
"""

# Streamlit UI
st.set_page_config(page_title="SQL Query Generator with Gemini")
st.title("Gemini-Powered SQL Query Generator")
st.subheader("Ask any question about your STUDENT database")

# Input
question = st.text_input("Enter your question:", key="input")
submit = st.button("Submit")

# Handle submission
if submit and question:
    try:
        # Get SQL query from Gemini
        sql_query = get_gemini_response(question, prompt)
        st.markdown(f"**Generated SQL Query:** `{sql_query}`")

        # Run SQL query on SQLite DB
        results = read_sql_query(sql_query, "student.db")

        # Display results
        if results:
            st.subheader("Query Results:")
            for row in results:
                st.write(row)
        else:
            st.info("No results found for the query.")
    except Exception as e:
        st.error(f"Error: {e}")
