from pptxtopdf import convert as convert_presentation
from pdf2docx import Converter
from docx2pdf import convert
from openpyxl import Workbook
import pandas as pd
import shutil
import random
import csv
import os


def convert_pdf(input_file, output_format, output_dir=None):
    cv = Converter(input_file)
    filename = os.path.basename(input_file)
    file_name_without_ext, _ = os.path.splitext(filename)
    output_path_and_name = os.path.join(
        output_dir, f"{file_name_without_ext}.{output_format}")
    cv.convert(output_path_and_name)
    cv.close()


def convert_doc(input_file, output_format, output_dir=None):
    extension = input_file.split(".")[-1].lower()
    input_dir = os.path.dirname(input_file)
    file_name_without_ext = os.path.splitext(os.path.basename(input_file))[0]

    original_input_file = input_file
    is_doc_file = extension == "doc"

    if is_doc_file:
        temp_file_name = f"temp_{random.randint(100, 100000)}_{file_name_without_ext}.docx"
        input_file = os.path.join(input_dir, temp_file_name)
        os.rename(original_input_file, input_file)

    output_dir = output_dir or input_dir
    output_file = os.path.join(
        output_dir, f"{file_name_without_ext}.{output_format}")

    convert(input_file, output_file)

    if is_doc_file:
        os.rename(input_file, original_input_file)


def convert_ppt(input_file, output_format, output_dir=None):
    convert_presentation(input_file, output_dir)


def convert_xls(input_file, output_format, output_dir=None):
    extension = input_file.split(".")[-1].lower()
    input_dir = os.path.dirname(input_file)
    file_name_without_ext = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(
        output_dir, f"{file_name_without_ext}.{output_format}")
    if output_format == "csv":
        read = pd.read_excel(input_file, engine="openpyxl")
        read.to_csv(output_file, index=False)
    
    elif output_format == "xlsx":
        wb = Workbook()
        ws = wb.active
        with open(input_file, 'r') as f:
            for row in csv.reader(f):
                ws.append(row)
        wb.save(output_file)
    else:
        print("")  # convert to pdf soon..


def convert_txt(input_file, output_format, output_dir=None):
    input_directory = os.path.dirname(input_file)
    file_name_without_ext, _ = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.join(output_dir or input_directory, f"{file_name_without_ext}.{output_format}")

    shutil.copy2(input_file, output_file)

    print(f"File converted successfully: {output_file}")

