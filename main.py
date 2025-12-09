import streamlit as st
from datetime import date

st.set_page_config(page_title="Regulatory Intelligence Dashboard", layout="wide")

# ---------------- HEADER ----------------
st.title("📊 Unified Regulatory Intelligence Dashboard")
st.caption(f"Live Regulatory Monitoring | {date.today()}")

st.markdown("---")

# ---------------- TOP SUMMARY OVERVIEW ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("New Regulatory Updates", "12", "+4")
col2.metric("High Risk Alerts", "3", "⚠")
col3.metric("Pending Action Items", "8", "+2")
col4.metric("Label Updates in Review", "4", "📝")

st.markdown("---")

# ---------------- SEARCH & FILTERS ----------------
st.subheader("🔍 Explore Regulatory Data")
search = st.text_input("Search regulations, country, product, guideline...")
colA, colB, colC = st.columns(3)
with colA: st.selectbox("Country/Authority", ["All", "FDA", "EMA", "CDSCO", "MHRA", "PMDA", "TGA"])
with colB: st.selectbox("Risk Level", ["All", "High", "Medium", "Low"])
with colC: st.date_input("Filter by Date")

st.markdown("---")

# ---------------- FULL COMBINED FEATURE SECTION ----------------

with st.expander("📄 Daily Regulatory Insights (Auto Summarized)", expanded=True):
    for i in range(1, 4):
        st.write(f"**Update {i}:** Regulatory summary generated from document...")
        st.text("AI Extracted compliance points, affected categories, key takeaways...")
        c1, c2, c3 = st.columns([1,1,2])
        c1.button("Analyze Impact", key=f"impact_{i}")
        c2.button("Full Summary", key=f"summary_{i}")
        c3.button("View Original PDF", key=f"pdf_{i}")
        st.markdown("---")

# ---------------- IMPACT + RISK + ACTION ENGINE ----------------
with st.expander("⚠ Regulatory Impact + Risk Analyzer + Action Engine", expanded=True):

    st.subheader("Risk Assessment & Compliance Impact")
    st.progress(0.75)
    st.write("Impact Level: **High** on Product A | Compliance Action Required")

    colX, colY = st.columns(2)

    with colX:
        st.write("🧪 **Products affected**: Drug A, Drug C")
        st.write("📌 Impact area: Labeling, Safety Update Required")
        st.button("Send teams alert")
        st.button("Email stakeholders")

    with colY:
        st.write("🧠 **AI Suggested Actions**:")
        st.checkbox("Review update internally")
        st.checkbox("Update label section 4.3")
        st.checkbox("Initiate safety board review")
        st.button("Assign Task + Create Ticket")

# ---------------- LABEL TRACKING ----------------
with st.expander("🏷 Label Change Tracker"):

    st.dataframe({
        "Product": ["Drug A", "Drug B", "Drug C"],
        "Current Version": ["v3.1","v1.4","v2.0"],
        "Proposed Change": ["Safety text mod","Format update","Dosage clarif."],
        "Status": ["Pending review","Completed","In drafting"]
    })

    st.button("Upload label document")
    st.button("Generate GPT draft from changes")

# ---------------- COMPARISON ENGINE ----------------
with st.expander("🌍 Cross-Country Regulatory Comparison"):

    st.table({
        "Feature/Rule":["Label Format","Safety Alert","Guideline Revision"],
        "FDA":["Updated","Active","2024"],
        "EMA":["Pending","Active","2025"],
        "CDSCO":["Active","None","2023"]
    })

    st.button("Export comparison report")

# ---------------- AI CHAT (Integrated live panel) ----------------
st.markdown("---")
st.subheader("💬 Ask the Regulatory AI Assistant")

query = st.text_input("Ask anything... (e.g. Show high risk EMA changes for oncology)")
if st.button("Generate Response"):
    st.write("🤖 *Mock Response:* Based on last 7 days, EMA has 2 major oncology updates affecting Drug A and B with high risk...")

