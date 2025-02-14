# Environmental Data Visualization App

This is a Streamlit-based web application that visualizes environmental data fetched from an API. The data includes metrics such as air liquidity, temperature, water conductivity, water level, and water quality, along with geographic coordinates (latitude and longitude). The app provides interactive visualizations, including an interactive map using Folium, to explore the data.

## Features
- **Interactive Map**: Visualize data points on a map with markers. Hover over markers to see location details and click to view additional information.
- **Raw Data Table**: Display the raw data fetched from the API in a table format.
- **Charts**: Visualize distributions of temperature and water quality using bar charts.
- **API Integration**: Fetch data from a remote API (`https://server-omega-tan-51.vercel.app/data`).

## Technologies Used
- **Streamlit**: For building the web app.
- **Folium**: For creating interactive maps.
- **Pandas**: For data manipulation and analysis.
- **Requests**: For fetching data from the API.

---

## Getting Started

### Prerequisites
Before running the app, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Navashub/Weather_App
   cd Weather_App 
   ```

2. pip install -r requirements.txt

3. streamlit run app.py