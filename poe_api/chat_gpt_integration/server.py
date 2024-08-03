import fastapi
import uvicorn
from fastapi_poe import make_app
from chat_gpt_integration.travelago_bot import TravelagoBot

ACCESS_KEY = "k9ZgSDPtTfAc5QzvUetbzxW9aDGqt8zA"
app = fastapi.FastAPI()

# Create an instance of your TravelagoBot
bot = TravelagoBot()

# Link the bot to the FastAPI app
app = make_app(bot, access_key=ACCESS_KEY)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
# @app.post("/chatbot", response_model=None)
# async def chatbot_endpoint(request: QueryRequest) -> AsyncGenerator[PartialResponse, None]:
#     last_message = request.query[-1].content
    
#     # Call your chatbot logic to generate a response based on the last message
#     response_text = "Your chatbot response here"
    
#     # Yield the response back to the website
#     yield PartialResponse(text=response_text)

# # Run the FastAPI server
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# # async def get_response(self, request: fp.QueryRequest) -> AsyncIterable[fp.PartialResponse]:
# #     last_message = request.query[-1].content
# #     yield fp.PartialResponse(text=last_message)