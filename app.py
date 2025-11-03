# Ray Companion — Chicago Beta (v0.1 Foundation)
# © 2025 Brian James Chapman • MIT
import streamlit as st
import pandas as pd
import json

from modules.insights import atypical
from modules.analytics import quick_roi_estimate, mock_table

st.set_page_config(page_title="Ray Companion — v0.1", page_icon="📎", layout="centered")

if "insights" not in st.session_state:
    st.session_state["insights"] = []

tabs = st.tabs(["Ray Console", "Analytics", "Insights", "Settings"])

# ---------- Ray Console ----------
with tabs[0]:
    st.header("👋 Ray Console")
    st.caption("Chromebook-first foundation. Minimal now, scalable later.")
    st.write("Here are a couple of starter listings (replace with feeds later):")
    df = mock_table()
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.subheader("Ask Ray (concept handoff)")
    st.caption("Copy the summary below into ChatGPT if you want richer language today.")
    st.text_area("Prompt", value="You are Ray, a concise, ethical Chicago real-estate assistant. Summarize the two listings and recommend one action today.", height=120)

# ---------- Analytics ----------
with tabs[1]:
    st.header("📈 Quick ROI (placeholder)")
    c1,c2 = st.columns(2)
    with c1:
        purchase = st.number_input("Purchase ($)", min_value=10000, value=310000, step=5000)
        rehab    = st.number_input("Rehab ($)", min_value=0, value=50000, step=1000)
        carry    = st.number_input("Carrying cost ($)", min_value=0, value=8000, step=500)
    with c2:
        arv      = st.number_input("After-Repair Value ($)", min_value=10000, value=410000, step=5000)
        sell_pct = st.number_input("Selling cost (%)", min_value=0.00, max_value=0.12, value=0.05, step=0.005, format="%.3f")

    if st.button("Estimate ROI"):
        est = quick_roi_estimate(purchase, rehab, arv, carry, sell_pct)
        st.success(f"Estimated ROI: {est['roi_pct']}%")
        st.caption("This is a simple estimator. The full Monte Carlo engine will plug in here in v1.0.")

# ---------- Insights ----------
with tabs[2]:
    st.header("🧩 Atypical Insight")
    depth = st.slider("Insight depth", 1, 3, 2)
    ethical = st.toggle("Blend Jesuit/ethical reflection", value=True)
    context = st.text_input("Optional context", value="Novice Chicago agent; flip intent")
    if st.button("Refresh Insight"):
        ins = atypical(depth=depth, ethical=ethical, context=context)
        st.session_state["insights"] = [ins] + st.session_state["insights"][:4]
    if st.session_state["insights"]:
        top = st.session_state["insights"][0]
        st.success(top["text"])
        st.caption(f"{top['meta']} • {top['generated_at']}")
        with st.expander("History"):
            for i in st.session_state["insights"]:
                st.write(f"- {i['generated_at']}: {i['text']} — _{i['meta']}_")
    else:
        st.info("Click Refresh Insight to generate a perspective.")

# ---------- Settings ----------
with tabs[3]:
    st.header("⚙️ Settings")
    st.write("This is the minimal foundation. You can:")
    st.markdown("- Deploy to Streamlit Cloud")
    st.markdown("- Add market feeds later")
    st.markdown("- Plug in the full Monte Carlo + headwinds modules when ready")
    st.markdown("- Package as a PWA with the provided wrapper")

    st.subheader("Region data (preview)")
    raw = json.load(open('data/chicago_regions.json'))
    st.json(raw)
