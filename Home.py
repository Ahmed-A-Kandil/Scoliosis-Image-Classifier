import streamlit as st

st.set_page_config(layout="wide")

st.title("Scoliosis Image Classifier")
st.write("Welcome to the Scoliosis Image Classifier app!")
st.write("Use the sidebar to navigate between pages.")
st.write(
    "On the 'Classify' page, you can upload an image to classify it as Scoliosis or Normal."
)


st.write("### Created by:")

ai_names = {
    "Title": [
        "Artificial Intelligence Dean",
        "Artificial Intelligence Student",
        "Artificial Intelligence Student",
        "Artificial Intelligence Student",
    ],
    "Name": [
        "Dr. Hesham Arafat Ali Khalifa",
        "Mohamed Mohamed Mousa Gobara",
        "Ahmed Amro Abdelmoneim Kandil",
        "Abdullah Mustafa Ahmed Zard",
    ],
}

p_names = {
    "Title": [
        "Physiotherapy Dean",
        "Physiotherapy Associate Professor",
    ],
    "Name": [
        "Dr. Hala Ebrahim Kassem",
        "Dr. Dina Salah Noaman",
    ],
}

col1, col2 = st.columns(2, gap="small")

with col1:
    st.dataframe(ai_names)

with col2:
    st.dataframe(p_names)

st.snow()
