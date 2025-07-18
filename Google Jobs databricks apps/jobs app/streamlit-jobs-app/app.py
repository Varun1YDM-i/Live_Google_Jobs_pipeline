# ---------------------------- after updating it :- instead of image for pipeline view inserting code

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder


# Mock DataFrames for display
jobs_data = pd.DataFrame({
    'Job Title': ['Data Engineer II Development', 'AI Python Developer_446', 'Allianz'],
    'Company': ['Thermo Fisher', 'Allianz', 'Allianz'],
    'Location': ['Bengaluru, India', 'India', 'Bengaluru, India'],
    'Job Role': ['Data Engineer', 'AI Specialist', 'Data Analyst']
})



kpi_data = pd.DataFrame({
    'Company': ['Allianz', 'Thermo Fisher', 'TCS'],
    'Count': [120, 95, 60]
})

location_data = pd.DataFrame({
    'Location': ['Bengaluru', 'Mumbai', 'Remote'],
    'Count': [100, 80, 70]
})

daily_posting = pd.DataFrame({
    'Date': pd.date_range(start='2024-04-01', periods=10),
    'Postings': [12, 15, 20, 18, 25, 30, 28, 32, 31, 29]
})

# Sidebar for Navigation

st.sidebar.title("🔎 Job Pipeline Navigation")

st.sidebar.markdown("---")  # Divider line

page = st.sidebar.radio(
    "📋 Select a Page:",
    ["🏢 Job Marketplace", "🔧 Pipeline View", "📊 KPI Dashboard", "🧭 Search & Explore Jobs", "🧪 Testing"],
    label_visibility="visible"
)

st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using Streamlit")

# ------------------------------------------------------------------------------

json_path = "data/pipeline_status.json"
df_par = pd.read_json(json_path , )
lst_scs_run = df_par['last_successful_run'].to_list()
new_jobs_today = df_par['new_jobs_today'].to_list()
record_count = df_par['record_count'].to_list()
dt_obj = datetime.strptime(lst_scs_run[0], "%Y-%m-%d %H:%M:%S")
formatted_date = dt_obj.strftime("%d-%m-%Y") 
formatted_time = dt_obj.strftime("%H:%M")     
# --------------------------------------------------------------------------------------
# importing from 
if page == '🧪 Testing':

    excel_path = "data/jobs_output.xlsx"  # ✅ Relative path from app.py
    json_path = "data/pipeline_status.json"
    df_jobs = pd.read_excel(excel_path, engine="openpyxl")
    # df_par = pd.read_json(json_path , )
    st.dataframe(df_jobs)
    # -------------------------
    image = Image.open("data/jobs_pipeline.drawio (1).png")
    st.image(image, caption="Job Trends", use_column_width=True)

# ------------------------------------------------------------------------------------

if page == "🏢 Job Marketplace":
    st.title("💼 Job Marketplace")
    st.write("")  # Spacer

    # Top Section: Pipeline Status + Last Run
    top_col1, top_col2 = st.columns([1.5, 2], gap="large")
    
    with top_col1:
        with st.container():
            st.subheader("🚀 Pipeline Status")
            # st.success("The pipeline is Live")
            st.write(
                        """
                        <div style="
                        background-color: #1b4332;
                        color: white;
                        padding: 6px 4px;
                        border-radius: 8px;
                        font-size: 26px;
                        font-weight: 500;
                        text-align: center;
                        ">
                        ✅ The pipeline is Live
                        </div>
                        """,
                        unsafe_allow_html=True
            )
    
    with top_col2:
        with st.container():
            st.subheader("📌 Last Successful Run")
            # st.text("📅 Date: 24-04-2024")
            st.write(f"<div style='font-size: 26px;'>📅 Date: {formatted_date}</div>", unsafe_allow_html=True)
            st.write(f"<div style='font-size: 20px;'>⏰ Time: {formatted_time}</div>", unsafe_allow_html=True)
            # st.text(f"⏰ Time: {formatted_time}")
    st.write("")  # Spacer

    # Metrics Section
    metric_col1, metric_col2 = st.columns([1.5,2], gap="large")

    with metric_col1:
        with st.container():
            st.subheader("🆕 New Jobs Today")
            st.write(f"<div style='font-size: 30px;margin-left:50px;'>{new_jobs_today[0]}</div>", unsafe_allow_html=True)
            # st.metric(label="🆕 New Jobs Today", value="30")

    with metric_col2:
        with st.container():
            st.subheader("📊 Total Job Records")
            st.write(f"<div style='font-size: 30px;margin-left:50px;'>{record_count[0]}</div>", unsafe_allow_html=True)
            # st.metric(label="📊 Total Job Records", value="2349")


# ------------------------------------------------------------------------------------------------------------

# Pipeline View Page
elif page == "🔧 Pipeline View":
    st.title("Pipeline View (Data Lineage)")

    st.markdown("""
    ### 🛠️ Pipeline Stages
    1. **API** ⟶ Fetch jobs based on roles
    2. **Bronze Layer**
        - `raw_jobs` (append only)
        - `daily_jobs` (overwrite daily)
    3. **Silver Layer**
        - `clean_jobs` (cleaned + SCD Type 1 logic)
    4. **Gold Layer**
        - `KPI Tables` (aggregated metrics)
    
    """)
    st.write("")
    image = Image.open("data/jobs_pipeline.drawio (1).png")
    st.image(image, caption="Pipeline Image", use_column_width=True)
    st.info("Use the left sidebar to explore KPIs and search jobs.")
