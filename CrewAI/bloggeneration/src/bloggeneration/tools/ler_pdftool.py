from crewai.tools import BaseTool
import pdfplumber
class ler_pdftool(BaseTool):
    name: str = "ler um pdf"
    description: str = "descrição do pdf"

    def _run(self, dir) -> str:
        try:
            with pdfplumber.open(dir) as pdf:
                texto_completo = ''
                for pagina_num, pagina in enumerate(pdf.pages):
                    texto = pagina.extract_text()
                    if texto:
                        texto_completo += f'--- Página {pagina_num + 1} ---\n{texto}\n'
                return texto_completo.replace('\n', ' ')  # Substitui quebras de linha por espaço
        except Exception as e:
            print(f'Erro ao ler o PDF {dir}: {e}')
            return None