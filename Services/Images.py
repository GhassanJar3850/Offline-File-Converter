from PIL import Image
from os import listdir
from os.path import splitext, join
from Services.Utilities import *

target_directory = RES_ImagePath
output_directory = OUT_ImagePath
fromExtension = '.png'
target = '.ico'


# png to jpg needs conversion to RGB
for file in listdir(target_directory):
    filename, extension = splitext(file)
    print(filename + extension + ":")
    try:
        if extension == fromExtension:
            full_file_path = join(target_directory, filename + extension)

            im = Image.open(full_file_path)
            #only when converting webp/png/gif to another format that doesn't support transparency
            # im = im.convert('RGB')
            output_file_path = join(
                output_directory, fromExtension.removeprefix(".") + "_to" + target)
            # im.info.pop('background', None)

            im.save(output_file_path)
            print(f"Converted {file} to {output_file_path}")

    except OSError as e:
        print(f"An error occurred while processing {file}: {e}")


# def convertImage(path, targetExtension, destinationPath):
#     filename, extension = splitext(file)
#     try:
#         if extension == fromExtension:
#             im = Image.open(path)

#             # im = im.convert('RGB')
#             output_file_path = join(destinationPath, filename + fromExtension.removeprefix(".") + "_to" + target)
#             # im.info.pop('background', None)

#             im.save(output_file_path)
#             print(f"Converted {file} to {output_file_path}")

#     except OSError as e:
#         print(f"An error occurred while processing {file}: {e}")
