from pdf2docx import Converter
import os


def convert_pdf(input_file, output_format, output_dir=None):
    cv = Converter(input_file)
    filename = os.path.basename(input_file)
    output_path_and_name = output_dir + "/" + filename + "." + output_format
    print(output_path_and_name)
    cv.convert(output_dir + filename+"."+output_format)
    cv.close()