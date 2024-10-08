import subprocess

with open('requirements.txt') as req:
    requirements = req.readlines()

for package in requirements:
    subprocess.check_call(["pip","install",package.strip()])