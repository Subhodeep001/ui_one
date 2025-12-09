import streamlit as st
from datetime import date

st.set_page_config(page_title="Regulatory Intelligence Dashboard", layout="wide")

# ------------------- Sidebar -------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Home Dashboard",
    "Regulatory Insights",
    "Impact Analyzer",
    "Decision Intelligence",
    "Labeling Tracker",
    "Cross-Country Comparison",
    "AI Chat Interface"
])

st.sidebar.markdown("---")
st.sidebar.markdown("📅 " + str(date.today()))

# ------------------- Home Page -------------------
if page == "Home Dashboard":
    st.title("📊 Regulatory Intelligence Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Today's Insights")
        st.metric("New Updates", "12", "+4 from yesterday")
        st.button("View Details")

    with col2:
        st.subheader("High Risk Alerts")
        st.metric("Critical Alerts", "3", "-1 vs last week")
        st.button("View Alerts")

    with col3:
        st.subheader("Pending Actions")
        st.metric("Open Tasks", "8", "+2 pending")
        st.button("Open Tasks Board")

    st.markdown("---")

    st.subheader("Recent Regulatory Updates")
    sample_updates = [
        ("FDA", "Drug X Safety Alert", "High"),
        ("EMA", "Oncology guideline revision", "Medium"),
        ("CDSCO", "Labelling format update", "Low"),
    ]
    for agency, title, risk in sample_updates:
        st.write(f"**{agency}** — {title} — 🔥 Risk: `{risk}`")
        st.button(f"View Impact →", key=title)

# ------------------- Regulatory Insights -------------------
elif page == "Regulatory Insights":
    st.title("📄 Daily Regulatory Insights")
    st.text_input("Search updates...")
    st.date_input("Filter by date")
    st.selectbox("Region", ["All", "FDA", "EMA", "CDSCO", "MHRA", "TGA"])

    for i in range(1, 6):
        with st.expander(f"Update {i} Summary"):
            st.write("Automated summary of regulatory update...")
            st.button("Analyze Impact", key=f"impact_{i}")
            st.button("Open Full Document", key=f"doc_{i}")

# ------------------- Impact Analyzer -------------------
elif page == "Impact Analyzer":
    st.title("⚠ Impact & Risk Analyzer")

    st.write("Select an update to analyze:")
    st.selectbox("Choose Regulatory Update", [f"Update {i}" for i in range(1, 6)])

    st.subheader("Risk Score")
    st.progress(0.7)
    st.write("Impact: **High** on Product A")

    st.write("📩 Notify via:")
    colA, colB = st.columns(2)
    colA.button("Send Email Alert")
    colB.button("Push to Teams")

# ------------------- Decision Intelligence -------------------
elif page == "Decision Intelligence":
    st.title("🧠 AI Decision Intelligence")

    st.subheader("Recommended Action Items")
    st.write("System generated next steps for selected updates")

    actions = ["Review Change", "Assess Impact", "Update SOP", "Label Revision", "Close"]
    for act in actions:
        with st.expander(act):
            st.write("Auto suggested steps...")
            st.button("Assign Task", key=act)

# ------------------- Label Tracker -------------------
elif page == "Labeling Tracker":
    st.title("🏷 Label Change Tracker")

    st.dataframe({
        "Product": ["Drug A", "Drug B"],
        "Old Label": ["Text v1", "Text v3"],
        "New Label": ["Text v2", "Text v4"],
        "Status": ["Pending", "Completed"]
    })

    st.button("Upload Label Change Document")
    st.button("Generate Label Draft via GPT")

# ------------------- Cross-Country Comparison -------------------
elif page == "Cross-Country Comparison":
    st.title("🌍 Cross-Country Regulatory Comparison")

    st.table({
        "Feature/Rule": ["Label Format", "Safety Alert", "Guideline Revision"],
        "FDA": ["Updated", "Active", "2024"],
        "EMA": ["Pending", "Active", "2025"],
        "CDSCO": ["Active", "No Alert", "2023"],
    })

# ------------------- Chat Interface -------------------
elif page == "AI Chat Interface":
    st.title("💬 AI Regulatory Chat")
    user_query = st.text_input("Ask anything about regulatory data...")
    if st.button("Generate Response"):
        st.write("🤖 GPT Response: (mock text) This update may affect product X...")

