import streamlit as st 
import requests 
import pandas as pd 
import folium
from streamlit_folium import st_folium

# fetch data from API 
def fetch_data():
    url = "https://server-omega-tan-51.vercel.app/data"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed fetching the data from the API")
        return None 
    
#creating map
def create_map(data):
    m = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=10)
    
    #adding markers 
    for idx, row in data.iterrows():
        popup_content = f"""
        <b>Air Liquidity:</b> {row['air_liquidity']}<br>
        <b>Temperature:</b> {row['temperature']}<br>
        <b>Water Conductivity:</b> {row['water_conductivity']}<br>
        <b>Water level:</b> {row['water_level']}<br>
        <b>Water Quality:</b> {row['water_quality']}<br>
        """
        
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup = folium.Popup(popup_content, max_width=300),
            tooltip=f"Location {idx + 1}"
        ).add_to(m)
        
    return m
    
# main app
def main():
    st.title("Data Visualization App")
    
    data = fetch_data()
    
    if data:
        
        df = pd.DataFrame(data)
        
        st.write("### Raw Data")
        st.dataframe(df)
        
        st.write("### Interactive Map")
        folium_map = create_map(df)
        st_folium(folium_map, width=700, height=500)
        
        st.write("### Temperatures distributions")
        st.bar_chart(df['temperature'])
        
        st.write("### Water quality Distribution")
        st.bar_chart(df['water_quality'])
        
if __name__ == "__main__":
    main()
        
        