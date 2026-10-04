import subprocess
from pathlib import Path

import numpy as np
import sherpa_onnx
import sounddevice as sd
from faster_whisper import WhisperModel
from medsched_screen import show_status, show_caption 



# SETTINGS

SAMPLE_RATE = 16000

# MedSched decides the user is finished speaking
# after 1.2 seconds of silence.
MIN_SILENCE = 1

VAD_MODEL = Path("models/silero_vad.onnx")


# SPEAKING FUNCTION


def speak(text):
    show_caption(text)

    piper = subprocess.Popen(
        [
            "python3", "-m", "piper",
            "--model", "speech-scripts/en_US-hfc_female-medium.onnx",
            "--output-raw",
            "--", text
        ],
        stdout=subprocess.PIPE
    )

    subprocess.run(
        ["aplay", "-r", "22050", "-f", "S16_LE", "-t", "raw", "-"],
        stdin=piper.stdout
    )

    piper.wait()



# LISTENING FUNCTION


def listen(recognizer):
    # Setting up voice activity detection
    config = sherpa_onnx.VadModelConfig()

    config.silero_vad.model = str(VAD_MODEL)
    config.silero_vad.min_silence_duration = MIN_SILENCE
    config.silero_vad.min_speech_duration = 0.25
    config.sample_rate = SAMPLE_RATE

    vad = sherpa_onnx.VoiceActivityDetector(
        config,
        buffer_size_in_seconds=30
    )

    window = config.silero_vad.window_size
    buffer = np.empty(0, dtype=np.float32)
    samples_per_read = int(0.1 * SAMPLE_RATE)

    print("Listening...")
    show_status("LISTENING") 

    with sd.InputStream(
        channels=1,
        dtype="float32",
        samplerate=SAMPLE_RATE
    ) as stream:

        while True:
            chunk, _ = stream.read(samples_per_read)
            buffer = np.concatenate(
                [buffer, chunk.reshape(-1)]
            )

            while len(buffer) > window:
                vad.accept_waveform(buffer[:window])
                buffer = buffer[window:]

            if not vad.empty():
                utterance = np.array(
                    vad.front.samples,
                    dtype=np.float32
                )

                vad.pop()

                print("Thinking...")
                show_status("THINKING")

                segments, _ = recognizer.transcribe(
                    utterance,
                    beam_size=1
                )

                text = " ".join(
                    segment.text.strip()
                    for segment in segments
                )

                print("You said:", text)

                return text



# MEDSCHED

print("Loading speech recognition...")

recognizer = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8"
)

# Device initiates the interaction
speak("Good morning! Reminder to take your medication.")

# MedSched waits for the user to respond
user_response = listen(recognizer)

print("Recognized response:", user_response)

# Respond to the user's question
if (
    "what do i take" in user_response.lower()
    or "what medication do i take" in user_response.lower()
):
    speak("You have Vitamin D scheduled for this morning.")

    second_response = listen(recognizer)
    print("Recognized second response:", second_response)

    response = second_response.lower()

    if "folic acid" in response:
        speak(
            "Folic acid is scheduled for this evening. "
            "Please take Vitamin D."
        )

        # Listen for confirmation that Vitamin D was taken
        third_response = listen(recognizer)

        print("Recognized third response:", third_response)

        confirmation = third_response.lower()

        if (
            "done" in confirmation
            or "taken" in confirmation
            or "took it" in confirmation
        ):
            speak("Great! Recorded that you have taken Vitamin D.")
