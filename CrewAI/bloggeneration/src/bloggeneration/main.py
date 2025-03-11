#!/usr/bin/env python
import sys
import warnings
import os
import pdfplumber
from datetime import datetime

# Adiciona o diretório 'src' ao sys.path para encontrar o módulo 'crew'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crew import Bloggeneration

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def find_pdf_path(directory):
    """Find all PDF files in the specified directory."""
    abs_directory = os.path.abspath(directory)

    if not os.path.isdir(abs_directory):
        raise ValueError(f"{abs_directory} is not a valid directory.")

    return [
        os.path.join(abs_directory, file) for file in os.listdir(abs_directory) if file.lower().endswith(".pdf")
    ]


def run():
    """Run the crew process."""
    pdf_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../pdfs"))

    try:
        pdf_files = find_pdf_path(pdf_dir)
        print(f"Found PDFs: {pdf_files}")

        for pdf_path in pdf_files:
            inputs = {"pdf_dir": pdf_path}
            result = Bloggeneration().crew().kickoff(inputs=inputs)
            print(result)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
