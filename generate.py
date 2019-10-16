import glob, os


#dataset_path = 'Macintosh HD⁩/Users⁩/Rakhesh⁩/Desktop⁩/darknet⁩⁩'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for file in glob.glob("data/images/*.jpg"):  
 #   title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test+1:
        counter = 1
        file_test.write(file + "\n")
    else:
        file_train.write(file + "\n")
        counter = counter + 1
file_train.close()
file_test.close()
