import pandas as pd 
import streamlit as st
import plotly.express as px


#Title
st.title("🛒BEST GLOW SHOPPING HOUSE🛍️")

# Read In the Dataset.
table=pd.read_csv("Shopping_data.csv")


table.rename(columns={"Genre":"Gender"},inplace=True)
df4=table.head()
st.text("The analysis was performed using a customer dataset containing key demographic and spending attriutes,This dataset includes information such as customer ID,gender,age,annual income,and spending score which helps in understanding customer behaivour and spending patterns.By analyzing this data,meaningful insights were generated to support customer segmentation,purchasing behaivour analysis, and data driven decision making.")
st.write(df4)

## Side Bar

st.sidebar.header("🔍 FILTER DATA")


## Gender Filter
g_filter=st.sidebar.multiselect(
    "SELECT Gender(s)",
    options=table["Gender"].unique(),
    default=table["Gender"].unique()
)


## Apply Filters
filter_data=table[
    (table["Gender"].isin(g_filter))]



## KPI (KEY PERFROMANCE INDICATOR)
st.subheader("📊 Key Performance Indicator")
total_aincome=filter_data["Annual Income (k$)"].sum()
avg_spending_score=filter_data["Spending Score (1-100)"].mean()
min_aincome=filter_data["Annual Income (k$)"].min()
min_age=filter_data["Age"].min()
max_age=filter_data["Age"].max()


col1,col2,col3=st.columns(3)
col1.metric("💰 TOTAL ANNUAL INCOME",f"${total_aincome:,.2f}")
col2.metric("💰 AVERAGE SPENDING SCORE",f"${avg_spending_score:,.2f}")
col3.metric("💰 MINIMUM ANNUAL INCOME",f"${min_aincome:,.2f}")


col4,col5=st.columns(2)
col4.metric("MINIMUM AGE",f"{min_age}years")
col5.metric("MAXIMUM AGE",f"{max_age}years")

# ## Show the Filtered Data Implementation
# st.subheader("filter Data Preview")
# st.write(filter_data)

## Descriptive Analysis.
des_table=(
    filter_data.groupby("Gender").sum(numeric_only=True).reset_index()
)

st.subheader("DESCRIPTIVE ANALYSIS")
st.write(des_table)


## Bar Chart
bar_chart=px.bar(des_table,x="Gender",y="Annual Income (k$)",color="Gender",title="BAR PLOT: TOTAL ANNUAL INCOME BY GENDER")
st.plotly_chart(bar_chart,use_container_width=True)

## Histogram Chart
hist=px.histogram(filter_data,x="Age",nbins=10)
st.plotly_chart(hist,use_container_width=True)


## Gender Split
bar2_plot=px.bar(filter_data,y="Gender")
st.plotly_chart(bar2_plot,use_container_width=True)


## Correlation of Annual Income and spending score.
sca_1=px.scatter(filter_data,x="Annual Income (k$)",y="Spending Score (1-100)",color="Gender")
st.plotly_chart(sca_1,use_container_width=True)

## Spending Score  vs Age.
sca2=px.scatter(filter_data,x="Age",y="Spending Score (1-100)",color="Gender")
st.plotly_chart(sca2,use_container_width=True)

## Grouping Gender Based on Spending Score and Annual income.
spi=filter_data.groupby("Gender")[["Spending Score (1-100)","Annual Income (k$)"]].mean().reset_index()

## Bar Chart for spending score.
sp2=px.bar(filter_data,x="Gender",y="Spending Score (1-100)",color="Gender",title="GENDER BASED ON SPENDING SCORE.")
st.plotly_chart(sp2,use_container_width=True)

## Bar chart for Annual Income.
sp3=px.bar(filter_data,x="Gender",y="Annual Income (k$)",color="Gender",title="GENDER BASED ON ANNUAL INCOME.")
st.plotly_chart(sp3,use_container_width=True)


## Grouped Aged Category.
## Age Grouped.
filter_data["Aged Group"]=pd.cut(filter_data["Age"], bins=[0,20,30,40,50,100],
                        labels=["Teens","20s","30s","40s","50+"])
filter_data


## Group the Age base on spending mean.
age_spend=filter_data.groupby("Aged Group")["Spending Score (1-100)"].mean().reset_index()
age_spend


## Bar Chart for the Grouped Age.
sc3=px.bar(age_spend,x="Aged Group",y="Spending Score (1-100)",title="AGE RANGES BASED ON SPENDING SCORE.")
st.plotly_chart(sc3,use_container_width=True)
