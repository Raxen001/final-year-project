# INSTALLATION GUIDE

## REQUIREMENTS

- OS - FEDORA
- `sudo dnf install python3-devel ripgrep python3 python3-venv`
- Need docker preinstalled
- `docker compose up` on root folder to start ollama instance
- `docker exec -it {{container-id}} bash`
    - ~`ollama pull llama3.2`~
    - `ollama pull qwen2.5-coder:7b`
- `pip install -r requirements.txt`
- `python3 src/main.py`
