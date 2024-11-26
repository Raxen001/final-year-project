#! /usr/bin/python
import os
from re import sub
import sys
import glob
import subprocess
from pprint import pprint
from time import sleep

import util

IGNORE_LIST = ['docker-compose.yml', '.gitignore', 'package.json']
LINE_COUNT_MAX = 500
NEW_LINE = '\n'
SPACE = " "

input_path = ""
docker_path = ""
# docker_path = "/home/raxen/Code/projects/ai-deployer/src/test/html/docker-compose.yml"

def get_path():
    global input_path, docker_path
    input_path = sys.argv[1]
    input_path = os.path.abspath(input_path)
    if not os.path.isdir(input_path):
        print("[ERROR]: DIRECOTRY NOT FOUND")
        sys.exit()

    print("[LOG]: PROJECT DIRECTORY LOADED: ", input_path)
    docker_path = os.path.join(input_path, "docker-compose.yml")
    print("[LOG]: DOCKER COMPOSE PATH LOADED: ", docker_path)
    return input_path

def get_contents():
    files = glob.glob(os.path.join(get_path(), "*.*"))
    content = str(files) + NEW_LINE
    for file in files:
        if file in IGNORE_LIST:
            break

        content += file + NEW_LINE
        with open(file, 'r') as f:
            for _ in range(LINE_COUNT_MAX):
                content += f.readline()

    return content

def write_docker_compose():
    docker_yaml = util.gen_yaml(get_contents())
    if 'ports' in docker_yaml.lower():
        print("[LOG]:", "FOUND PORT, DOING PORT FORWARDING")
        os.system("sudo tailscale funnel --bg 8080")
        os.system("qrencode -t ansi https://legion.tailaadcc.ts.net/")
    try:
        with open(docker_path, 'x') as docker_file:
            docker_file.write(docker_yaml)
            print("[LOG]:", "Docker Compose has been written successfully.")
    except FileExistsError:
        with open(docker_path, 'w') as docker_file:
            docker_file.write(docker_yaml)
            print("[LOG]:", "Docker Compose has been written successfully.")


def run_docker():

    print('[LOG]: Trying to start the docker container...', docker_path)
    command = "docker compose -f " + docker_path + " up"
    os.system(command)
    # command = ['docker', 'compose', '-f', docker_path, 'up', '-d']
    # print(command)
    # ps = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    # while ps.poll() is None:
    #     # stdout, stderr = ps.communicate()
    #     print("[LOG]:", ps.communicate())
    #     sleep(1)
    # else:
    #     stdout, stderr = ps.communicate()
    #     print("[ERROR]:", '[DOCKER ERROR]', stderr)

if __name__ == "__main__":
    write_docker_compose()
    run_docker()
