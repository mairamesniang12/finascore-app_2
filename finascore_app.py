import streamlit as st
import numpy as np

st.set_page_config(page_title="FinaScore", layout="centered")

st.title("📊 FinaScore")
st.subheader("Scoring de crédit alternatif – MVP")

st.write(
    "Cette application estime un score de crédit à partir de données "
    "Mobile Money et de comportement financier."
)

st.markdown("---")

# 👉 Entrées utilisateur
st.header("📥 Données financières (simulées)")

R = st.slider("Régularité des revenus", 0.0, 1.0, 0.6)
V = st.slider("Volatilité des transactions", 0.0, 1.0, 0.4)
F = st.slider("Fréquence des transactions Mobile Money", 0.0, 1.0, 0.7)
D = st.slider("Ratio dépenses / revenus", 0.0, 1.0, 0.5)
P = st.slider("Ponctualité des paiements", 0.0, 1.0, 0.8)

# 👉 Calcul du score
score = 100 * (
    0.25 * R +
    0.20 * (1 - V) +
    0.15 * F +
    0.15 * (1 - D) +
    0.25 * P
)

st.markdown("---")

# 👉 Résultats
st.header("📈 Résultat")

st.metric(label="Score de crédit", value=f"{score:.1f} / 100")

if score >= 75:
    st.success("🟢 Risque faible – Profil éligible au crédit")
elif score >= 50:
    st.warning("🟠 Risque moyen – Crédit sous conditions")
else:
    st.error("🔴 Risque élevé – Crédit déconseillé")

st.markdown("---")

st.caption(
    "⚠️ Ce score est basé sur un modèle simulé à des fins académiques."
)
