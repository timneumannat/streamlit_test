import streamlit as st

st.title("Dummy Streamlit Cloud Test App")
st.write("If you see this message, your Streamlit Cloud deployment is working correctly!")

# A simple button to test interactivity
if st.button("Click me"):
    st.write("Button clicked!")

# A slider for additional interactivity
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write("Slider value:", value)
