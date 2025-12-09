import streamlit as st
from datetime import date

st.set_page_config(page_title="Unified Regulatory Dashboard", layout="wide")

st.title("📊 Unified Regulatory Intelligence Dashboard")
st.caption("All insights, impacts, actions, label tracking, comparisons & chat — in one place.")
st.markdown(f"📅 **{date.today()}**")
st.markdown("---")

# ======= TOP METRICS =======
c1, c2, c3, c4 = st.columns(4)
c1.metric("New Updates Today", "14")
c2.metric("High-Risk Alerts", "3")
c3.metric("Pending Actions", "10")
c4.metric("Labels Requiring Update", "2")

st.markdown("---")

# ======= DAILY INSIGHTS =======
st.subheader("📄 Daily Regulatory Insights (Auto Summarized)")
for i in range(1, 4):
    with st.expander(f"Update {i}: Example Regulatory Change Summary"):
        st.write("AI-generated concise summary of regulatory update …")
        st.write("Agency: FDA | Region: USA | Category: Labeling | Severity: High")

        if st.button(f"Analyze Impact on Products #{i}"):
            st.session_state[f"impact_show_{i}"] = True
        if st.session_state.get(f"impact_show_{i}", False):
            st.success("Product A — High Risk | Product C — Medium Risk")
            st.button("Push Alert to Teams")
            st.button("Send Email to Product Owner")

st.markdown("---")

# ======= DECISION & ACTION SYSTEM =======
st.subheader("🧠 Decision Intelligence (Auto Action Recommendations)")

actions = [
    "Review change with RA team",
    "Initiate label revision",
    "Assess manufacturing documentation",
    "Update internal SOP",
]

for act in actions:
    st.checkbox(f"✔ {act}", value=False)

st.button("Convert Actions to Tasks & Assign Owners")

st.markdown("---")

# ======= LABEL CHANGE TRACKER =======
st.subheader("🏷 Labeling Updates Automatically Mapped")

st.table({
    "Product": ["Drug X", "Drug Y"],
    "Current Label Version": ["v1.2", "v3.4"],
    "Required Update": ["Yes", "In Review"],
    "Status": ["Pending", "Under Evaluation"]
})

st.button("Auto-Generate New Label Draft (GPT)")

st.markdown("---")

# ======= COUNTRY COMPARISON TABLE =======
st.subheader("🌍 Cross-Country Rule Comparison (Auto-Sync)")

st.dataframe({
    "Rule": ["Label Format Update", "Safety Alert", "Packaging Warning"],
    "FDA": ["Active", "High", "Pending"],
    "EMA": ["Active", "Active", "Active"],
    "CDSCO": ["Pending", "No Alert", "Active"]
})

st.markdown("---")

# ======= AI CHAT INTERFACE =======
st.subheader("💬 Chat with Your Regulatory Data")

query = st.text_input("Ask about regulations, impacts, products, timelines...")
if st.button("Ask AI"):
    st.write("🤖 *Mock Response:* This regulation affects Drug X in US & EU. Risk: High.")

st.markdown("---")

# ======= FOOTER ANALYTICS =======
st.caption("Powered by Automated Compliance Scanning + LLM Regulatory Intelligence Layer")
