from pdf2docx import Converter
import os


def convert_pdf(input_file, output_format, output_dir=None):
    cv = Converter(input_file)
    filename = os.path.basename(input_file)
    file_name_without_ext, _ = os.path.splitext(filename)
    output_path_and_name = os.path.join(output_dir, f"{file_name_without_ext}.{output_format}")
    cv.convert(output_path_and_name)
    cv.close()