from InputHandler import receiveInput, createFolder
from MoveFiles import moveToDirectory

print('''
========================================================================================================================
                                                    PYORGANIZER
========================================================================================================================
''')
print('''
This program will organize your files in the program's folder, according to the files extensions.

________________________________________________________________________________________________________________________
________________________________________________________________________________________________________________________

1. Create 'Images' folder. (.jpg, .png, .bmp, .gif, .tif, .tiff)

2. Create 'Videos' folder. (.mp4, .avi, .mov, .avchd, .wmv, .webm, .mkv)

3. Create 'Audios' folder. (.mp3, .wav, .ogg, .aac, .flac, .alac, .aiff, .dsd, .pcm)

4. Create 'Texts' folder. (.txt, .pdf, .doc, .json)

5. Create 'Installers' folder. (.exe, .msi, .msm,  .msp)

6. Create 'Zipped' folder (.zip, .tar, .gz, .7z)

7. Create all of the above.
''')

answer = receiveInput(1, 7)

if answer == 1:
    createFolder("Images")
    moveToDirectory(('.jpg', '.png', '.bmp', '.gif', '.tif', '.tiff'), "Images")
elif answer == 2:
    createFolder("Videos")
    moveToDirectory(('.mp4', '.avi', '.mov', '.avchd', '.wmv', '.webm', '.mkv'), "Videos")
elif answer == 3:
    createFolder("Audios")
    moveToDirectory(('.mp3', '.wav', '.ogg', '.aac', '.flac', '.alac', '.aiff', '.dsd', '.pcm'), "Audios")
elif answer == 4:
    createFolder("Texts")
    moveToDirectory(('.txt', '.pdf', '.doc', '.json'), "Texts")
elif answer == 5:
    createFolder("Installers")
    moveToDirectory(('.exe', '.msi',  '.msm', '.msp'), "Installers")
elif answer == 6:
    createFolder("Zipped")
    moveToDirectory(('.rar', '.zip', '.tar', '.gz', '.7z'), "Zipped")
elif answer == 7:
    createFolder("Images")
    moveToDirectory(('.jpg', '.png', '.bmp', '.gif', '.tif', '.tiff'), "Images")
    createFolder("Videos")
    moveToDirectory(('.mp4', '.avi', '.mov', '.avchd', '.wmv', '.webm', '.mkv'), "Videos")
    createFolder("Audios")
    moveToDirectory(('.mp3', '.wav', '.ogg', '.aac', '.flac', '.alac', '.aiff', '.dsd', '.pcm'), "Audios")
    createFolder("Texts")
    moveToDirectory(('.txt', '.pdf', '.doc', '.json'), "Texts")
    createFolder("Installers")
    moveToDirectory(('.exe', '.msi', '.msm', '.msp'), "Installers")
    createFolder("Zipped")
    moveToDirectory(('.zip', '.tar', '.gz', '.7z'), "Zipped")




