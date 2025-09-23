# Intensivo de Python: 50 Desafios Práticos

Este documento contém uma lista curada de 50 desafios de programação em Python criados pelo Gemmini Pro, organizados por nível de dificuldade para guiar seu aprendizado de forma progressiva.

## 🔰 Nível Iniciante (Dia 1-10)

**Foco:** Sintaxe básica, variáveis, tipos de dados e operadores.

1. **Olá, Mundo!:** Escreva um programa que imprima "Olá, Mundo!" na tela.
2. **Soma Simples:** Crie um programa que solicite dois números ao usuário e mostre a soma deles.
3. **Conversor de Unidades (Metros para Centímetros):** Peça ao usuário um valor em metros e converta-o para centímetros.
4. **Calculadora de Idade:** Pergunte o ano de nascimento do usuário e calcule a idade aproximada dele.
5. **Concatenação de Strings:** Solicite o nome e o sobrenome do usuário e exiba uma mensagem de boas-vindas com o nome completo.
6. **Verificador de Número Par ou Ímpar:** Crie um programa que receba um número inteiro e diga se ele é par ou ímpar.
7. **Cálculo de Média:** Peça ao usuário para inserir três notas e calcule a média aritmética.
8. **Manipulação de Strings (Maiúsculas e Minúsculas):** Receba uma palavra do usuário e imprima-a em maiúsculas e minúsculas.
9. **Operações Matemáticas:** Peça dois números e exiba o resultado da soma, subtração, multiplicação e divisão.
10. **Calculadora de Área de um Quadrado:** Solicite o lado de um quadrado e calcule sua área e seu perímetro.

## 🔷 Nível Júnior (Dia 11-21)

**Foco:** Estruturas de controle (if/else, loops), listas, dicionários e funções básicas.

11. **Tabuada de Multiplicação:** Peça um número ao usuário e exiba a tabuada de multiplicação desse número de 1 a 10.
12. **Contador de Vogais:** Crie um programa que conte o número de vogais em uma string fornecida pelo usuário.
13. **Inversor de Palavras:** Escreva uma função que receba uma string e a retorne invertida. Ex: "python" -> "nohtyp".
14. **Lista de Compras:** Crie um programa que permita ao usuário adicionar e remover itens de uma lista de compras. Ao final, exiba a lista completa.
15. **Verificador de Palíndromo:** Desenvolva um programa que verifique se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente).
16. **Encontrando o Maior Número:** Escreva uma função que receba uma lista de números e retorne o maior valor.
17. **Agenda de Contatos Simples:** Crie um dicionário para armazenar nomes e números de telefone. Permita que o usuário adicione e procure por contatos.
18. **Sequência de Fibonacci:** Gere os primeiros N números da sequência de Fibonacci, onde N é informado pelo usuário.
19. **Adivinhe o Número:** Crie um jogo simples onde o computador "pensa" em um número entre 1 e 100, e o usuário tem que adivinhar. O programa deve dar dicas (maior/menor).
20. **Função de Fatorial:** Escreva uma função que calcule o fatorial de um número inteiro não negativo.
21. **Filtrando Números Pares:** Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.

# 🔶 Nível Pleno (Dia 22-32)

**Foco:** Funções avançadas (args, kwargs), manipulação de arquivos, list comprehensions e introdução à Orientação a Objetos (POO).

22. **Contador de Frequência de Palavras:** Crie um programa que leia um arquivo de texto (.txt) e conte a frequência de cada palavra, exibindo as mais comuns.
23. **List Comprehension para Múltiplos:** Use list comprehension para criar uma lista de todos os números entre 1 e 100 que são divisíveis por 7.
24. **Calculadora com Funções:** Refatore a calculadora do nível iniciante usando funções separadas para cada operação (soma, subtração, etc.).
25. **Gerador de Senhas Aleatórias:** Crie uma função que gere uma senha aleatória com um comprimento específico, contendo letras maiúsculas, minúsculas, números e símbolos.
26. **Classe Carro:** Crie uma classe chamada Carro com os atributos marca, modelo e ano. Adicione métodos para ligar(), desligar() e acelerar().
27. **Manipulação de JSON:** Crie um programa que leia um arquivo JSON contendo dados de usuários e permita buscar um usuário por email.
28. **Função com** * **args:** Escreva uma função soma_ilimitada que aceite um número indefinido de argumentos numéricos e retorne a soma de todos eles.
29. **Herança em POO:** Crie uma classe Veiculo com atributos e métodos genéricos. Em seguida, crie as classes Carro e Moto que herdem de Veiculo e adicionem seus próprios atributos e métodos.
30. **Lambda para Ordenação:** Use uma função lambda para ordenar uma lista de dicionários com base no valor de uma chave específica (ex: ordenar por 'idade').
31. **Validador de CPF (Formato):** Crie uma função que verifique se uma string de CPF está no formato correto (XXX.XXX.XXX-XX) usando manipulação de strings.
32. **Logger Simples:** Crie um programa que escreva mensagens de log (com data e hora) em um arquivo log.txt cada vez que uma determinada função for chamada.

🔥 Nível Sênior (Dia 33-43)

**Foco:** POO avançado, tratamento de exceções, decoradores, geradores e módulos/bibliotecas.

