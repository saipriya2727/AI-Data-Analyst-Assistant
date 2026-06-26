import streamlit as st
import plotly.express as px


def show_charts(df):

    st.subheader("📊 Interactive Data Visualization")

    numeric_columns = list(df.select_dtypes(include=["number"]).columns)
    all_columns = list(df.columns)

    if len(numeric_columns) == 0:
        st.warning("No numeric columns available.")
        return

    chart_type = st.selectbox(
        "Select Chart",
        [
            "Bar Chart",
            "Line Chart",
            "Scatter Plot",
            "Histogram",
            "Box Plot",
            "Pie Chart"
        ]
    )

    x_axis = st.selectbox("Select X-axis", all_columns)

    y_axis = st.selectbox("Select Y-axis", numeric_columns)

    if chart_type == "Bar Chart":
        fig = px.bar(df, x=x_axis, y=y_axis)

    elif chart_type == "Line Chart":
        fig = px.line(df, x=x_axis, y=y_axis)

    elif chart_type == "Scatter Plot":
        fig = px.scatter(df, x=x_axis, y=y_axis)

    elif chart_type == "Histogram":
        fig = px.histogram(df, x=x_axis)

    elif chart_type == "Box Plot":
        fig = px.box(df, y=y_axis)

    elif chart_type == "Pie Chart":

        counts = df[x_axis].value_counts().reset_index()
        counts.columns = [x_axis, "Count"]

        fig = px.pie(
            counts,
            names=x_axis,
            values="Count"
        )

    st.plotly_chart(fig, use_container_width=True)