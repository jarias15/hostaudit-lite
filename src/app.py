import streamlit as st
import json
import os

st.title("HostAudit Lite Dashboard")
st.subheader("Automated Linux CIS Compliance Auditor")

if os.path.exists("results.json"):
    with open("results.json", "r") as f:
        data = json.load(f)

    st.metric(label="Passed Checks", value=data["summary"]["passed"])
    st.write("### Detailed Findings")
    st.json(data["findings"])
else:
    st.warning("results.json not found. Run python3 src/auditor.py first.")
