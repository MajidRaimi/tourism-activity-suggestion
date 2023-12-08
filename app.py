import streamlit as st
from activity_suggester import load_activities_from_csv, suggest_tourism_activity

activities = load_activities_from_csv('data/activities.csv')

st.title('Tourism Activity Suggestion 🧳')

weather_preference = st.radio("Do you prefer outdoor or indoor activities?", ("outdoor", "indoor", "no preference"))
activity_type = st.selectbox("What type of activity are you interested in?", ("adventure", "cultural", "leisure", "educational", "physical"))

if st.button('Suggest Activity'):
    suggestion = suggest_tourism_activity(activities, weather_preference, activity_type)
    st.write("Here's a suggested activity for you:")
    st.write(suggestion)
