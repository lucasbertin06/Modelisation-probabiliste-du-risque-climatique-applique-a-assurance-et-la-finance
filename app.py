import os
import sys
import statistics

import streamlit as st
import plotly.graph_objects as go

# on connecte le dossier src/ (mêmes fichiers que le repo, inchangés)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from climat_risk import HAZARDS
from climatic_scenario import SCENARIOS, apply_scenario
from simulation import simulation
from insurance import VaR, expected_Shortfall, ruin_prob, recommended_capital

st.set_page_config(page_title="ClimateRiskSim", page_icon="🌊", layout="wide")

st.title("ClimateRiskSim")
st.caption("Simulation Monte-Carlo du risque climatique assurantiel — modèle de risque collectif (CRM)")

# ---------- sidebar : paramètres ----------
st.sidebar.header("Paramètres")

hazard_names = ["all"] + [h["name"] for h in HAZARDS]
hazard_name = st.sidebar.selectbox("Aléa climatique", hazard_names, index=0)

scenario_name = st.sidebar.selectbox("Scénario climatique", [s["name"] for s in SCENARIOS], index=0)

years = st.sidebar.slider("Années simulées", min_value=100, max_value=5000, value=1000, step=100)

capital = st.sidebar.number_input("Capital disponible (€)", min_value=0, value=100000, step=10000)

run_clicked = st.sidebar.button("Lancer la simulation", type="primary")
compare_clicked = st.sidebar.button("Comparer les 3 scénarios")


def choose_hazard(name):
    if name == "all":
        return HAZARDS
    for h in HAZARDS:
        if h["name"] == name:
            return [h]
    raise ValueError(f"Unknown hazard : {name}")


def choose_scenario(name):
    for s in SCENARIOS:
        if s["name"] == name:
            return s
    raise ValueError(f"Unknown scenario : {name}")


def run_model(hazard_name, scenario_name, years, capital):
    risks = choose_hazard(hazard_name)
    scenario = choose_scenario(scenario_name)
    adjusted_risks = [apply_scenario(r, scenario) for r in risks]  # applique le scénario à CHAQUE aléa sélectionné

    losses = simulation(adjusted_risks, years=years)

    return {
        "losses": losses,
        "avg": statistics.mean(losses),
        "variance": statistics.variance(losses),
        "var99": VaR(losses, 0.99),
        "es99": expected_Shortfall(losses, 0.99),
        "ruin": ruin_prob(losses, capital),
        "cap_reco": recommended_capital(losses, 0.99),
    }


def eur(x):
    return f"{x:,.0f} €".replace(",", " ")


def render_histogram(losses, capital, var99):
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=losses,
        nbinsx=40,
        marker=dict(color="rgba(79,182,166,0.75)"),
        name="Pertes simulées",
    ))
    fig.add_vline(x=capital, line_dash="dash", line_color="#eef2f5",
                  annotation_text="Capital", annotation_position="top")
    fig.add_vline(x=var99, line_dash="dot", line_color="#8b98a8",
                  annotation_text="VaR 99%", annotation_position="bottom")
    fig.update_layout(
        template="plotly_dark",
        height=380,
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis_title="Perte annuelle (€)",
        yaxis_title="Nombre d'années simulées",
    )
    st.plotly_chart(fig, use_container_width=True)


def render_result(res, capital):
    st.metric("Probabilité de ruine", f"{res['ruin']*100:.2f} %",
              delta=None, delta_color="off")

    render_histogram(res["losses"], capital, res["var99"])

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Perte moyenne", eur(res["avg"]))
    c2.metric("Variance", eur(res["variance"]))
    c3.metric("VaR 99%", eur(res["var99"]))
    c4.metric("Expected Shortfall", eur(res["es99"]))
    c5.metric("Capital recommandé", eur(res["cap_reco"]))


# ---------- run ----------
if compare_clicked:
    st.subheader(f"Comparaison des scénarios — aléa : {hazard_name}")
    rows = []
    for s in SCENARIOS:
        res = run_model(hazard_name, s["name"], years, capital)
        rows.append({
            "Scénario": s["name"],
            "Perte moyenne": eur(res["avg"]),
            "VaR 99%": eur(res["var99"]),
            "Expected Shortfall": eur(res["es99"]),
            "Probabilité de ruine": f"{res['ruin']*100:.2f} %",
            "Capital recommandé": eur(res["cap_reco"]),
        })
    st.table(rows)
else:
    res = run_model(hazard_name, scenario_name, years, capital)
    render_result(res, capital)

st.caption(
    "Modèle : fréquence des sinistres ~ Poisson(λ), coût unitaire ~ log-normale(μ,σ). "
    "Résultats issus de src/*.py, exécutés directement — projet fictif à but pédagogique."
)