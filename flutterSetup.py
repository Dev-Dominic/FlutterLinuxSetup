# Downloading and Unpacking archives
def unpackArchives():

    # Imports 
    import wget
    import os
    from pyunpack import Archive

    print("Downloading Flutter....")
    flutterArchive = wget.download('https://storage.googleapis.com/flutter_infra/releases/stable/linux/flutter_linux_v1.7.8+hotfix.4-stable.tar.xz')

    print("\n\nDownloading AndroidSDK....")
    androidSDKArchive = wget.download('https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip')

    print(f"\n\n{flutterArchive} : {androidSDKArchive}")
    
    # Unpacks archives in SDK folder
    # Creates SDK folder if non exists
    path = '/home/dominic/Documents/SDK'
    try:    
        os.mkdir(path)
    except FileExistsError:
        print("\n\nUploading Flutter and androidSDK folders...")

    print("\n\nUnpacking Archives...")
    # Unpacks flutter and androidsdk in SDK folder
    Archive(flutterArchive).extractall(path)
    Archive(androidSDKArchive).extractall(path)

    print("\n\nSuccess")
    

# Setting PATH variable for sdks


# Main
if __name__ == "__main__":
    unpackArchives()

