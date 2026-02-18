from app.api.dependencies import get_rfq_lead_scorer

def calculate_lead_score(subject: str | None, body: str) -> dict:
    """
    Uses DSPy to extract signals and calculate a lead score.
    """

    try:
        req_mail = (subject or "").lower() + " " + body.lower()

        scorer = get_rfq_lead_scorer()
        result,signals = scorer(email=req_mail)
        print(f"lead_score_details:\nResult:{result}\nSignals:{signals}")
        score = result.score

        if score >= 80:
            label = "Hot"
        elif score >= 50:
            label = "Warm"
        else:
            label = "Cold"

        return {
            "score": min(max(score, 0), 100),
            "label": label,
            "explanation": result.explanation
        }
    except Exception as error:
        return error
