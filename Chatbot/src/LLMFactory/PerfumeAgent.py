import os
import google.generativeai as genai
from typing import Optional, Dict, Any
from .AgentTools import AgentTools

from pathlib import Path
import json
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "data.json"
with DATA_FILE.open(encoding="utf-8") as f:
    products_data = json.load(f)["products"]



class PerfumeAgent:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("GEMENI_API_KEY")
        self.tools = AgentTools(products_data, self.api_key)

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=genai.types.GenerationConfig(
                temperature=0.7, top_p=0.8, top_k=40, max_output_tokens=800
            )
        )

    def _decide_action(self, prompt: str):
     
        if "weather" in prompt.lower():
            return "weather"
        elif "perfume" in prompt.lower() or "fragrance" in prompt.lower():
            return "rag"
        else:
            return "chat"

    def chat(self, prompt: str, name="customer"):
        action = self._decide_action(prompt)

        if action == "weather":
            city = "Cairo"  # ممكن تستخرجها من الهستوري أو من السؤال
            tool_result = self.tools.get_weather(city)
            context = f"Weather info for {city}: {tool_result}"
        elif action == "rag":
            tool_result = self.tools.rag_search(prompt)
            context = f"Perfume search results: {tool_result}"
        else:
            context = ""

        system_prompt = f"""
        You are Aria, a perfume agent.
        Customer said: {prompt}
        Extra context: {context}
        Respond helpfully.
        """

        response = self.model.generate_content(system_prompt)

        reply = response.text.strip() if response and response.text else "Sorry, I couldn't respond."
        self.tools.save_interaction(name, prompt, reply, meta={})
        return reply
