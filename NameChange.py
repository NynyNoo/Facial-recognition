import os


folderPath = 'train-images/2/'

# Function to rename multiple files
for count, filename in enumerate(os.listdir(folderPath)):
    if count < 10:
        dst = "image000" + str(count) + ".jpg"
    else:
        dst = "image00" + str(count) + ".jpg"
    src = folderPath + filename
    dst = folderPath + dst
    os.rename(src, dst)