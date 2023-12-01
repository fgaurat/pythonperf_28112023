import streamlit as st

def main():
    st.title('Python Streamlit')
    name = st.text_input('Name', '')
    if st.button('Say hello') and name:
        st.write('Hello', name)

if __name__=='__main__':
    main()
