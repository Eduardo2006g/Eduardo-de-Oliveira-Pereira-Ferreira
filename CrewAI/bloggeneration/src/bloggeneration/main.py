import os
import sys
from pathlib import Path
from typing import List

from crew import BlogGeneration

def find_pdf_files(directory: str) -> List[str]:
    directory_path = Path(directory).resolve()
    
    if not directory_path.is_dir():
        raise ValueError(f"Invalid directory path: {directory_path}")

    return list(directory_path.glob("**/*.pdf"))

def run() -> None:
    try:
        pdf_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../pdfs"))

        pdf_files = find_pdf_files(pdf_directory)
        if not pdf_files:
            raise FileNotFoundError("No PDF files found in the input directory")
            
        print(f"Found {len(pdf_files)} PDF files")

        for pdf_path in pdf_files:
            print(f"Processing: {pdf_path.name}")
            
            blog_crew = BlogGeneration(pdfDir=str(pdf_path))
            result = blog_crew.crew().kickoff()
            
            output_dir = Path("markdowns")
            output_dir.mkdir(exist_ok=True)
            
            output_path = output_dir / f"{pdf_path.stem}.md"
            output_path.write_text(str(result), encoding="utf-8")
            
    except Exception as e:
        print(f"Pipeline failed: {str(e)}", file=sys.stderr)
        raise

if __name__ == "__main__":
    run()