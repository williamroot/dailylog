import streamlit as st
from core import utils
import apps.home

utils.set_logging_format()

# Customização de CSS: onde se sobrescrevem partes do stylesheet original
HTML = """
  <style>
    header .decoration {
        display: none;
    }
    header > .toolbar {
        display: none;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(180deg,#dbdbdb,#dbdbdb);
    }
    .reportview-container .main {
        background-color: #f6f7f8;
    }
    footer {
        display: none;
    }
  </style>
"""
st.markdown(HTML, unsafe_allow_html=True)

# Listagem de páginas: onde se indicam as páginas do portal
PAGES = {
    "Início": apps.home
}


def main():
    """
    Constrói a barra de navegação com os elementos de `PAGE` e
    chama a função `utils.write_page()`, que renderiza a página
    selecionada
    """
    st.sidebar.markdown("<h3>Navegação</h3>", unsafe_allow_html=True)
    selection = st.sidebar.selectbox("Selecione uma página", list(PAGES.keys()))
    page = PAGES[selection]

    with st.spinner(f"Carregando {selection}..."):
        utils.write_page(page)


if __name__ == "__main__":
    main()
