import ollama
from ollama import Client

from pprint import pprint

import os
from guidance import models, gen

HOST = os.environ.get("LLAMA_HOST", "http://localhost:11434")
MODEL = os.environ.get("LLAMA_MODEL", "qwen2.5-coder:7b")
client = Client(
  host=HOST
)

MODELNAME='raven'
MODELFILE='''
FROM qwen2.5-coder:7b
SYSTEM you should only ouput the necessary dockercompose.yml and nothing else. no verbose output
'''
ollama.create(model=MODELNAME, modelfile=MODELFILE)


content = "Create me a python3 docker container to run my main.py"
response = client.generate(
    model=MODELNAME,
    prompt=content,
)

pprint(response['response'])
