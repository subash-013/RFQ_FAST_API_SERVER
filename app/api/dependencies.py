from functools import cache
from app.core.config import settings
from app.modules.dspy.rfq import RFQClassifier
from app.modules.dspy.lead import RFQLeadScorer
import dspy


@cache
def fetch_and_configure_lm():
    """This runs ONLY ONCE in the lifetime of Fast API server."""
    print("🤖 Connecting to Ollama...")
    dspy_lm = dspy.LM(
        model=f"ollama_chat/{settings.ollama_model}",
        base_url=settings.ollama_host,
        temperature=0.1,
        max_tokens=512,
        timeout_s=120
    )
    dspy.settings.configure(lm=dspy_lm)      # configure once when first requested
    print("✅ LLM configured")
    return dspy_lm


@cache
def get_rfq_classifier():
    """Singleton RFQClassifier instance — created once per worker"""
    return RFQClassifier()

@cache
def get_rfq_lead_scorer():
    """Singleton RFQLeadScorer instance — created once per worker"""
    return RFQLeadScorer()

