from fastapi import FastAPI

app = FastAPI(
    title="RemaPomiary API",
    description="This API will be used by website to purchase, activate and manage licenses for my Mobile Application RemaPomiary.",
    version="1.0.0",
    on_shutdown=print("Żegnam!")
)

@app.get('/')
def home():
    return {"message": "api działa!"}