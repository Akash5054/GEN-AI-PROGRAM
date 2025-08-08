import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
import streamlit as st

#chatbox model
from langchain_google_genai import ChatGoogleGenerativeAI

#build the large language model (llm)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# query = input("ask anything..")
# res=llm.invoke(query)
# print(res.content)

st.title("Simple Chat Box")
st.header("Simple Chat Box")

user_input=st.text_input("Type something")
if user_input:
    res=llm.invoke(user_input)
    st.write(res.content)
    