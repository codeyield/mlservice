from fastapi import APIRouter, BackgroundTasks
from src.schemas.requests import TextRequest
from src.services.model import EmotionClassifier
from src.services.utils import print_logger_info

router = APIRouter()


@router.post("/predict/")
async def predict_emotion(text_request: TextRequest, background_tasks: BackgroundTasks):
    """
    Predicting emotions from the text.

    Args:
        text_request (TextRequest): Text request.

    Returns:
        dict: The result of the prediction as dictionary.
    """
    result = EmotionClassifier.predict_emotion(text_request.text)
    background_tasks.add_task(
        print_logger_info,
        text_request.text,
        result,
    )
    return result
