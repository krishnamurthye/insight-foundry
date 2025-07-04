import subprocess

def stop_ollama_model(model):
    try:
        subprocess.run(["ollama", "stop", model], check=True)
        print(f"Stopped Ollama model: {model}")
    except:
        print(f"Could not stop model: {model}")