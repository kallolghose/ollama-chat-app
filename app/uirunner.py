import streamlit as st

def main():
    st.title("Test Data Ginnie")
    st.caption("Select an Open API Specification")
    uploaded_file = st.file_uploader("Choose a file", type=["json", "yaml", "yml"])
    if uploaded_file is not None:
        st.success("Upload Successful !!")


if __name__=="__main__":
    main()
