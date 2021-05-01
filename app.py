import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('''**Data Analysis Application**
''')
st.write("""
[You can reach the data here]
(https://raw.githubusercontent.com/dinislam31/Final-project/main/googleplaystore_cleaned.csv)
""")


@st.cache
def get_df(link_to_df):
    data = pd.read_csv(link_to_df)

    return data


df = get_df("https://raw.githubusercontent.com/dinislam31/Final-project/main/googleplaystore_cleaned.csv")

st.sidebar.header('Data Control')
num_rows1 = st.sidebar.number_input("Number of rows data:", value=0)
num_rows2 = st.sidebar.number_input("", value=10840)
df = df[num_rows1:num_rows2]
st.write(df)

# 2
st.subheader("**Some Mathematical operations:**")
des_col = df.describe().columns
sel_col = st.selectbox("Select the feature:", des_col)
left_side, right_side = st.beta_columns(2)

left_side.subheader("Max value is:")
left_side.write(df[sel_col].max())
left_side.subheader("Median value is:")
left_side.write(df[sel_col].median())
left_side.subheader("Mode value is:")
if len(df[sel_col].mode()) == 1:
    left_side.write(float(df[sel_col].mode()))
else:
    left_side.write((df[sel_col].mode()))

right_side.subheader("Min value is:")
right_side.write(df[sel_col].min())
right_side.subheader("Arithmetic mean value is:")
right_side.write(df[sel_col].mean())
right_side.subheader("Sum value is:")
right_side.write(df[sel_col].sum())

# 3
st.subheader("**Data Visualization:**")
sel_feat1 = st.selectbox("Select features of data:", df.describe().columns)
sel_feat2 = st.selectbox("", df.columns)


def bar_plot():
    con_bar = st.sidebar.slider("Row control for barplot:", 1, len(df), value=10)
    bar = df[:con_bar]
    sns.barplot(x=bar[sel_feat1], y=bar[sel_feat2], ci=None, data=bar)
    st.pyplot()


def pie_plot():
    con_pie = st.sidebar.slider("Row control for pieplot:", 1, len(df), value=10)
    pie_data = df[:con_pie]
    pie = pie_data[sel_feat2].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot()


bar_plot()
pie_plot()
