import streamlit as st
import plotly.express as px
from backend import get_data
# Frontend
st.title("Weather Forecast App")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {option} days in {place}")

if place:
    # Get the temperature/sky data
    filtered_data = get_data(place, days)

    match option:
        case "Temperature":
            # Filter data again
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create temperature plot
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature / °C"})
            st.plotly_chart(figure)
        case "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            # Filter data again
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # Create sky conditions plot
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)


