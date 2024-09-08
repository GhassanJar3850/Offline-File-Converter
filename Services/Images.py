import os
from PIL import Image
from os import listdir
from os.path import splitext, join
from Services.Utilities import *

# target_directory = RES_ImagePath
# output_directory = OUT_ImagePath
# fromExtension = '.png'
# target = '.ico'


# # png to jpg needs conversion to RGB
# for file in listdir(target_directory):
#     filename, extension = splitext(file)
#     print(filename + extension + ":")
#     try:
#         if extension == fromExtension:
#             full_file_path = join(target_directory, filename + extension)

#             im = Image.open(full_file_path)
#             # only when converting webp/png/gif to another format that doesn't support transparency
#             # im = im.convert('RGB')
#             output_file_path = join(
#                 output_directory, fromExtension.removeprefix(".") + "_to" + target)
#             # im.info.pop('background', None)

#             im.save(output_file_path)
#             print(f"Converted {file} to {output_file_path}")

#     except OSError as e:
#         print(f"An error occurred while processing {file}: {e}")


def convert_Image(input_file, output_format, output_dir=None):
    filename = os.path.basename(input_file)
    file_name_without_ext, extension = os.path.splitext(filename)
    extension = extension.removeprefix(".")
    try:
        im = Image.open(input_file)
        print(f"from {extension} to {output_format}")
        supports_transparency = ["webp", "png", "gif", "svg", "ico"]
        if extension in supports_transparency and output_format not in supports_transparency:
            print("I've been there")
            im = im.convert('RGB')

        output_file_path = os.path.join(
            output_dir, file_name_without_ext + "." + output_format)
        im.info.pop('background', None)

        im.save(output_file_path)
    except OSError as e:
        print(f"An error occurred while processing {input_file}: {e}")
