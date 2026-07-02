# backend/tools.py
def eligibility_tool(data):
    schemes = []

    if data.get("income", 999999) < 150000 and data.get("occupation") == "farmer":
        schemes.append("PM Kisan")

    if data.get("income", 999999) < 500000:
        schemes.append("Ayushman Bharat")

    return schemes

def scheme_info_tool(scheme):
    info = {
        "PM Kisan": "प्रधानमंत्री किसान योजना किसानों को सालाना 6000 रुपये देती है।",
        "Ayushman Bharat": "आयुष्मान भारत योजना मुफ्त स्वास्थ्य बीमा देती है।"
    }
    return info.get(scheme, "जानकारी उपलब्ध नहीं है")
