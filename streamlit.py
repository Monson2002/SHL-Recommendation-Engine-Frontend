import streamlit as st
import requests

# API_URL = "http://localhost:8000/recommend"
API_URL = "https://monson2002-shl-backend.hf.space/recommend"

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

st.title("🔍 SHL Assessment Recommendation Engine")

st.write("Enter a job description below:")

query = st.text_area("Your Query", height=150)

top_k = st.slider("Number of recommendations", min_value=5, max_value=10, value=10)

if st.button("Recommend Assessments"):
    if not query.strip():
        st.warning("Please enter a query")
    else:
        with st.spinner("Fetching recommendations..."):
            payload = {"query": query, "top_k": top_k}
            response = requests.post(API_URL, json=payload)

            if response.status_code != 200:
                st.error("Error from backend")
            else:
                data = response.json()
                results = data.get("recommended_assessments", [])

                st.subheader("Recommended SHL Tests")
                for r in results:
                    st.markdown(f"### ✅ {r['name']}")
                    st.markdown(f"[View Test]({r['url']})")
                    st.markdown("---")
