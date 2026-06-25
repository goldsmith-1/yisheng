EMERGENCY_KEYWORDS = [
    "chest pain", "trouble breathing", "shortness of breath", "stroke", "face drooping",
    "one side", "unconscious", "severe bleeding", "suicidal", "kill myself",
    "seizure", "anaphylaxis", "swelling tongue", "can’t breathe"
]

def assess_safety(text: str) -> str:
    lowered = text.lower()
    if any(k in lowered for k in EMERGENCY_KEYWORDS):
        return "urgent"
    return "general"

def disclaimer() -> str:
    return "This information is not medical advice, diagnosis, or treatment. For diagnosis or treatment, consult a licensed healthcare professional."
