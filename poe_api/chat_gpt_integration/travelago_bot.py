# travelago_bot.py

from typing import AsyncIterable, Union
from fastapi_poe import PoeBot, QueryRequest, PartialResponse, ErrorResponse, ReportFeedbackRequest, SettingsResponse

class TravelagoBot(PoeBot):

    async def get_response(self, request: QueryRequest) -> AsyncIterable[Union[PartialResponse, ErrorResponse]]:
        try:
            last_message = request.query[-1].content
            # Enhanced example response logic
            if "recommendation" in last_message.lower():
                response_text = "I recommend visiting the Grand Canyon in Arizona for breathtaking views!"
            elif "weather" in last_message.lower():
                response_text = "The weather in Tokyo is currently mild and sunny."
            elif "hotels" in last_message.lower():
                response_text = "For luxury stays, I recommend the Ritz-Carlton. For budget-friendly options, try Airbnb."
            else:
                response_text = f"You asked about: {last_message}"
            
            yield PartialResponse(text=response_text)
        except Exception as e:
            yield ErrorResponse(text=str(e), allow_retry=True)

    async def get_settings(self, setting) -> SettingsResponse:
        return SettingsResponse(
            introduction_message="Welcome to Travelago! I'm here to help with travel destinations, recommendations, weather updates, and more.",
            allow_attachments=False
        )

    async def on_feedback(self, feedback_request: ReportFeedbackRequest) -> None:
        feedback = feedback_request.feedback_type
        print(f"Received feedback: {feedback}")

    async def on_error(self, error_request) -> None:
        print(f"Error occurred: {error_request.message}")
