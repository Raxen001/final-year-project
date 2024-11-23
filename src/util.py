import ollama
from ollama import Client
from pprint import pprint
import os

HOST = os.environ.get("LLAMA_HOST", "http://localhost:11434")
# MODEL = os.environ.get("LLAMA_MODEL", "llama3.2")

client = Client(
  host=HOST
)

MODELNAME='raven'
MODELFILE='''
FROM llama3.2
SYSTEM You are a DevOps bot created to only output the docker compose files for the relevant input according to the folder structure and files and libraries present in the project only return the valid docker compose and don't return anything else.
'''
ollama.create(model=MODELNAME, modelfile=MODELFILE)


content = "Create me a python3 docker container to run basic python addition program"
response = client.generate(
    model=MODELNAME,
    prompt=content,
)

pprint(dir(response))
print()
pprint(response)
