import requests
import json
import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية من ملف .env المخفي
load_dotenv()

def generate_video_prompts(topic):
    print(f"🔄 جاري الاتصال بنموذج gemini-3.8-flash لمشروع: {topic}...\n")
    
    # قراءة المفتاح بشكل آمن دون كتابته في الكود
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise Exception("لم يتم العثور على المفتاح السري! تأكدي من وجوده في ملف .env")
        
    model_name = "models/gemini-3.8-flash"
    url_gen = f"https://generativelanguage.googleapis.com/v1beta/{model_name}:generateContent?key={api_key}"
    
    headers = {"Content-Type": "application/json"}
    
    prompt = f'''
    You are an expert AI Video Director. Create a 3-scene prompt sequence for a short promotional video about: '{topic}'.
    Output strictly in JSON format without markdown blocks, using this structure:
    [
      {{
        "scene": 1,
        "image_prompt": "highly detailed image generation prompt (cinematic, 4k, photorealistic)",
        "video_motion_prompt": "prompt for video tools like Runway or Luma (e.g., slow pan left, cinematic lighting)",
        "voiceover_script": "text for the voiceover in Arabic"
      }}
    ]
    '''
    
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    res_gen = requests.post(url_gen, headers=headers, json=data)
    
    if res_gen.status_code == 200:
        return res_gen.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        raise Exception(f"خطأ أثناء التوليد: {res_gen.text}")

if __name__ == "__main__":
    project_topic = "Eco-Sense-AI: منصة للتقارير البيئية مدعومة بتحليل الذكاء الاصطناعي لحماية البيئة"
    
    try:
        result = generate_video_prompts(project_topic)
        clean_result = result.replace('```json', '').replace('```', '').strip()
        
        with open("eco_sense_workflow.json", "w", encoding="utf-8") as f:
            f.write(clean_result)
            
        print("🎉 نجاح! تم توليد الأوامر وحفظها في eco_sense_workflow.json")
    except Exception as e:
        print(f"❌ {e}")