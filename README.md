# 🎬 AI Video Prompt Automator

## 📌 Overview
The **AI Video Prompt Automator** is a dynamic Python script designed to streamline and automate the pre-production workflow for AI-generated videos. Instead of manually crafting complex prompts for image generation and video motion, this tool acts as an "AI Art Director." It takes a project concept and reverse-engineers a complete, structured JSON storyboard.

## 🚀 Why I Built This
During development, I encountered compatibility issues and deprecations with the standard Google Generative AI SDKs. Rather than giving up, I engineered a **direct REST API integration** that bypasses the SDK. 
The script dynamically fetches the active models for my API key, selects the most capable text-generation model (such as `gemini-3.8-flash`), and constructs a structured payload to ensure robust performance.

## 🌍 Use Case: Eco-Sense-AI
I utilized this tool to automate the promotional video workflow for **Eco-Sense-AI** (an AI-powered environmental reporting platform). The script generated highly detailed, cinematic prompts that were immediately ready to be deployed in tools like **Leonardo.ai** (for image generation) and **Luma Dream Machine** (for motion).

## 🛠️ Tech Stack & Features
- **Language:** Python
- **Integration:** Google Gemini REST API (Direct HTTP requests via `requests` library)
- **Prompt Engineering:** Meta-prompting for JSON-structured output (Image Prompt, Motion Prompt, Voiceover Script).
- **Error Handling:** Dynamic model fetching and fallback mechanisms.

## 🏃‍♂️ How to Run
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment and install requirements: `pip install -r requirements.txt`
4. Add your API key directly or via a `.env` file.
5. Run the script: `python main.py`

*The resulting `eco_sense_workflow.json` contains the production-ready prompts used to generate the final video presentation.*