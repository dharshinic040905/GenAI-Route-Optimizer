import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai

genai.configure(api_key="AIzaSyBvkl0flp1braTclESK3WbDT5n2Vvj3gPs")
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="GenAI Logistics Optimizer", layout="centered")
st.title("🚚 GenAI-Driven Logistics Route Optimizer")

distance = st.slider("Distance (km)", 1, 200, 25)
traffic = st.selectbox("Live Traffic Condition", ["Low", "Medium", "High"])
sla = st.slider("Delivery SLA (minutes)", 30, 240, 90)
fuel_cost = st.slider("Fuel Cost (₹/L)", 80, 120, 100)

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Speak now...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand audio"
    
if st.button("🎤 Voice Input"):
    voice_text = speech_to_text()
    st.success("You said: " + voice_text)

def calculate_eta(distance, traffic):
    speed = 40
    if traffic == "Medium":
        speed = 30
    elif traffic == "High":
        speed = 20
    return (distance / speed) * 60

def calculate_fuel(distance, fuel_cost):
    mileage = 15
    return (distance / mileage) * fuel_cost

def check_sla(eta, sla):
    return "On Time" if eta <= sla else "Delayed"

def generate_ai_narrative(eta, fuel, status, traffic):
    prompt = f"""
    You are a logistics AI assistant.
    Analyze the following delivery situation:
    - Traffic: {traffic}
    - ETA: {eta:.2f} minutes
    - Fuel Cost: ₹{fuel:.2f}
    - SLA Status: {status}
    Provide:
    1. Delivery explanation
    2. Risk analysis
    3. Route improvement suggestion
    Keep response short and professional.
    """
    response = model.generate_content(prompt)
    return response.text

def speak(text):
    tts = gTTS(text=text)
    file = "output.mp3"
    tts.save(file)
    return file

if st.button("🚚 Optimize Route"):
    eta = calculate_eta(distance, traffic)
    fuel = calculate_fuel(distance, fuel_cost)
    status = check_sla(eta, sla)
    st.subheader("📊 Delivery Analytics")
    st.write("ETA:", round(eta, 2), "minutes")
    st.write("Fuel Cost: ₹", round(fuel, 2))
    st.write("Status:", status)
    if status == "Delayed":
        st.error("⚠ SLA BREACH RISK DETECTED")
    else:
        st.success("✅ DELIVERY ON TRACK")
    st.subheader("🤖 GENAI INSIGHT (Gemini)")
    ai_response = generate_ai_narrative(eta, fuel, status, traffic)
    st.write(ai_response)
    st.subheader("🔊 Voice Output")
    audio_file = speak(ai_response)
    st.audio(audio_file)