# ----------------------------------------------------------------------------------------------------
# KPI Dashboard Page
elif page == "📊 KPI Dashboard":
    st.title("KPI Dashboard")

    tab1, tab2, tab3, tab4 = st.tabs(["Top Hiring Companies", "Jobs by Location", "Daily Job Posting Trend","Remote vs Onsite"])

    with tab1:
        st.subheader("Top Hiring Companies")
        df_tp_cmp = pd.read_excel('data/top_companies.xlsx', engine="openpyxl")
        df_top_10 = df_tp_cmp.sort_values(by="job_postings", ascending=False).head(8)
        # top_n = st.slider("Select number of top companies to display", min_value=1, max_value=20, value=10)
        # df_top_n = df_tp_cmp_sorted.head(top_n)

        fig = px.bar( df_top_10, x='job_postings', y='company_name', title="Top Hiring Companies",orientation='h', 
                      color='job_postings',
                      color_continuous_scale='blues'
                    )
        fig.update_layout( xaxis_title="Number of Job Postings",yaxis_title="Company", yaxis=dict(autorange="reversed"),
                           plot_bgcolor='rgba(0,0,0,0)',
                           paper_bgcolor='rgba(0,0,0,0)'
                         )

        # Display chart
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.subheader("Jobs by State")

        # Load and preprocess the data
        df_jb_loc = pd.read_excel('data/jobs_by_location_city.xlsx', engine="openpyxl")

        # Fill missing states
        df_jb_loc["state"] = df_jb_loc["state"].fillna("Remote")

        # Group by state and sum job postings
        df_by_state = df_jb_loc.groupby("state", as_index=False)["job_postings"].sum()

        # Sort
        df_by_state = df_by_state.sort_values(by="job_postings", ascending=False)

        # Plot
        fig2 = px.bar(
            df_by_state,
            x="job_postings",
            y="state",
            orientation="h",
            color="job_postings",
            color_continuous_scale="viridis",
            title="Jobs by State"
        )

        fig2.update_layout(
            xaxis_title="Job Postings",
            yaxis_title="State",
            yaxis=dict(autorange="reversed"),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )

        st.plotly_chart(fig2, use_container_width=True)
    with tab3:
        st.subheader("Daily Job Posting Trend")

        # Load the data
        df_daily = pd.read_excel('data/jobs_posting_trend.xlsx', engine="openpyxl")

        # Convert date column to datetime
        df_daily["date_posted"] = pd.to_datetime(df_daily["date_posted"], errors='coerce')

        # Drop null dates (e.g. '-')
        df_daily = df_daily.dropna(subset=["date_posted"])

        # Sort and get last 10 days
        df_last_10 = df_daily.sort_values("date_posted").tail(10)

        # Plot line chart
        fig3 = px.line(
            df_last_10,
            x="date_posted",
            y="daily_job_postings",
            markers=True,
            title="Daily Job Posting Trend (Last 10 Days)",
            labels={"date_posted": "Date", "daily_job_postings": "Number of Jobs"},
            color_discrete_sequence=["#1F487E"]
        )

        fig3.update_layout(
            xaxis_title="Date",
            yaxis_title="Job Postings",
            xaxis=dict(tickformat="%d-%b"),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )

        st.plotly_chart(fig3, use_container_width=True)
    

    with tab4:
        st.subheader("Remote vs Onsite Jobs")

        # Load the data
        df_job_type = pd.read_excel("data/remote_vs_onsite.xlsx", engine="openpyxl")

        # Create pie chart
        fig4 = px.pie(
            df_job_type,
            names="job_type",
            values="count",
            title="Remote vs Onsite Job Distribution",
            color_discrete_sequence=["#1F487E", "#B5E2FA"],
            hole=0.3  # for donut style
        )

        fig4.update_traces(textinfo='percent+label')

        st.plotly_chart(fig4, use_container_width=True)


# ------------------------------------------------------------------------------------------------------------

# Search & Explore Jobs Page
elif page == "🧭 Search & Explore Jobs":
    st.title("🔍 Search & Explore Jobs")

    # ✅ Load Excel data
    excel_path = "data/jobs_output.xlsx"
    df_jobs = pd.read_excel(excel_path, engine="openpyxl")

    # ✅ Select only required columns
    selected_cols = [
        "job_title", 
        "search_role", 
        "company_name", 
        "loacation", 
        "posted_at", 
        "schedule_type"
    ]
    df_filtered = df_jobs[selected_cols].copy()

    # ✅ Format posted_at to show only date
    df_filtered["posted_at"] = pd.to_datetime(df_filtered["posted_at"]).dt.strftime('%d-%m-%Y')

     # ✅ UI: Select column and search term
    search_col = st.selectbox("🔎 Select column to search", options=selected_cols)
    search_term = st.text_input(f"Enter value to search in '{search_col}'")

    # ✅ Filter based on search
    if search_term:
        df_filtered = df_filtered[df_filtered[search_col].astype(str).str.contains(search_term, case=False, na=False)]

    # ✅ Display table
    st.dataframe(df_filtered)



