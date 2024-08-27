# import streamlit as st
# from agents import run_crew  # Import the function from agents.py
# from langchain_groq import ChatGroq  # Import ChatGroq for the chatbot
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Set the API key as an environment variable
# api_key = "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"

# # Initialize the chatbot model
# chatbot_model = ChatGroq(model='llama3-8b-8192', api_key=api_key)

# st.title("Multi-Agent System Integration")

# # Existing code for agent selection and input
# agent_option = st.selectbox(
#     "Select an Agent",
#     ["Research Agent", "Customer Support Agent"]
# )

# if agent_option == "Research Agent":
#     topic = st.text_input("Enter the topic for the research:")
# elif agent_option == "Customer Support Agent":
#     task_options = [
#         "Inquiry Resolution",
#         "Quality Assurance Review"
#     ]
#     selected_task = st.selectbox("Select Task", task_options)

# # Generate content button
# if st.button("Generate Content"):
#     if agent_option == "Research Agent":
#         if topic:
#             with st.spinner("Generating content..."):
#                 result = run_crew(agent_option, None, topic)
#                 st.markdown(result)
#         else:
#             st.error("Please enter a topic.")

# # Chatbot section
# st.header("Clarification Chatbot")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # React to user input
# if prompt := st.chat_input("Ask a question about the generated content:"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     # Generate response
#     try:
#         with st.spinner("Thinking..."):
#             response = chatbot_model.invoke(prompt).content
        
#         # Display assistant response in chat message container
#         with st.chat_message("assistant"):
#             st.markdown(response)
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": response})
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")



import streamlit as st
from agents import run_crew  # Import the function from agents.py
from langchain_groq import ChatGroq  # Import ChatGroq for the chatbot
import os
from dotenv import load_dotenv

load_dotenv()

# Set the API key as an environment variable
api_key = "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"

# Initialize the chatbot model
chatbot_model = ChatGroq(model='llama3-8b-8192', api_key=api_key)

st.title("Multi-Agent System Integration")

# Agent selection
agent_option = st.selectbox(
    "Select an Agent",
    ["Research Agent", "Resume Agent"]
)

if agent_option == "Research Agent":
    topic = st.text_input("Enter the topic for the research:")
elif agent_option == "Resume Agent":
    task_options = [
        "Research",
        "Profile",
        "Resume Strategy",
        "Interview Prep"
    ]
    selected_task = st.selectbox("Select Task", task_options)

    if selected_task == "Research":
        job_posting_url = st.text_input("Enter the job posting URL:")
    elif selected_task == "Profile":
        github_url = st.text_input("Enter the GitHub URL:")
        personal_writeup = st.text_input("Enter the personal write-up:")
    elif selected_task == "Resume Strategy":
        st.text("Click Generate Content to tailor the resume based on profile and job requirements.")
    elif selected_task == "Interview Prep":
        st.text("Click Generate Content to prepare interview questions and talking points.")

# Generate content button
if st.button("Generate Content"):
    if agent_option == "Research Agent":
        if topic:
            with st.spinner("Generating content..."):
                result = run_crew(agent_option, None, topic)
                st.markdown(result)
        else:
            st.error("Please enter a topic.")
    elif agent_option == "Resume Agent":
        if selected_task == "Research" and job_posting_url:
            with st.spinner("Generating job analysis..."):
                result = run_crew(agent_option, "Research", job_posting_url)
                st.markdown(result)
        elif selected_task == "Profile" and github_url and personal_writeup:
            with st.spinner("Generating profile..."):
                result = run_crew(agent_option, "Profile", {"github_url": github_url, "personal_writeup": personal_writeup})
                st.markdown(result)
        elif selected_task == "Resume Strategy":
            with st.spinner("Tailoring resume..."):
                result = run_crew(agent_option, "Resume Strategy", None)
                st.markdown(result)
        elif selected_task == "Interview Prep":
            with st.spinner("Preparing interview questions..."):
                result = run_crew(agent_option, "Interview Prep", None)
                st.markdown(result)
        else:
            st.error("Please provide the necessary inputs.")

# Chatbot section
st.header("Clarification Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question about the generated content:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response with the ChatGroq model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chatbot_model(prompt)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
