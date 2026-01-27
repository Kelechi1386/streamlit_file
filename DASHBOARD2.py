import pandas as pd
import streamlit as st
import plotly.express as px


# title
st.title("BEST GLOW SHOPPING HOUSE")

# Read in the Dataset
table=pd.read_csv("Shopping_data.csv")
df2=table.head(10)


st.text("The analysis was performed using a customer dataset containing key demographic and spending attriutes,This dataset includes information such as customer ID,gender,age,annual income,and spending score which helps in understanding customer behaivour and spending patterns.By analyzing this data,meaningful insights were generated to support customer segmentation,purchasing behaivour analysis, and data driven decision making.")
st.write(df2)

## Side Bar

st.sidebar.header("FILTER DATA")


table=table.rename(columns={"Genre":"Gender"})



## Gender Filter
g_filter=st.sidebar.multiselect(
    "SELECT DAY(S)",
    options=table["Gender"].unique(),
    default=table["Gender"].unique()
)



## Apply Filters
filter_data=table[(table["Gender"].isin(g_filter))]




##KPI (KEY PERFORMANCE INDICATOR)
st.subheader("Key performance Indicator")
total_aincome=filter_data["Annual Income (k$)"].sum()
avg_spending_score=filter_data["Spending Score (1-100)"].mean()
min_aincome=filter_data["Annual Income (k$)"].min()
min_age=filter_data["Age"].min()
max_age=filter_data["Age"].max()

col1,col2,col3=st.columns(3)
col1.metric("TOTAL ANNUAL INCOME",f"${total_aincome:.2f}")
col1.metric("AVERAGE SPENDING SCORE",f"${avg_spending_score:,.2f}")
col1.metric("MINIMUM ANNUAL INCOME",f"${min_aincome:,.2f}")


col4,col5=st.columns(2)
col1.metric("MINIMUM AGE",f"{min_age}years")
col5.metric("MAXIMUM AGE",f"{max_age}years")

## show the filtered Data impl
st.subheader("filter Data Preview")
st.write(filter_data)

## Descriptive
des_table=(
    filter_data.groupby("Gender").sum(numeric_only=True).reset_index()
)

st.subheader("DESCRIPTIVE ANALYSIS")
st.write(des_table)

 
bar_chart=px.bar(des_table,x="Gender",y="Annual Income (k$)",color="Gender",title="BAR PLOT: TOTAL ANNUAL INCOME BY GENDER")
st.plotly_chart(bar_chart,use_container_width=True)

## Histogram Chart
hist=px.histogram(filter_data,x="Age",nbins=10)
st.plotly_chart(hist,use_container_width=True)



## Diagnostic
dia_table=(
    filter_data.groupby("Gender").mean(numeric_only=True).reset_index()
)

st.subheader("DIAGNOSTIC ANALYSIS")
st.write(dia_table)


bar_chart=px.bar(filter_data,x="Gender",y="Spending Score (1-100)",color="Gender",title="GENDER BASED SPENDING SCORE.")
st.plotly_chart(bar_chart,use_container_width=True)
                

scatter=px.scatter(filter_data,x="Annual Income (k$)",y="Spending Score (1-100)",color="Gender")
st.plotly_chart(scatter,use_container_width=True)


bar_chart=px.bar(filter_data,x="Gender",y="Annual Income (k$)",color="Gender",title="GENDER BASED ANNUAL INCOME.")
st.plotly_chart(bar_chart,use_container_width=True)


bar_chart=px.bar(filter_data,x="Age",y="Spending Score (1-100)",title="AGE BASED ON SPENDING SCORE")
st.plotly_chart(bar_chart,use_container_width=True)


## Grouped Aged Category