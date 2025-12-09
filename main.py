import streamlit as st

st.set_page_config(page_title="Regulatory Intelligence Platform", layout="wide")

st.title("📊 Regulatory Intelligence Platform – UI Mock")
st.markdown("A concept UI for Compliance Monitoring, Insights & Decision Intelligence System")

tabs = st.tabs([
    "Compliance Tracker", 
    "Regulatory Insights", 
    "Impact Analyzer", 
    "Decision Intelligence", 
    "Chat Interface"
])


# --------------------------------------------
# 1. Compliance Tracker
# --------------------------------------------
with tabs[0]:
    st.header("🕒 Compliance Tracker")
    st.subheader("Monitor regulatory updates across global agencies")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Features")
        st.markdown("""
        - Monitor **12 regulatory websites** daily  
        - **AI/NLP extraction** of pharma regulations  
        - Store using **defined schema**  
        - Auto dump updates into **central DB**  
        """)

    with col2:
        st.markdown("### Data Status")
        st.metric("Sources Connected", "12")
        st.metric("Latest Crawl", "Running...")
        st.progress(60)

    st.info("⏳ Timeline Target: **15th Dec**")

    st.markdown("---")
    st.markdown("#### Sample Regulatory Feeds (Mock)")
    st.table({
        "Date": ["2025-12-09", "2025-12-08", "2025-12-08"],
        "Agency": ["FDA", "EMA", "MHRA"],
        "Update Type": ["Safety Alert", "Labeling Guideline", "Drug Approval"],
        "Status": ["Extracted", "Extracted", "Pending Summary"]
    })


# --------------------------------------------
# 2. Regulatory Insights
# --------------------------------------------
with tabs[1]:
    st.header("🧠 Regulatory Insights")
    st.subheader("Automated daily summaries & insights layer")

    st.markdown("""
    - Daily **summary generation**  
    - **Automated compliance insights**  
    - Cross-country **regulatory comparison dashboards**  
    - Add **GPT plug-in for reasoning & Q/A**  
    """)

    st.info("🎯 Timeline: **31st Dec**")

    st.markdown("---")
    st.text_area("Paste new regulatory update text for sample summarization")
    if st.button("Generate Insight Summary (Mock)"):
        st.success("Summary generated ➝ (Demo Output)")
        st.write("> *AI summary of regulatory update will appear here*")


# --------------------------------------------
# 3. Impact Analyzer
# --------------------------------------------
with tabs[2]:
    st.header("⚠️ Impact Analyzer")
    st.subheader("Evaluate regulatory changes & business impact")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - Teams & Email Integration  
        - Regulatory Impact & **Risk scoring**  
        - Change propagation tracking  
        """)

    with col2:
        st.slider("Risk Threshold", 0, 100, 60)
        if st.button("Run Impact Scoring (Mock)"):
            st.success("Impact Score Generated: High Risk 🟥")

    st.info("📅 Timeline: **15th Jan**")


# --------------------------------------------
# 4. Decision Intelligence
# --------------------------------------------
with tabs[3]:
    st.header("🧩 Decision Intelligence Engine")
    st.subheader("Automated actionable decision support")

    st.markdown("""
    - Auto prompt **action items** from regulatory change  
    - Create **Action Bucket List**  
    - Track **labeling updates** & required actions  
    """)

    st.text_input("Add new action rule (Mock)")
    st.button("Save Rule")

    st.markdown("### Action Item Buckets")
    st.table({
        "Bucket": ["Urgent", "Moderate", "Low"],
        "Examples": ["Label change", "Internal review", "FYI only"]
    })

    st.info("⏳ Timeline Target: **30th Jan**")


# --------------------------------------------
# 5. Chat Interface
# --------------------------------------------
with tabs[4]:
    st.header("💬 Regulatory Chat Interface")
    st.subheader("Query historic updates & decisions using conversational layer")

    query = st.text_input("Ask something (e.g. Show EMA safety updates from last week)")
    if st.button("Search (Mock)"):
        st.write("🟢 *Response from regulatory DB will appear here*")

    st.info("📌 Timeline: **15th Feb**")
