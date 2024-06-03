import altair as alt
import pandas as pd
# import seaborn as sns
import streamlit as st

penguin_file = st.file_uploader("Select Your Local LLE features CSV")
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    st.stop()

st.title("Word Similarity")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    penguins_df.columns,
)

# Create a button
# button_clicked = st.button('Process Selection')
selected_y_var = st.selectbox(
    "What about the y?",
    penguins_df.columns,
)
# Create a button
selected_labels_var = st.selectbox(
    "What about the names(labels)?",
    penguins_df.columns,
)
button_clicked = st.button('Process Selection')


if button_clicked and selected_x_var and selected_y_var:
    alt_chart = (
        alt.Chart(penguins_df, title="Scatterplot of word similarity")
        .mark_circle(size=100)
        .encode(
            x=selected_x_var,
            y=selected_y_var,
            color=selected_labels_var,
        )
        .interactive()
    )
    st.altair_chart(alt_chart, use_container_width=True)
