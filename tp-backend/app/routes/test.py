import asyncio
import io
from fastapi import UploadFile
from app.services.elevenlabs import transcribe_audio, text_to_speech
from app.services.openrouter import call_openrouter_api
from tempfile import SpooledTemporaryFile

import aiofiles  # For reading your test audio file


# -------- OpenRouter & TTS Tests --------
async def run_tests():
    # -------- OpenRouter Test 1 --------
    prompt1 = "How can I scale a SaaS product with $5k in marketing budget?"
    print("🧠 Sending prompt to OpenRouter...")
    try:
        result1 = await call_openrouter_api(prompt1)
        print("✅ OpenRouter Response (1):\n", result1)
    except Exception as e:
        print("❌ Error with OpenRouter (1):", str(e))

    # -------- ElevenLabs TTS Test --------
    print("\n🗣️ Sending text to ElevenLabs for TTS...")
    try:
        audio = await text_to_speech("Hello world from your Thought Partner.")
        with open("tts_output.mp3", "wb") as f:
            f.write(audio)
        print("✅ TTS audio saved as tts_output.mp3")
    except Exception as e:
        print("❌ Error with ElevenLabs TTS:", str(e))

    # -------- STT Test with Sample File --------
    await test_stt()

    # -------- OpenRouter Test 2 --------
    prompt2 = "Can you explain the 80/20 rule in business operations?"
    print("\n🧠 Sending second prompt to OpenRouter...")
    try:
        result2 = await call_openrouter_api(prompt2)
        print("✅ OpenRouter Response (2):\n", result2)
    except Exception as e:
        print("❌ Error with OpenRouter (2):", str(e))


# -------- Direct STT Test Function --------
async def test_stt():
    print("\n🎙️ Testing STT with sample.mp3...")
    test_audio_path = "tests/sample.mp3"  # ensure this file exists

    try:
        async with aiofiles.open(test_audio_path, mode='rb') as f:
            content = await f.read()

        # Properly emulate UploadFile object with a Content-Type
        from starlette.datastructures import UploadFile as StarletteUploadFile, Headers
        from tempfile import SpooledTemporaryFile

        temp_file = SpooledTemporaryFile()
        temp_file.write(content)
        temp_file.seek(0)

        headers = Headers({"content-type": "audio/mpeg"})
        upload_file = StarletteUploadFile(filename="sample.mp3", file=temp_file, headers=headers)

        transcript = await transcribe_audio(upload_file)
        print("✅ STT Transcript:\n", transcript)

    except Exception as e:
        print("❌ STT Test Failed:", str(e))


# -------- Main Entry Point --------
if __name__ == "__main__":
    asyncio.run(run_tests())
