


import streamlit as st
import json

def menu():
    nome_arquivo = 'lista_de_cadastro.txt'
    cadastro_usuarios = []
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema']

    st.header('MENU PRINCIPAL')
    opcao = st.radio('Selecione uma opção:', opcoes)

    if opcao == 'Ver pessoas cadastradas':
        lista_cadastro(nome_arquivo)
    
    elif opcao == 'Cadastrar nova Pessoa':
        novo_cadastro(cadastro_usuarios, nome_arquivo)
    
    elif opcao == 'Sair do Sistema':
        st.success('Saindo do sistema...Até logo!')
        st.balloons()
def novo_cadastro(cadastro_usuarios, nome_arquivo):
    st.header('NOVO CADASTRO')
    nome = st.text_input('Nome:').title()
    idade = st.number_input('Idade:', min_value=0, max_value=150)
    
    if st.button('Cadastrar'):
        grava_usuario(nome, idade, nome_arquivo)
        
        try:
            with open('cadastro_cursoev.json', 'r') as arquivo:
                cadastro_usuarios = json.load(arquivo)
        except FileNotFoundError:
            cadastro_usuarios = []

        cadastro_usuarios.append({'Nome': nome, 'Idade': idade})
        with open('cadastro_cursoev.json', 'w') as arquivo:
            json.dump(cadastro_usuarios, arquivo)
        
        st.success('Cadastro efetuado com sucesso!')
        
def lista_cadastro(nome_arquivo):
    st.header('PESSOAS CADASTRADAS')
    cadastro = []
    try:
        with open(nome_arquivo, 'r') as arquivo: 
            for linha in arquivo:
                nome, idade = linha.strip().split(',')
                cadastro.append({'Nome': nome, 'Idade': idade})
        st.table(cadastro)
    except FileNotFoundError:
        st.warning(f'Lista sem pessoas cadastradas')

def grava_usuario(nome, idade, nome_arquivo):
    try:
        with open(nome_arquivo, 'a') as cadastro:
            cadastro.write(f'{nome}, {idade}\n')
    except FileNotFoundError:
        st.warning(f'arquivo {nome_arquivo} não foi criado. Criando novo arquivo!')
        with open(nome_arquivo, 'w') as cadastro:
            st.success(f'{nome_arquivo} criado com sucesso!')
if __name__ == '__main__':
    menu()
