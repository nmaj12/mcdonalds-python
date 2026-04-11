import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import seaborn as sns
from main import wynik_pd

st.title(' == Produkty z McDonalds, o wysokiej kaloryczności == ')
col1, col2 = st.columns([0.3, 0.7])

charts = ["streamlit","matplotlib","seaborn","plotly","altair"]
with col1:
    option = st.selectbox(
        "Który wykres?",
        charts,
    )
    available_categories = wynik_pd['Kategoria'].tolist()
    selected_categories = st.multiselect(
        "Wybierz kategorię (puste = wszystkie):", 
        options = available_categories,
        default = available_categories #domyslnie wybrane są wszystkie kategorie
        )
with col2:
    if selected_categories:
        wynik_pd = wynik_pd[wynik_pd['Kategoria'].isin(selected_categories)]
    
    st.subheader("Tabela danych")    
    st.table(wynik_pd)
    st.subheader("Wykres", divider=True)
    st.write(f"Wybrałeś: {option}")

    match option:
        case "streamlit":
            st.bar_chart(wynik_pd, x="Kategoria", y="Liczba")
        
        case "matplotlib":
            kategorie = wynik_pd['Kategoria'].tolist()
            liczba = wynik_pd['Liczba'].tolist()
            fig, ax = plt.subplots()
            ax.bar(kategorie, liczba)
            plt.xticks(rotation=90)
            st.pyplot(fig)

        case "seaborn":
            fig, ax = plt.subplots()
            sns.barplot(data=wynik_pd, x="Kategoria", y="Liczba", ax=ax)
            plt.xticks(rotation=90)
            st.pyplot(fig)

        case "plotly":
            fig = px.bar(
                wynik_pd,
                x="Kategoria",
                y="Liczba",
                title="Liczba produktów powyżej 500 kcal"
            )
            st.plotly_chart(fig)

        case "altair":
            chart = alt.Chart(wynik_pd).mark_bar().encode(
                x="Kategoria",
                y="Liczba"
            )
            st.altair_chart(chart, use_container_width=True)
        
# uruchamianie w terminalu
# streamlit run wizualizacje.py

# zamknięcie portu przez naciśnięcie Ctrl + C w terminalu