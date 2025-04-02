import os
import shutil
import subprocess
import sys

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"[✓] Deleted file: {path}")
    else:
        print(f"[ ] File not found: {path}")

def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"[✓] Deleted folder: {path}")
    else:
        print(f"[ ] Folder not found: {path}")

def uninstall_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", package])
        print(f"[✓] Uninstalled package: {package}")
    except Exception as e:
        print(f"[!] Failed to uninstall {package}: {e}")

def main():
    print("=== Uninstalling Offline LLM Setup ===")

    # Define paths (update if needed)
    home = os.path.expanduser("~")
    model_path = os.path.join(home, "models", "mistral.gguf")
    model_folder = os.path.join(home, "models")
    chatbot_file = "llm_chat.py"

    # Delete files and folders
    delete_file(model_path)
    delete_file(chatbot_file)
    
    # If you want to remove entire model folder (optional)
    if os.path.isdir(model_folder) and not os.listdir(model_folder):
        delete_folder(model_folder)

    # Uninstall llama-cpp-python (optional)
    uninstall = input("Do you want to uninstall llama-cpp-python? [y/N]: ").lower()
    if uninstall == "y":
        uninstall_package("llama-cpp-python")

    print("\n[✓] Cleanup complete. All traces removed.")

if __name__ == "__main__":
    main()