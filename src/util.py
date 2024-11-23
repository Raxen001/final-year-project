import ollama
import os

HOST = os.environ.get("LLAMA_HOST", "http://localhost:11434")
MODEL = os.environ.get("LLAMA_MODEL", "qwen2.5-coder:7b")
MODELNAME='raven'
MODELFILE='''
FROM qwen2.5-coder:7b
SYSTEM you should only ouput the necessary dockercompose.yml and nothing else. no verbose output, no naml\\n or ``` 
'''

client = ollama.Client(
  host=HOST
)
ollama.create(model=MODELNAME, modelfile=MODELFILE)

def gen_yaml(content):

    response = client.generate(
        model=MODELNAME,
        prompt=content,
    )
    yaml = response['response']
    return yaml


