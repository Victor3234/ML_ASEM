import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report

# Simulează rezultatele modelelor (înlocuiește cu rezultatele tale)
results = pd.DataFrame({
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest'],
    'Accuracy': [0.945, 0.92, 0.93],
    'Precision': [0.55, 0.60, 0.65],
    'Recall': [0.17, 0.40, 0.50],
    'F1-Score': [0.26, 0.48, 0.55]
})

# Titlul aplicației
st.title("Compararea Performanțelor Modelelor de Clasificare")

# Afișarea tabelului cu rezultatele
st.subheader("Rezultate")
st.dataframe(results)

# Afișarea graficelor (opțional)
st.subheader("Graficul Performanțelor")
st.bar_chart(results.set_index('Model')[['Accuracy', 'Precision', 'Recall', 'F1-Score']])