33. **Decorador de Tempo de Execução:** Crie um decorador que meça o tempo de execução de uma função e imprima o resultado.
34. **Tratamento de Exceções:** Modifique o programa de "Soma Simples" (questão 2) para garantir que ele não quebre se o usuário digitar um valor não numérico, usando try e except.
35. **Gerador de Sequência de Fibonacci:** Implemente a sequência de Fibonacci usando um gerador (yield) para otimizar o uso de memória.
36. **Context Manager para Arquivos:** Crie um gerenciador de contexto (with open(...)) personalizado usando uma classe com os métodos __enter__ e __exit__.
37. **Consumo de API:** Escreva um script que faça uma requisição a uma API pública (ex: API de cotação de moedas ou de previsão do tempo) e exiba os dados de forma legível.
38. **Validador de CPF (Algoritmo):** Aprimore o validador de CPF (questão 31) para verificar se os dígitos verificadores são válidos de acordo com o algoritmo oficial.
39. **Expressões Regulares (Regex):** Crie uma função que use expressões regulares para extrair todos os endereços de e-mail de um bloco de texto.
40. **Programação Assíncrona (asyncio):** Escreva um script simples usando asyncio e aiohttp para fazer o download de múltiplas páginas da web de forma concorrente.
41. **Metaclasses:** Crie uma metaclasse que garanta que qualquer classe que a utilize tenha certos métodos obrigatórios implementados.
42. **Polimorfismo em Ação:** Crie um sistema onde diferentes classes (ex: Cachorro, Gato) herdam de uma classe Animal e implementam um método fazer_som() de maneiras diferentes.
43. **Interface de Linha de Comando (CLI):** Usando a biblioteca argparse ou click, crie uma ferramenta de linha de comando que execute uma das funcionalidades que você já criou (ex: gerador de senhas).

## 🚀 Projetos para Portfólio (Dia 44-50)

**Foco:** Aplicação prática e integrada de conhecimentos para criar soluções completas.

44. **Web Scraper de Notícias:** Desenvolva um web scraper usando BeautifulSoup e Requests para extrair os títulos e links das principais notícias de um portal de sua escolha e salvar os resultados em um arquivo CSV.
45. **API REST com Flask/Django:** Crie uma API REST simples para gerenciar uma lista de tarefas (CRUD - Create, Read, Update, Delete). A API deve ter endpoints para listar todas as tarefas, adicionar uma nova, atualizar e deletar.
46. **Bot para Discord/Telegram:** Desenvolva um bot que responda a comandos básicos. Por exemplo, um comando !cotação dolar que busca a cotação atual usando uma API e responde no chat.
47. **Analisador de Dados Financeiros:** Utilize a biblioteca Pandas e Matplotlib para ler um arquivo CSV com dados históricos de ações (ex: PETR4.SA), calcular a média móvel e gerar um gráfico simples da evolução do preço de fechamento.
48. **Aplicação de Lista de Tarefas (To-Do List) com Interface Gráfica:** Crie um aplicativo de desktop com uma interface gráfica (usando Tkinter ou PyQt) que permita ao usuário gerenciar suas tarefas diárias.
49. **Automatizador de Tarefas com Selenium:** Crie um script que automatize uma tarefa repetitiva na web, como preencher um formulário de login ou baixar relatórios de um sistema web.
50. **Blog Simples com Banco de Dados:** Desenvolva uma aplicação web completa de um blog usando um framework como Django ou Flask. A aplicação deve permitir criar, editar e deletar posts, além de ter um sistema de comentários e armazenamento em um banco de dados (SQLite ou PostgreSQL).

## 💻 Como Utilizar Este Repositório

Clonar o repositório:

```Bash
git clone https://github.com/selrahcsan/50-dias-de-Python.git
```

Navegue até o diretório:

```Bash
cd 50-dias-de-Python
```

## 🤔 Escolha um desafio e comece a codificar!
Crie um arquivo Python para cada solução (ex: *desafio_01.py, desafio_02.py*).

## Tente resolver o problema sozinho antes de procurar por soluções. A dificuldade faz parte do aprendizado!

##  😎 Teste e refatore seu código:

Após chegar a uma solução, revise seu código. Ele está legível? Pode ser mais eficiente? Há casos extremos que não foram tratados?

## 📝 Use Git para salvar seu progresso:

Faça commits regulares das suas soluções. Isso é uma ótima prática para se acostumar com o fluxo de trabalho de desenvolvimento.

```Bash
git add .
git commit -m "Solução para o desafio 05: Verificador de Palíndromo"
```

🛠️ Ferramentas e Conceitos Abordados


🤝 Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender e criar. Qualquer contribuição que você fizer será muito apreciada.

* Faça um Fork do projeto.
* Crie uma Branch para sua feature (git checkout -b feature/NovaFeature).
* Faça o Commit de suas alterações (git commit -m 'Adiciona NovaFeature').
* Faça o Push para a Branch (git push origin feature/NovaFeature).
* Abra um Pull Request.

## 😌 Sugestões de contribuição

* Correção de erros de digitação.
* Sugestão de novos desafios.
* Melhora na descrição dos desafios existentes.

## 📄 Licença

Distribuído sob a licença GPL-3.0 license.
Veja LICENSE para mais informações.
