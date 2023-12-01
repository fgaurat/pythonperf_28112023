import streamlit as st
from UserDAO import UserDAO

dao = UserDAO('users_db.db')
users = dao.findAll()


st.title('DAO Users')
st.table(users)

