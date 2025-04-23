
import streamlit as st
from streamlit_option_menu import option_menu
from menu_extrair import exibir_menu_extrair
from menu_reduzir import exibir_menu_reduzir_pdf
from menu_unir import exibir_menu_unir_pdf
from menu_imagens import exibir_menu_imagens
from menu_marca_dagua import exibir_menu_marca_dagua
from menu_converte_prn import exibir_menu_converte_prn

st.set_page_config(
    page_title='Utility Doc',
    page_icon=':page_facing_up:',
    layout='wide'
)


entradas_menu = {
    'Extrair páginas': 'file-earmark-pdf-fill',
    'Unir PDFs': 'plus-square-fill',
    'Reduzir tamanho PDF': 'file-earmark-zip-fill',
    'Imagem para PDF': 'file-earmark-richtext-fill',
    "Adicionar marca d'água": 'droplet-fill',
    "Converter .PRN para Word": 'file-earmark-arrow-up-fill',}

_ ,col2, _ = st.columns([0.1,0.6, 0.3])

with st.sidebar:
    st.image('utility-doc/images/logo.png', width=300)
  

    escolha = option_menu(
        menu_title=None,
        options=list(entradas_menu.keys()),
        icons=list(entradas_menu.values()),
        default_index=0,
        orientation='vertical',
        menu_icon="cast",
        key='menu',
        styles={
            "container": {"padding": "0!important", "background-color": "#f8f9fa", "border-radius": "10px"},
            "icon": {"color": "#1f355e", "font-size": "25px"},
            "nav-link": {"font-size": "18px", "text-align": "left", "margin": "5px", "--hover-color": "e3e3e3"},
            "nav-link-selected": {"background-color": "#e3e3e3", "color": "#333333", "border-radius": "2px"},  # Cinza claro
            "icon-selected": {"color": "#333333"},  # Cinza escuro
        }
    )

st.markdown(
    """
    <style>
    .stButton>button {
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: white;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)



with col2:
    match escolha:
        case 'Extrair páginas':
            exibir_menu_extrair(coluna=col2)
        case 'Reduzir tamanho PDF':
            exibir_menu_reduzir_pdf(coluna=col2)
        case 'Unir PDFs':
            exibir_menu_unir_pdf(coluna=col2)
        case 'Imagem para PDF':
            exibir_menu_imagens(coluna=col2)
        case "Adicionar marca d'água":
            exibir_menu_marca_dagua(coluna=col2)
        case "Converter .PRN para Word":
            exibir_menu_converte_prn(coluna=col2)
        case _:
            st.warning('Implementar página')