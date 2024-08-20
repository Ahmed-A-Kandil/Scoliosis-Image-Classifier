import streamlit as st

import numpy as np

from keras.models import load_model
from keras.preprocessing import image

model = load_model("Models/Model.h5")


def load_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.0
    return img_tensor


st.title("Classify Image")
st.write("Upload an image to classify it as Scoliosis or Normal.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    image = load_image(uploaded_file)

    if st.button("Classify"):
        prediction = model.predict(image)

        result = "Scoliosis" if prediction[0][0] < 0.5 else "Normal"
        confidence = prediction.max()

        if result == "Scoliosis":
            st.error(f"{result} with {confidence:.2%} confidence")
        else:
            st.success(f"{result} with {confidence:.2%} confidence")
