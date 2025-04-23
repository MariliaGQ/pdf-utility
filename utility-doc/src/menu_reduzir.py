import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import tempfile
from pathlib import Path
import io

def exibir_menu_reduzir_pdf(coluna):
    with coluna:
        st.markdown("""
        ### 💽 Reduzir tamanho do PDF
                """)
        st.divider()
        st.markdown("""
        
        Escolha um arquivo PDF e selecione o nível de compressão desejado:
        """)

        # Upload do arquivo PDF
        arquivo_pdf = st.file_uploader(
            label='',
            type='pdf',
            accept_multiple_files=False
        )

        # Opções de qualidade com 300 DPI adicionada
        qualidade_opcoes = {
            "Baixa - 72 DPI": 72,
            "Média - 100 DPI": 100,
            "Alta - 150 DPI": 150,
            "Muito Alta - 300 DPI": 300  # Nova opção
        }
        qualidade_selecionada = st.selectbox(
            "Escolha o nível de compressão:",
            options=list(qualidade_opcoes.keys())
        )

        # Botão para reduzir PDF
        clicou_reduzir = st.button(
            'Reduzir o PDF',
            use_container_width=True,
            disabled=not bool(arquivo_pdf)
        )

        if clicou_reduzir and arquivo_pdf:
            try:
                # Mostrar o indicador de processamento enquanto o PDF está sendo reduzido
                with st.spinner('Reduzindo arquivo - Aguarde...'):
                    dpi = qualidade_opcoes[qualidade_selecionada]
                    pdf_reduzido = reduzir_pdf(arquivo_pdf, dpi)

                nome_arquivo = f"{Path(arquivo_pdf.name).stem}_reduzido.pdf"
                st.download_button(
                    label="Clique para baixar o PDF reduzido",
                    type='primary',
                    data=pdf_reduzido,
                    file_name=nome_arquivo,
                    mime="application/pdf",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Erro ao reduzir o PDF: {e}")

def reduzir_pdf(arquivo_pdf, dpi):
    """
    Reduz o tamanho de um PDF ajustando a resolução das imagens com a PIL.
    
    Parâmetros:
        arquivo_pdf: Arquivo PDF enviado pelo usuário.
        dpi: Resolução desejada (DPI).
    
    Retorna:
        O conteúdo do PDF reduzido em bytes.
    """
    # Abrir o PDF
    pdf_documento = fitz.open(stream=arquivo_pdf.read(), filetype="pdf")

    # Criar um PDF temporário para armazenar as páginas modificadas
    pdf_reduzido = fitz.open()

    # Reduzir as imagens do PDF
    for pagina_num in range(len(pdf_documento)):
        pagina = pdf_documento.load_page(pagina_num)  # Carregar a página do PDF
        pixmap = pagina.get_pixmap(dpi=dpi)  # Converter para imagem com a resolução desejada

        # Verifique se o Pixmap foi gerado corretamente
        if pixmap is None:
            raise ValueError("Erro ao criar o Pixmap da página")

        # Converter a imagem Pixmap para PIL Image
        imagem = Image.open(io.BytesIO(pixmap.tobytes()))

        # Redimensionar a imagem com PIL
        imagem = imagem.resize((imagem.width // 2, imagem.height // 2), Image.Resampling.LANCZOS)

        # Salvar a imagem redimensionada de volta para um formato de PDF
        imagem_bytes = io.BytesIO()
        imagem.save(imagem_bytes, format="PDF")
        imagem_bytes.seek(0)

        # Criar um documento fitz a partir do PDF em memória
        imagem_pdf = fitz.open("pdf", imagem_bytes.read())

        # Adicionar a página redimensionada ao PDF final
        pdf_reduzido.insert_pdf(imagem_pdf)

    # Salvar o PDF comprimido em um arquivo temporário
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_pdf_path = Path(temp_dir) / "pdf_reduzido.pdf"
        pdf_reduzido.save(temp_pdf_path, garbage=4, deflate=True, clean=True)
        pdf_reduzido.close()

        # Verificar se o PDF foi salvo corretamente
        if not temp_pdf_path.exists():
            raise ValueError("Erro ao salvar o PDF comprimido")

        # Ler os bytes do PDF comprimido
        with open(temp_pdf_path, "rb") as output_pdf:
            pdf_data = output_pdf.read()

    pdf_documento.close()
    return pdf_data
