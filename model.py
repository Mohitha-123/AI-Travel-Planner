import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

#Title and Icon
st.set_page_config(page_title="Ticket Price Estimator 🎟️")

# App Title & Subtitle
st.title("🚆✈️🚌 AI Travel Planner!!")
st.subheader("🔍 Calculate an idea of the cost of traveling for your visit!!")

# User Inputs
source = st.text_input("📍 Source:", placeholder="Enter your departure city")
destination = st.text_input("📍 Destination:", placeholder="Enter your arrival city")
mode = st.selectbox("🚗 Select Mode of Transport:", ["Train", "Flight", "Bus"])
date = st.date_input("📅 Select Your Travel Date:")

# OpenAI API Key
api_key = "AIzaSyBItvysBggCo5T2iE61M209b24e36FmiBo"

# Prompt Template
prompt = ChatPromptTemplate(messages=[
    ('system', "You are an AI assistant for estimating average ticket prices and trip planning."),
    ('human', """Provide an estimated cost breakdown for all travel classes from {source} to {destination} via {mode} on {date}. 
    Format the response as:
    - 💺 [Class Name]: ₹[Price]
    - ...
    ✨ Estimated overall average cost: ₹[Total Average]

    Additionally, summarize a brief **trip plan** (max 300 words), including travel duration, best travel tips, and recommendations.""")
])

# Language Model & Output Parser
chat_model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.0-flash-exp")
output_parser = StrOutputParser()

# Button to Get Estimation
if st.button("🎯 Estimate Ticket Price"):
    if source and destination and mode:
        user_input = {"source": source, "destination": destination, "mode": mode, "date": str(date)}
        result = (prompt | chat_model | output_parser).invoke(user_input)
        st.success("📢 Here’s your estimated travel cost and plan:")
        st.write(result)
    else:
        st.warning("⚠️ Please enter all details to get an accurate estimate!")

# Footer
st.markdown("---")
st.caption("💡 *Powered by AI | Estimated prices may vary*")

