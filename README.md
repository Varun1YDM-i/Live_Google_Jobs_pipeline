# 📡 Live Google Jobs Pipeline

An end-to-end data engineering project built on **Databricks** to extract, process, and analyze job postings from the **Google Jobs API** using **Medallion Architecture** (Bronze → Silver → Gold). It delivers insights via a fully interactive **Streamlit** dashboard [Live](https://hello-world-3935897645615541.aws.databricksapps.com/).

---

## 🚀 Project Overview

The `Live_Google_Jobs_pipeline` automates the process of:
- Collecting job data via **Google Jobs API** (SerpAPI).
- Structuring and transforming it through multiple layers.
- Delivering real-time insights via an analytical dashboard.

This pipeline supports:
- Trend analysis
- Top hiring companies
- Job role distribution across geographies
- Remote vs Onsite job statistics

---
## 📁 Folder Structure
```
📁 Live_Google_Jobs_pipeline/
├── 📂 notebooks/
│   ├── 📄 Bronze_Layer.ipynb
│   ├── 📄 Silver_Layer.ipynb
│   ├── 📄 Gold_Layer.ipynb
│   └── 📄 write_data_to_app.ipynb
├── 📂 app/
│   └── 📄 app.py
├── 📂 data_exports/
│   ├── 📄 kpi_top_companies.xlsx
│   ├── 📄 kpi_jobs_by_location_city.xlsx
│   └── 📄 pipeline_status.json
├── README.md # Project documentation
└── requirements.txt # Python dependencies for Streamlit app
```
---

## 🛠️ Key Technologies

| Technology      | Purpose                                               |
|------------------|--------------------------------------------------------|
| **PySpark**      | Distributed data processing                          |
| **Databricks**   | Cloud platform for running notebooks and pipelines   |
| **SerpAPI**      | API layer to fetch Google Jobs data                  |
| **Delta Lake**   | Storage layer supporting ACID transactions           |
| **Streamlit**    | Interactive frontend dashboard                       |
| **Pandas**       | Data manipulation in the Streamlit app               |
| **Plotly**       | Rich visualizations in the dashboard                 |

---

## 🧱 Medallion Architecture Layers

### 🥉 Bronze Layer
- **Purpose**: Raw data landing zone
- **Tables**:
  - `raw_jobs`: Append-only historical data
  - `daily_jobs`: Overwritten daily with latest API pulls

### 🥈 Silver Layer
- **Purpose**: Data cleansing and transformation
- **Transformations**:
  - Extract `posted_at` and `schedule_type`
  - Split and clean location fields (city, state, country)
  - Convert date fields to timestamp
  - Deduplicate using SCD Type 1 logic on `job_id`
- **Output Table**: `clean_jobs`

### 🥇 Gold Layer
- **Purpose**: KPI generation and aggregation
- **KPIs Produced**:
  - **Top Hiring Companies** (`kpi_top_companies`)
  - **Jobs by Location (City/State)** (`kpi_jobs_by_location_city`)
  - **Daily Job Posting Trends** (`kpi_daily_job_trend`)
  - **Remote vs. Onsite Jobs** (`kpi_job_type_distribution`)

---

## 🔄 Pipeline Workflow

| Step | Notebook | Description |
|------|----------|-------------|
| 1️⃣ | `Bronze_Layer.ipynb` | Extracts and stores raw API data |
| 2️⃣ | `Silver_Layer.ipynb` | Cleans, deduplicates, and structures the data |
| 3️⃣ | `Gold_Layer.ipynb` | Aggregates data into analytical KPIs |
| 4️⃣ | `write_data_to_app.ipynb` | Exports pipeline status and KPIs to files |
| 5️⃣ | `app.py` | Streamlit app to visualize insights |

---

## 📊 Streamlit Dashboard Features

### 1. **Job Marketplace**
- Pipeline status (live/failure)
- Last successful run
- Total jobs available
- New jobs posted today

### 2. **Pipeline View (Data Lineage)**
- End-to-end visual of the flow: **API → Bronze → Silver → Gold**

### 3. **KPI Dashboard**
- Top Hiring Companies
- Job Trends (Last 10 Days)
- Jobs by State
- Remote vs. Onsite Distribution

### 4. **Search & Explore Jobs**
- Dynamic filtering based on:
  - Job title
  - Company
  - Location
  - Employment type

---
## 📈 Future Enhancements

- ⏱️ **CI/CD Integration**  
  Automate pipeline deployment and testing using GitHub Actions or Azure DevOps.

- 📦 **SCD Type 2 Implementation**  
  Implement Slowly Changing Dimension Type 2 logic to preserve historical job data.

- 🔔 **Monitoring & Alerts**  
  Add automated notifications (e.g., email, Slack, or Databricks alerts) for pipeline failures and SLA breaches.

- ☁️ **Cloud Deployment**  
  Host the Streamlit app on a public cloud platform like:
  - [Streamlit Community Cloud](https://streamlit.io/cloud)
  - Azure Web Apps
  - AWS EC2 or S3 + Lambda (for static hosting + backend)



