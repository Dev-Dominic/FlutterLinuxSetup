#!/usr/bin/env python

# Imports 
import wget
import os
import sys
import subprocess
from pyunpack import Archive

# Downloading and Unpacking archives
def unpackArchives(path):
    print("Downloading Flutter....")
    flutterArchive = wget.download('https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_v1.7.8+hotfix.4-stable.tar.xz')

    print("\n\nDownloading AndroidSDK....")
    androidSDKArchive = wget.download('https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip')

    # Unpacks archives in SDK folder
    # Creates SDK folder if non exists
    try:    
        os.mkdir(path)
    except FileExistsError:
        print("\n\nSDK folder already made!")
    finally: 
        try:
            os.mkdir(path+'/androidSDK')
        except FileExistsError:
            print("androidSDK folder already made!")

    # Unpacks flutter and androidsdk in SDK folder
    Archive(flutterArchive).extractall(path)
    Archive(androidSDKArchive).extractall(path+'/androidSDK')

    # Deletes archive files from current directory
    os.remove(flutterArchive)
    os.remove(androidSDKArchive)

# Setting PATH variable for sdks
def setPath(path):
    path_string = f'export PATH="$PATH:{path}"\n'

    with open("/home/dominic/.bashrc", "a") as bashFile:
        bashFile.write(path_string)

    # Exports path in console for present use
    # os.environ["PATH"] += os.pathsep + os.pathsep.join(path)
    
    
    print(f"PATH Set:{path}")

# Runs bash shell subprocess 
# Installs various android tools and runs flutter doctor after
"""
def androidToolsInstall():
    # Installing android sdk tools and emulator
    subprocess.run(["sdkmanager", "platform-tools", "platforms;android-28", "build-tools;28.0.3"]) 
    subprocess.run(["sdkmanager", "platforms;android-21"])
    subprocess.run(["sdkmanager", "emulator"])

    # Runs flutter docotor
    subprocess.run(['flutter', 'doctor','--android-licenses'])
    subprocess.run(['flutter', 'doctor'])
"""

# Main
if __name__ == "__main__":
	# Sets default path to Documents folder
	if len(sys.argv) == 2:
		defaultPath = sys.argv[1]
	else:
		defaultPath = '~/Documents'
	

	androidPath = defaultPath + '/androidSDK'
	androidBinPath = androidPath + '/tools/bin'

	unpackArchives(defaultPath)
	setPath(defaultPath + '/flutter/bin')
	setPath(androidPath)
	setPath(androidBinPath)

	# Setting ANDROID_HOME
	with open("/home/dominic/.bashrc", "a") as bashFile:
		bashFile.write(f'export ANDROID_HOME="{androidPath}"')

	os.system(f'chmod +x {androidBinPath}/*')
	# androidToolsInstall() 

	#print("An error occured: Could not setup flutter successfully!")
	print("Exiting.")

