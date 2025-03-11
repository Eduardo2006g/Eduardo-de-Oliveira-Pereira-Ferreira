from crewai.tools import BaseTool
import pdfplumber

class ReadPDFTool(BaseTool):
    name: str = "PDF Reader"
    description: str = "Extracts text content from PDF files"
    pdfDir: str

    def _run(self) -> str:
        try:
            with pdfplumber.open(self.pdfDir) as pdf:
                texto_completo = ''
                for pagina_num, pagina in enumerate(pdf.pages):
                    texto = pagina.extract_text()
                    if texto:
                        texto_completo += f'--- Página {pagina_num + 1} ---\n{texto}\n'
                return texto_completo.replace('\n', ' ') 
        except Exception as e:
            print(f'Erro ao ler o PDF {self.pdfDir}: {e}')
            return None