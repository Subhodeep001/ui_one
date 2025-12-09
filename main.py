import streamlit as st
from datetime import date

st.set_page_config(page_title="Regulatory Update Dashboard", layout="wide")

st.title("📊 Regulatory Updates & Impact Center")
st.caption("Single-screen oversight of regulatory changes, impacts & action categories.")
st.markdown(f"📅 **{date.today()}**")
st.markdown("---")

# ===== SUMMARY CARDS =====
col1, col2, col3 = st.columns(3)
col1.metric("New Updates Today", "9")
col2.metric("High Impact", "3")
col3.metric("Require Action", "6")

st.markdown("---")

# Filters
st.subheader("🔍 Filter Updates")
f1, f2, f3 = st.columns(3)
f1.multiselect("Region", ["FDA","EMA","CDSCO","MHRA","TGA"], default=["FDA","EMA"])
f2.multiselect("Impact Level", ["High","Medium","Low"])
f3.multiselect("Category", ["Label Change","SOP Change","Safety Alert","Packaging","CMC","Risk"])

st.markdown("---")

# ===== UPDATES LIST WITH IMPACT + CATEGORY =====
st.subheader("📄 Recent Regulatory Updates")

updates = [
    {"id":1,"title":"FDA warning insertion required","impact":"High","category":"Label Change"},
    {"id":2,"title":"EMA guideline update on storage","impact":"Medium","category":"SOP Change"},
    {"id":3,"title":"CDSCO packaging note revised","impact":"Low","category":"Packaging"},
    {"id":4,"title":"EMA oncology labeling modification","impact":"High","category":"Label Change"},
]

for u in updates:
    with st.container():
        st.markdown(f"### {u['title']}")
        st.write(f"📍 **Category:** `{u['category']}`")
        st.write(f"🔥 **Impact Level:** **{u['impact']}**")

        colA, colB, colC = st.columns([1,1,2])
        colA.button("View Summary", key=f"summary_{u['id']}")
        colB.button("View Impact Details", key=f"impact_{u['id']}")
        colC.button("Generate Action Item", key=f"action_{u['id']}")

        st.markdown("---")

# ===== ACTION WORKFLOW =====
st.subheader("🧠 Action Items for Updates")
st.write("Generated only when update requires work")

st.table({
    "Update": ["FDA warning insertion", "EMA oncology labeling"],
    "Category": ["Label Change","Label Change"],
    "Impact": ["High","High"],
    "Action Status": ["Pending","Assigned"]
})

st.markdown("---")

# ===== OPTIONAL AI CHAT =====
st.subheader("💬 Ask AI about any update")
q = st.text_input("e.g. 'Show all high impact label changes this week'")
if st.button("Ask"):
    st.write("🤖 *AI Response Placeholder*")

