import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "Country": ["USA", "China", "India", "Germany", "UK", "France", "Japan", "Brazil", "Canada", "Russia", "Australia", "South Korea", "Italy", "Mexico", "South Africa"],
    "GDP (Trillions USD)": [26.8, 19.3, 3.7, 4.2, 3.1, 2.8, 4.9, 1.9, 2.2, 1.5, 1.4, 1.8, 2.0, 1.3, 0.4],
    "Population (Millions)": [331, 1441, 1393, 83, 67, 65, 126, 213, 38, 145, 26, 52, 60, 128, 59],
    "Inflation Rate (%)": [3.5, 2.3, 6.7, 2.1, 3.0, 2.5, 2.8, 5.4, 3.1, 5.6, 4.0, 2.2, 3.4, 6.1, 7.0],
    "Unemployment Rate (%)": [4.2, 5.1, 7.6, 3.0, 4.5, 5.2, 2.6, 8.9, 5.5, 6.2, 4.1, 3.7, 8.2, 4.3, 9.1],
    "Trade Balance (Billion USD)": [-800, 500, -120, 250, 100, -50, 150, -70, -50, 200, 100, 120, -30, -60, -90]
}

df = pd.DataFrame(data)

st.title("Global Economy Data Analytics Dashboard")

metric = st.sidebar.selectbox("Select a metric to visualize", df.columns[1:])

st.subheader(f"{metric} by Country")
fig = px.bar(df, x="Country", y=metric, text=metric, color="Country", color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig)

st.subheader("GDP vs Population")
fig_scatter = px.scatter(df, x="Population (Millions)", y="GDP (Trillions USD)", size="GDP (Trillions USD)", 
                         hover_name="Country", color="Country", color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_scatter)

st.subheader("Share of Global GDP")
fig_pie = px.pie(df, values="GDP (Trillions USD)", names="Country", title="Global GDP Distribution", color="Country", color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_pie)

st.subheader("Global GDP Map")
fig_map = px.choropleth(df, locations="Country", locationmode="country names", color="GDP (Trillions USD)",
                        hover_name="Country", title="GDP Distribution Across the Globe",
                        color_continuous_scale="Pinkyl", range_color=(df["GDP (Trillions USD)"].min(), df["GDP (Trillions USD)"].max()))
st.plotly_chart(fig_map)

st.write("\nData Table:")
st.dataframe(df)
