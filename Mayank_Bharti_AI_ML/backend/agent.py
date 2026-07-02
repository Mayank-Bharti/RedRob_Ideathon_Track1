# backend/agent.py
from memory import update_memory, get_memory
from tools import eligibility_tool, scheme_info_tool
import re

REQUIRED_FIELDS = ["age", "income", "occupation"]

NUMBER_MAP = {
    "zero":0, "ek":1, "do":2, "teen":3, "char":4, "chaar":4, "paanch":5, "paach":5, "chhe":6,
    "saat":7, "aath":8, "nau":9, "das":10, "gyarah":11, "baarah":12, "teerah":13, "chaudah":14,
    "pandrah":15, "solah":16, "satrah":17, "atharah":18, "unnees":19, "bees":20, "tees":30, "chaalees":40,
    "pachaas":50, "saath":60, "sattar":70, "assi":80, "nabbe":90, "sau":100
}

def word_to_number(text):
    text = text.lower()
    for word, num in NUMBER_MAP.items():
        if word in text:
            return num
    return None


def extract_info(user_text):
    mem = get_memory()
    expected = mem.get("expected_field")
    text = user_text.lower()
    extracted = False  

   
    if expected == "age":
        age_num = word_to_number(text)
        if age_num is not None:
            update_memory("age", age_num)
            extracted = True
        else:
            m = re.search(r"\d+", text)
            if m:
                update_memory("age", int(m.group()))
                extracted = True

   
    elif expected == "income":
        num = word_to_number(text)   
        if num is not None and "lak" in text:
            update_memory("income", num * 100000)
            extracted = True
        else:
            digits = "".join(filter(str.isdigit, text))
            if digits:
                update_memory("income", int(digits) * 100000)
                extracted = True

    
    elif expected == "occupation":
        if "kisan" in text or "किसान" in text:
            update_memory("occupation", "farmer")
            extracted = True
        elif "teacher" in text or "शिक्षक" in text:
            update_memory("occupation", "teacher")
            extracted = True

    if extracted:
        update_memory("expected_field", None)


def planner():
    mem = get_memory()
    missing = [f for f in REQUIRED_FIELDS if f not in mem or mem[f] is None]
    if missing:
        mem["expected_field"] = missing[0]  
        update_memory("expected_field", missing[0])
        return f"कृपया अपनी {missing[0]} बताएं।"
    return None


def executor():
    """Call eligibility tool"""
    mem = get_memory()
    return eligibility_tool(mem)

def evaluator(schemes):
    """Prepare response"""
    if not schemes:
        return "आप किसी भी सरकारी योजना के लिए पात्र नहीं हैं।"

    response = "आप इन योजनाओं के लिए पात्र हैं:\n"
    for s in schemes:
        response += f"- {s}: {scheme_info_tool(s)}\n"
    return response

def agent_step(user_text):
    if not user_text.strip():
        return "माफ़ कीजिए, आपकी आवाज़ समझ नहीं आई। कृपया दोबारा बोलें।"

    
    extract_info(user_text)

    
    missing_info = planner()
    if missing_info:
        return missing_info

   
    schemes = executor()

   
    return evaluator(schemes)
