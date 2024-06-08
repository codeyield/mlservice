from pydantic import BaseModel

class PredictionResult(BaseModel):
    label: str = "unknown"
    score: float = 0.0
