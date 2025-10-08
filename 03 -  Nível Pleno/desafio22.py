#**Contador de Frequência de Palavras:** Crie um programa que leia um arquivo de texto (.txt) 
# e conte a frequência de cada palavra, exibindo as mais comuns.

from collections import Counter
import re 

def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo.lower())
        total_palavras = len(palavras)
        frequencia = Counter(palavras)

        print(f"\n--- Análise de '{nome_arquivo}' ---")
        print(f"Total de palavras no arquivo: {total_palavras}")
        print("\nTop palavras mais frequentes:")
        for palavra, contagem in frequencia.most_common(20):
            if len(palavra) >2:
                print(f"- '{palavra}': {contagem} vezes")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    contar_palavras('../README.md')
    contar_palavras('texto_desafio22.txt')

if __name__ == '__main__':
    main()