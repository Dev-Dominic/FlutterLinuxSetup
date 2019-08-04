# Downloading and Unpacking archives
def unpackArchives(path):

    # Imports 
    import wget
    import os
    from pyunpack import Archive

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

    print("\nUnpacking Archives...")
    # Unpacks flutter and androidsdk in SDK folder
    Archive(flutterArchive).extractall(path)
    Archive(androidSDKArchive).extractall(path+'/androidSDK')

    print("Successfully!!! Unpacked")
    print("Garbage Collecting....")

    # Deletes archive files from current directory
    os.remove(flutterArchive)
    os.remove(androidSDKArchive)

# Setting PATH variable for sdks
def setPath(path):
    with open("/home/dominic/.bashrc", "a") as bashFile:
        bashFile.write(f'export PATH="$PATH:{path}"\n')

    print(f"PATH Set:{path}")

# Main
if __name__ == "__main__":
    defaultPath = '/home/dominic/Documents/SDK'
    androidPath = defaultPath + '/androidSDK'

    unpackArchives(defaultPath)
    setPath(defaultPath + '/flutter/bin')
    setPath(androidPath)

    # Setting ANDROID_HOME
    with open("/home/dominic/.bashrc", "a") as bashFile:
        bashFile.write(f'export ANDROID_HOME="{androidPath}"')

    #print("An error occured: Could not setup flutter successfully!")
    print("Exiting.")

