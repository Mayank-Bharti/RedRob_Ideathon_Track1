# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import whisper
from gtts import gTTS
from agent import agent_step
import os
import uuid

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = whisper.load_model("base")
print("Whisper model loaded!")


@app.post("/voice-agent/")
async def voice_agent(file: UploadFile = File(...), lang: str = "hi"):

    # Save user audio
    user_audio_path = f"user_{uuid.uuid4().hex}.wav"
    with open(user_audio_path, "wb") as f:
        f.write(await file.read())

    # STT
    result = model.transcribe(user_audio_path, language=lang)
    user_text = result["text"]
    print(f"USER ({lang}):", user_text)

    # Agent reasoning
    reply_text = agent_step(user_text)
    print("AGENT:", reply_text)

    # TTS
    agent_audio_path = f"agent_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=reply_text, lang=lang)
    tts.save(agent_audio_path)

    return JSONResponse({
        "user_text": user_text,
        "agent_text": reply_text,
        "user_audio": user_audio_path,
        "agent_audio": agent_audio_path
    })

@app.get("/audio/{filename}")
async def get_audio(filename: str):
    """
    Serve audio files to frontend
    """
    return FileResponse(filename, media_type="audio/mpeg")
