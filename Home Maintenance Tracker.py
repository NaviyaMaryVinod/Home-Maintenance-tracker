#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit


# In[2]:


pip install pandas


# In[9]:


import streamlit as st
import pandas as pd
import datetime

# Define file paths
tasks_file = 'C:\\Users\\naviy\\Downloads\\Tasks.csv'
contractors_file = 'C:\\Users\\naviy\\Downloads\\Contractors.csv'

# Load data
try:
    tasks = pd.read_csv(tasks_file)
except FileNotFoundError:
    tasks = pd.DataFrame(columns=["Task", "Date", "Contractor", "Notes", "Status"])

try:
    contractors = pd.read_csv(contractors_file)
    if contractors.empty:
        contractors = pd.DataFrame(columns=["Name", "Contact"])
except FileNotFoundError:
    contractors = pd.DataFrame(columns=["Name", "Contact"])

# Title and Sidebar
st.title("Home Maintenance Tracker")
st.sidebar.header("Add New Maintenance Task")

# Input fields for new tasks
task_name = st.sidebar.text_input("Task Name")
task_date = st.sidebar.date_input("Date", datetime.date.today())
task_contractor = st.sidebar.selectbox("Contractor", contractors['Name'].tolist())
task_notes = st.sidebar.text_area("Notes")

if st.sidebar.button("Add Task"):
    new_task = pd.DataFrame([[task_name, task_date, task_contractor, task_notes, "Upcoming"]],
                            columns=["Task", "Date", "Contractor", "Notes", "Status"])
    new_task.to_csv(tasks_file, mode='a', header=False, index=False)
    st.sidebar.success("Task added successfully!")

# Display tasks
st.subheader("Scheduled Maintenance Tasks")
tasks = pd.read_csv(tasks_file)
st.table(tasks[tasks['Status'] == 'Upcoming'])

# Display service history
st.subheader("Service History")
st.table(tasks[tasks['Status'] == 'Completed'])

# Contractor Management
st.sidebar.header("Manage Contractors")
contractor_name = st.sidebar.text_input("Contractor Name")
contractor_contact = st.sidebar.text_input("Contact Information")

if st.sidebar.button("Add Contractor"):
    new_contractor = pd.DataFrame([[contractor_name, contractor_contact]],
                                  columns=["Name", "Contact"])
    new_contractor.to_csv(contractors_file, mode='a', header=False, index=False)
    st.sidebar.success("Contractor added successfully!")

st.sidebar.subheader("Contractor List")
st.sidebar.table(contractors)

# Maintenance Tips and Guides
st.subheader("Maintenance Tips and Guides")
with open('C:\\Users\\naviy\\Downloads\\Maintenance_tips.md') as f:
    tips = f.read()
st.markdown(tips)


# In[10]:


streamlit run app.py


# In[ ]:




