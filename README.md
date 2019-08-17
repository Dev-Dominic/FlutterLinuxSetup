# Flutter Linux Setup

## Description

The purpose of this script is to automate the setup of the newest version of flutter and android sdk, and to save more hours of my life. 

## How to run script

Ensure you have pip and python 3.7.4 installed.

```bash

$ git clone https://github.com/Dev-Dominic/FlutterLinuxSetup.git
$ pip install pipenv
$ pipenv shell 
$ pipenv install 
$ ./flutterSetup.py <path of installation>

```

`Installation is made from the Pipfile.lock`

## Steps the script takes to setup

1. Downloads the flutter android sdk archive files
2. Extracts the archive files into the SDK folder in the Documents
3. Appends path of the flutter and android sdk into .bashrc in home user folder
4. Creates ANDROID_HOME path 
5. Makes all the functions in the ..androidSDK/tools/bin executable

## Issues

- Downloading files from the android and flutter website doesn't take the most up-to-date packages.
- The packages to required for android studio have to be installed manually after initial setup.
(Need to find a way to reload .bashrc file)
- Use of os functions along with subprocess funciton.
(Need to refactor code to use only subprocess)
- Need to make changes to make more readable code. 
