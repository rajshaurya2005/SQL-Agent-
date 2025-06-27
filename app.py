import streamlit as st
from agent import invoke_agent

st.set_page_config(page_title="MySQL LLM Agent", page_icon="🧠")

st.title("🧠 MySQL Database Assistant")

query = st.text_area("Enter your question about the database:")

if st.button("Run Query"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing..."):
            result = invoke_agent(query)
        st.success("Done!")
        st.subheader("Result:")
        st.json(result)
