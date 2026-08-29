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

# ---------- esthétique : palette storm / teal / amber, Fraunces + IBM Plex Mono ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500&family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');

:root{
    --bg-void:#0c1218;
    --bg-panel:#141b23;
    --bg-panel-2:#1a232d;
    --line:#25313d;
    --text-primary:#eef2f5;
    --text-muted:#8b98a8;
    --text-dim:#5c6a7a;
    --safe:#4fb6a6;
    --danger:#e2703a;
    --danger-bright:#ef8a58;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
    color:var(--text-primary);
}

.stApp{
    background:var(--bg-void);
    background-image:
        radial-gradient(ellipse 900px 500px at 15% -10%, rgba(79,182,166,0.08), transparent 60%),
        radial-gradient(ellipse 700px 500px at 100% 10%, rgba(226,112,58,0.07), transparent 60%);
}

/* titre */
h1{
    font-family:'Fraunces', serif !important;
    font-weight:500 !important;
    letter-spacing:-0.01em;
    color:var(--text-primary) !important;
}
.stCaption, [data-testid="stCaptionContainer"]{
    font-family:'IBM Plex Mono', monospace !important;
    color:var(--safe) !important;
    font-size:12.5px !important;
    letter-spacing:0.04em;
}

/* sidebar */
[data-testid="stSidebar"]{
    background:var(--bg-panel) !important;
    border-right:1px solid var(--line);
}
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] label{
    font-family:'IBM Plex Mono', monospace !important;
    color:var(--text-muted) !important;
    text-transform:uppercase;
    font-size:11.5px !important;
    letter-spacing:0.06em;
}

/* inputs */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div,
[data-testid="stSidebar"] input{
    background:var(--bg-panel-2) !important;
    border:1px solid var(--line) !important;
    color:var(--text-primary) !important;
    font-family:'IBM Plex Mono', monospace !important;
}
[data-testid="stSidebar"] .stSlider [data-baseweb="slider"] > div > div{
    background:var(--safe) !important;
}

/* boutons */
[data-testid="stSidebar"] button{
    font-family:'IBM Plex Mono', monospace !important;
    font-size:12.5px !important;
    text-transform:uppercase;
    letter-spacing:0.03em;
    border-radius:7px !important;
}
[data-testid="stSidebar"] button[kind="primary"]{
    background:var(--safe) !important;
    color:#08221d !important;
    border:none !important;
    font-weight:600 !important;
}
[data-testid="stSidebar"] button[kind="secondary"]{
    background:transparent !important;
    color:var(--text-muted) !important;
    border:1px solid var(--line) !important;
}
[data-testid="stSidebar"] button[kind="secondary"]:hover{
    border-color:var(--danger) !important;
    color:var(--danger-bright) !important;
}

/* metric cards */
[data-testid="stMetric"]{
    background:var(--bg-panel);
    border:1px solid var(--line);
    border-radius:10px;
    padding:16px 18px;
}
[data-testid="stMetricLabel"]{
    font-family:'IBM Plex Mono', monospace !important;
    text-transform:uppercase;
    font-size:10.5px !important;
    letter-spacing:0.07em;
    color:var(--text-dim) !important;
}
[data-testid="stMetricValue"]{
    font-family:'IBM Plex Mono', monospace !important;
    color:var(--text-primary) !important;
}

/* le tout premier metric (probabilité de ruine) en hero */
[data-testid="column"]:first-of-type [data-testid="stMetricValue"]{
    font-family:'Fraunces', serif !important;
    font-size:52px !important;
}

/* table de comparaison */
[data-testid="stTable"], .stDataFrame{
    font-family:'IBM Plex Mono', monospace !important;
}
[data-testid="stTable"] table{
    background:var(--bg-panel) !important;
    border:1px solid var(--line) !important;
}
[data-testid="stTable"] th{
    color:var(--text-dim) !important;
    text-transform:uppercase;
    font-size:10.5px !important;
    letter-spacing:0.06em;
    border-bottom:1px solid var(--line) !important;
}
[data-testid="stTable"] td{
    border-bottom:1px solid var(--line) !important;
}
hr{border-color:var(--line) !important;
}
[data-testid="stHeader"]{
    display:none;
}
[data-testid="stToolbar"]{
    display:none;
}
[data-testid="stDecoration"]{
    display:none;
}
</style>
""", unsafe_allow_html=True)

st.title("ClimateRiskSim")
st.caption("MODÈLE DE RISQUE COLLECTIF · SIMULATION MONTE-CARLO")

# ---------- sidebar : paramètres ----------
st.sidebar.header("Paramètres")

hazard_names = ["all"] + [h["name"] for h in HAZARDS]
hazard_name = st.sidebar.selectbox("Aléa climatique", hazard_names, index=0)

scenario_name = st.sidebar.selectbox("Scénario climatique", [s["name"] for s in SCENARIOS], index=0)

years = st.sidebar.slider("Années simulées", min_value=100, max_value=5000, value=1000, step=100)

capital = st.sidebar.number_input("Capital disponible (€)", min_value=0, value=100000, step=10000)

run_clicked = st.sidebar.button("Lancer la simulation", type="primary")
compare_clicked = st.sidebar.button("Comparer les 3 scénarios")


def choose_hazard(name) :
    if name == "all" :
        return HAZARDS
    for h in HAZARDS :
        if h["name"] == name :
            return [h]
    raise ValueError(f"Unknown hazard : {name}")


def choose_scenario(name) :
    for s in SCENARIOS:
        if s["name"] == name :
            return s
    raise ValueError(f"Unknown scenario : {name}")


def run_model(hazard_name, scenario_name, years, capital) :
    risks = choose_hazard(hazard_name)
    scenario = choose_scenario(scenario_name)
    adjusted_risks = [apply_scenario(r, scenario) for r in risks]  # applique le scénario à CHAQUE aléa sélectionné

    losses = simulation(adjusted_risks, years = years)

    return {
        "losses" : losses,
        "avg" : statistics.mean(losses),
        "variance" : statistics.variance(losses),
        "var99" : VaR(losses, 0.99),
        "es99" : expected_Shortfall(losses, 0.99),
        "ruin" : ruin_prob(losses, capital),
        "cap_reco" : recommended_capital(losses, 0.99),
    }


def eur(x) :
    return f"{x:,.0f} €".replace(",", " ")


def render_histogram(losses, capital, var99) :
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
        paper_bgcolor="#141b23",
        plot_bgcolor="#141b23",
        font=dict(family="IBM Plex Mono, monospace", color="#8b98a8", size=11),
        height=380,
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis_title="Perte annuelle (€)",
        yaxis_title="Nombre d'années simulées",
        bargap=0.05,
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
if compare_clicked :
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
else :
    res = run_model(hazard_name, scenario_name, years, capital)
    render_result(res, capital)

st.caption(
    "Modèle : fréquence des sinistres ~ Poisson(λ), coût unitaire ~ log-normale(μ,σ). "
    "Résultats issus de src/*.py, exécutés directement — projet fictif à but pédagogique."
)