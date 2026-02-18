from app.api.dependencies import get_rfq_classifier

def classify_is_rfq(subject: str | None, body: str) -> dict:
    try:
        req_mail = f"Subject: {subject}\n\n{body}" if subject else body
        rfq_classifier = get_rfq_classifier()
        result = rfq_classifier(email=req_mail)

        return {
            "is_rfq": result.is_rfq,
            "confidence": float(result.confidence or 0.5),
            "reason": (result.reason or "No clear reason detected").strip(),
        }
    except Exception as error:
        return error