import streamlit as st

st.title("Streamlit is amazing! 🎈")

# You can provide a local file path or a URL to the image
image_path = "data/Image.jpg"  # Replace with the actual path or URL

# Display the image
st.image(image_path, use_column_width=True)

if st.button('More ❄️❄️❄️ please!'):
    st.balloons()
