import os
import subprocess
import urllib.request
import platform
import sys

# Step 1: Install llama-cpp-python
def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[✓] Installed {package}")
    except subprocess.CalledProcessError:
        print(f"[!] Failed to install {package}")
        sys.exit(1)

# Step 2: Download model if not present
def download_model(destination_path):
    url = "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
    print("[*] Downloading model (~4GB)... This may take some time.")
    urllib.request.urlretrieve(url, destination_path)
    print(f"[✓] Model downloaded to {destination_path}")

# Step 3: Create chatbot Python file
def create_chatbot_file(model_path, chatbot_path):
    chatbot_code = f'''from llama_cpp import Llama

llm = Llama(
    model_path=r"{model_path}",
    n_ctx=2048,
    n_threads=6
)

print("Offline LLM ready! Ask number theory questions (type 'exit' to quit).\\n")

while True:
    question = input("You: ")
    if question.strip().lower() in {{"exit", "quit"}}:
        break
    prompt = f"[INST] {{question}} [/INST]"
    response = llm(prompt, max_tokens=300)
    print("LLM:", response["choices"][0]["text"].strip(), "\\n")
'''
    with open(chatbot_path, "w", encoding="utf-8") as f:
        f.write(chatbot_code)
    print(f"[✓] Chatbot script created: {chatbot_path}")

# Main setup function
def main():
    print("=== Offline LLM Setup for Number Theory ===")
    install_package("llama-cpp-python")

    model_dir = os.path.expanduser("~/models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "mistral.gguf")

    if not os.path.exists(model_path):
        try:
            download_model(model_path)
        except Exception as e:
            print("[!] Model download failed. Please download manually from HuggingFace.")
            print("URL: https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF")
            print("Save it as:", model_path)
            return

    chatbot_path = "llm_chat.py"
    create_chatbot_file(model_path, chatbot_path)

    print("\n[✓] All done! Run your chatbot anytime using:")
    print("    python llm_chat.py")

if __name__ == "__main__":
    main()