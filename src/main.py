import os
import sys
import glob
from pprint import pprint
import util
import re

IGNORE_LIST = ['docker-compose.yml', '.gitignore', 'package.json']
LINE_COUNT_MAX = 500
NEW_LINE = '\n'
SPACE = " "

input_path = sys.argv[1]
input_path = os.path.abspath(input_path)

if not os.path.isdir(input_path):
    print("DIRECOTRY NOT FOUND")
    sys.exit()

print("[LOG]: PROJECT DIRECTORY LOADED: ", input_path)

files = glob.glob(os.path.join(input_path, "*.*"))
content = ''
for file in files:
    if file in IGNORE_LIST:
        break

    content += file + NEW_LINE
    with open(file, 'r') as f:
        for i in range(LINE_COUNT_MAX):
            content += f.readline()


docker_yaml = util.gen_yaml(content)
docker_path = os.path.join(input_path, "docker-compose.yml")
try:
    with open(docker_path, 'x') as docker_file:
        docker_file.write(docker_yaml)
except FileExistsError:
    with open(docker_path, 'w') as docker_file:
        docker_file.write(docker_yaml)


def run_docker():
    command = ""
    command += "docker" + SPACE
    command += "compose" + SPACE
    command += "-f" + SPACE 
    command += docker_path + SPACE
    command += "up"
    print('[LOG]: Trying to start the docker container...')
    os.system(command)

run_docker()
