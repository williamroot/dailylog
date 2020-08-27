import streamlit as st


def write():
    logo = 'https://i.imgur.com/WudeOYV.gif'
    style_logo = 'display:block; margin-left:auto; margin-right:auto'
    st.markdown(
        f"<img src='{logo}' style='{style_logo}' />",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h2 align=center>ÁBACO</h2>" +
        "<p align=center>" +
        "Repositório de painéis interativos do Jornalismo da Rede Globo" +
        "</p>" +
        "<p align=center style='font-size:smaller;'>" +
        "Produzido pela Equipe de Soluções do CoE Analytics" +
        "</p>"
        "<p align=center style='font-size:smaller;'>" +
        "Versão 0.1" +
        "</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    write()
