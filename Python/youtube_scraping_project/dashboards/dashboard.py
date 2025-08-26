import streamlit as st
import pandas as pd
import glob
import plotly.express as px
import os

st.title("YouTube Channel Tracker")

# Load all CSV snapshots
output_dir = os.path.join(os.path.dirname(__file__), "../scripts/Python/youtube_scraping_project/output")
all_files = sorted(glob.glob(os.path.join(output_dir, "channel_stats_*.csv")))
print("Files found:", all_files)
if not all_files:
    st.warning("No data files found. Run youtube_data_collection.py first!")
    st.stop()

all_data = pd.concat([pd.read_csv(f) for f in all_files], ignore_index=True)
all_data = all_data.loc[:, ~all_data.columns.str.contains("^Unnamed")]

# Convert 'Date' to datetime
if 'Date' not in all_data.columns:
    all_data['Date'] = pd.to_datetime('today').normalize()
else:
    all_data['Date'] = pd.to_datetime(all_data['Date'])

# Sidebar: select channel
channel = st.selectbox("Select a channel", all_data['Channel Title'].unique())
channel_data = all_data[all_data['Channel Title'] == channel].sort_values("Date")

# --- Date selection ---
available_dates = channel_data['Date'].dt.date.unique()
selected_date = st.selectbox("Pick a date", sorted(available_dates, reverse=True))

# Filter for selected date
data_for_date = channel_data[channel_data['Date'].dt.date == selected_date]

# Display single row table
st.subheader(f"Stats for {channel} on {selected_date}")
st.dataframe(data_for_date[['Subscribers', 'Total Views', 'Video Count']].reset_index(drop=True))

# Line chart: Subscribers
fig_subs = px.line(channel_data, x='Date', y='Subscribers', title=f"{channel} Subscribers Over Time")
st.plotly_chart(fig_subs)

# Line chart: Total Views
fig_views = px.line(channel_data, x='Date', y='Total Views', title=f"{channel} Total Views Over Time")
st.plotly_chart(fig_views)

# Line chart: Video Count
fig_videos = px.line(channel_data, x='Date', y='Video Count', title=f"{channel} Video Count Over Time")
st.plotly_chart(fig_videos)

# Daily change table
channel_data['Subscribers Change'] = channel_data['Subscribers'].diff()
channel_data['Views Change'] = channel_data['Total Views'].diff()
channel_data['Videos Change'] = channel_data['Video Count'].diff()

st.subheader("Daily Changes")
st.dataframe(channel_data[['Date', 'Subscribers Change', 'Views Change', 'Videos Change']].fillna(0))

# run: "streamlit run C:\Users\Austin\Documents\GitHubRepo\data-analyst-portfolio\Python\youtube_scraping_project\dashboards\dashboard.py" to launch
