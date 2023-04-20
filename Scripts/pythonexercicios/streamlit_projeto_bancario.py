import streamlit as st
from funcoes_bancaria import deposito

# Define uma lista de tuplas com os itens do menu
menu_items = [    (1, "Depositar"),    (2, "Sacar"),    (3, "Extrato"),    (4, "Cadastrar usuário"),    (5, "Cadastrar Conta Bancária"),    (6, "Listar usuários"),    (7, "Listar Contas"),    (8, "Exclui usuário"),    (0, "Sair")]

# Configura a imagem do título
st.image("../pythonexercicios/brazao_familia_Carvalho.webp", use_column_width="auto")

# Estilo do título
title_html = "<h2 style='text-align: center; color: #F5D300;'><b>⭐ Bem vindo ao Banco MMC ⭐</b></h2>"
st.write(title_html, unsafe_allow_html=True)

# Exibe o menu
title_html = "<h3 style='text-align: center; color: #1A237E;'><b>==========================</b></h3>"
st.write(title_html, unsafe_allow_html=True)

# Divide a tela em duas colunas
col1, col2 = st.columns(2)

# Insere os botões em cada coluna
for item in menu_items[:len(menu_items)//2]:
    if col1.button(f"[:blue[**{item[0]}**]] {item[1]}", key=item[0], use_container_width=True):
        # Lógica para lidar com o item selecionado
        st.write("========================================================================================")
        st.write(f"Você selecionou a opção {item[0]} - {item[1]}")
        if item[0] == 1:
             saldo = 0
             relacao_depositos = ''
             deposito(saldo, relacao_depositos)
       

for item in menu_items[len(menu_items)//2:]:
    if col2.button(f"[:blue[**{item[0]}**]] {item[1]}", key=item[0], use_container_width=True):
        # Lógica para lidar com o item selecionado
        st.write("========================================================================================")
        st.write(f"Você selecionou a opção: {item[0]} - {item[1]}")


if st.button("Click Here") is True:
       st.write('Great')

#Usando o markdown
# Exibe um título de primeiro nível
st.write("# Título de primeiro nível")

# Exibe um título de segundo nível
st.write("## Título de segundo nível")

# Exibe um texto em negrito
st.write("Este é um texto **negrito**")

# Exibe um texto em itálico
st.write("Este é um texto *itálico*")

# Exibe uma lista com marcadores
st.write("- Item 1\n- Item 2\n- Item 3")

# Exibe uma tabela
st.write("| Coluna 1 | Coluna 2 | Coluna 3 |\n| --- | --- | --- |\n| Dado 1 | Dado 2 | Dado 3 |")

# Exibe uma imagem com uma descrição
st.markdown("![Descrição da imagem](../pythonexercicios/brazao_familia_Carvalho.webp)")

st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
