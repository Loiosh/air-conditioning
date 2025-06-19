import streamlit as st

st.title("Is the air conditioning working?")
st.markdown(
    """ 
    ## NO 
    """
)

if st.button("Send help!"):
    st.balloons()