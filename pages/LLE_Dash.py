import pandas as pd
import plotly.express as px
from sklearn.manifold import locally_linear_embedding
import streamlit as st

penguin_file = st.file_uploader("Select Your Local LLE features CSV")
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

n_neigbours = st.slider("How many neighbours to consider?", 0, 20, 5)

if st.button("Submit"):
    embedding, _ = locally_linear_embedding(penguins_df,n_neighbors=n_neigbours, n_components=2)
    fig = px.scatter(x=embedding[:,0], y=embedding[:,1])
    st.plotly_chart(fig)
else:
    st.write("please press submit")

