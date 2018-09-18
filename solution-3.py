from PIL import Image
from PIL.ExifTags import TAGS
import os
import csv

row = ['Width', 'Height', 'File Name', 'Website']

with open('image_metadata.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=";")
    writer.writerow(row)

    dir = os.listdir('images/')
    for website in dir:
        images = os.listdir('images/' + website)
        for image in images:
            try:
                img = Image.open('images/' + website + '/' + image)
                exifData = dict()
                exifDataRaw = getattr(img, '_getexif', None) 
                if exifDataRaw and hasattr(exifDataRaw, 'items'):
                    for tag, value in exifDataRaw.items():
                        decodedTag = TAGS.get(tag, tag)
                        exifData[decodedTag] = value
                if exifData:
                    print(exifData)
                tup = img.size
                row = [tup[0], tup[1], image, website]
                writer.writerow(row)
            except Exception:
                pass

    csvFile.close()
