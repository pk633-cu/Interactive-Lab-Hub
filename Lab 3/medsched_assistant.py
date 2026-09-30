import subprocess


def speak(text):
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


# Device initiates the interaction
speak("Good Morning! Reminder to take your medication.")
# Device initiates the interaction
