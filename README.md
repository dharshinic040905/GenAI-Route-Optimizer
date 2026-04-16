# 🚚 GenAI-Driven Logistics Route Optimizer

An AI-powered **Logistics Optimization Web App** built using **Streamlit** and **Google Gemini API**. This application analyzes delivery conditions like distance, traffic, fuel cost, and SLA to provide **ETA predictions, cost analysis, and intelligent route recommendations**.

## 🚀 Features

* 📍 Real-time route analysis
* ⏱️ ETA (Estimated Time of Arrival) calculation
* ⛽ Fuel cost estimation
* 📊 SLA (Service Level Agreement) monitoring
* 🤖 AI-powered insights using Gemini
* 🎤 Voice input support (Speech Recognition)
* 🔊 Voice output using Text-to-Speech

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **AI Model:** Google Generative AI (Gemini 2.5 Flash)
* **Libraries:**

  * `streamlit`
  * `speech_recognition`
  * `gTTS`
  * `google-generativeai`

## 📌 How It Works

1. Enter delivery details (distance, traffic, SLA, fuel cost)
2. Use voice input (optional)
3. System calculates:

   * ETA
   * Fuel cost
   * SLA status
4. Gemini AI generates:

   * Delivery explanation
   * Risk analysis
   * Route optimization suggestions
5. AI response is also converted into voice output

## 📂 Project Structure

```bash
GenAI-Logistics-Optimizer/
│── app.py
│── README.md
```

## ▶️ Run Locally

### 1️⃣ Install Dependencies

```bash
pip install streamlit google-generativeai speechrecognition gtts
```

### 2️⃣ Run the App

```bash
streamlit run app.py
```

## 🔐 API Key Setup

Replace your API key in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

> ⚠️ Do not expose your API key in public repositories.

## 💡 Use Cases

* 🚛 Fleet Management
* 📦 Delivery Optimization
* 🧠 AI Decision Support Systems
* 📉 Cost Reduction Analysis

## 🌟 Future Enhancements

* 🌐 Multi-language voice support
* 📡 Live traffic API integration
* ☁️ Cloud deployment
* 📊 Advanced analytics dashboard

## 🙌 Acknowledgment

Built using **Streamlit** and **Google Generative AI (Gemini)**.

⭐ Star this repository if you found it useful!
