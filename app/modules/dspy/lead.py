import dspy 

class ExtractRFQSignals(dspy.Signature):
    """Extract key buying signals from an RFQ email for seals of air turbine."""
    email: str = dspy.InputField()
    quantity: str = dspy.OutputField(desc="e.g. '4 units' or '50 LPH commercial'")
    urgency: str = dspy.OutputField(desc="deadline or 'urgent' phrase, or 'none'")
    specs_detail: str = dspy.OutputField(desc="TDS, stages, certifications mentioned?")
    budget_hint: str = dspy.OutputField(desc="range/target price or 'none'")
    authority: str = dspy.OutputField(desc="sender title/domain")
    buying_stage: str = dspy.OutputField(desc="early/catalog vs late/PO ready")

class ScoreRFQLead(dspy.Signature):
    """Score RFQ email 0–100 for purchase probability based on extracted signals."""
    signals: dict = dspy.InputField()  # from previous step
    score: int = dspy.OutputField(desc="0-100, higher = higher chance of order")
    explanation: str = dspy.OutputField(desc="Brief bullets per category")
    label: str = dspy.OutputField(desc="Hot / Warm / Cold")


class RFQLeadScorer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.extract = dspy.ChainOfThought(ExtractRFQSignals)
        self.score = dspy.ChainOfThought(ScoreRFQLead)

    def forward(self, email):
        signals = self.extract(email=email)
        result = self.score(signals=signals)
        return result,signals