import streamlit as st
import mysql.connector
import pandas as pd  
st.set_page_config(page_title="Employee Management System",page_icon="https://www.pngitem.com/pimgs/m/523-5233379_employee-management-system-logo-hd-png-download.png")
st.title("Employee Management System")
choice=st.sidebar.selectbox("choose one",["details", "projects", "user_auth", "employee_departments"])
if choice=="details":
    st.write("Manage employee data, projects, and departments efficiently in one place.")
    st.markdown("<iframe src='https://lnu.diva-portal.org/smash/get/diva2:204828/FULLTEXT01.pdf' width='100%' height='500px'</iframe>",unsafe_allow_html=True)
elif choice=="projects":
    st.image("https://png.pngtree.com/png-clipart/20230824/original/pngtree-quarantine-office-people-employee-manager-picture-image_8420225.png")
    mydb = mysql.connector.connect(host="localhost", user="root", password="Imthi$123", database="employee")
    q2 = "SELECT * FROM projects"
    df_projects = pd.read_sql(q2, mydb)
    st.dataframe(df_projects)
elif choice=="user_auth":
    login=False
    us_id=st.text_input("Enter username")
    pw_id=st.text_input("Enter pass")
    mydb=mysql.connector.connect(host="localhost",user="root",password="Imthi$123",database="employee")
    c=mydb.cursor()
    c.execute("select * from user_auth")
    rows = c.fetchall()  
    for r in rows:
        if(r[0]==us_id and r[1]==pw_id):
           login=True
           st.markdown("<h4 style='color: green;'>Login Success </h4>", unsafe_allow_html=True)
           q1 = "select * from leaves where emp_id = %s"
           df = pd.read_sql(q1, mydb, params=(us_id,))
           st.subheader("Your Leave Records")
           st.dataframe(df)
           break
    if not us_id or not pw_id:
        st.write("Please enter both username and password.")
    elif not login:
        st.markdown("<h4 style='color: red;'>Login Failed </h4>", unsafe_allow_html=True)
elif choice=="employee_departments":
    st.video("https://www.youtube.com/watch?v=wO0g7RIhQMA")
