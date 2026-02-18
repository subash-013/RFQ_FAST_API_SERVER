import dspy

class ClassifyRFQ(dspy.Signature):
    """Determine if this email is a genuine RFQ (Request for Quotation / price quote request)."""

    email: str = dspy.InputField(desc="Full email body including subject if available")
    
    is_rfq: bool = dspy.OutputField(desc="true only if the sender is clearly asking for a quotation, pricing, specs, supplier offer, or similar commercial inquiry")
    confidence: float = dspy.OutputField(desc="0.0 to 1.0 — how certain are you?")
    reason: str = dspy.OutputField(desc="One clear sentence explaining the decision")

class RFQClassifier(dspy.Module):
    def __init__(self):
        super().__init__()
        self.classify = dspy.ChainOfThought(ClassifyRFQ)   # or dspy.Predict for simpler

    def forward(self, email: str):
        prediction = self.classify(email=email)
        return prediction
