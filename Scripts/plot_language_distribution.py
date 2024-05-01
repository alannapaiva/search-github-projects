# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from github import Github

def plot_language_distribution(queries, access_token):
    languages = []
    project_counts = []
    
    # Definir lista de consultas para buscar projetos nas linguagens desejadas
    queries = ['language:xml stars:>100', 'language:rdf stars:>100', 'language:owl stars:>100', 'language:sparql stars:>100']
    
    # Definir token de acesso ao GitHub
    access_token = "your_github_access_token"
    # Para cada consulta, buscar projetos e contar a quantidade de projetos encontrados
    for query in queries:
        # Extrair o nome da linguagem da consulta
        language = query.split(':')[1].split()[0].strip()
        languages.append(language)

        # Fazer a busca de projetos
        g = Github(access_token)
        search_results = g.search_repositories(query)

        # Quantidade de projetos encontrados
        num_projects = search_results.totalCount
        project_counts.append(num_projects)

    # Criar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(languages, project_counts, color='skyblue')
    plt.title('Quantidade de Projetos por Linguagens da Web Semantiica')
    plt.xlabel('Linguagem')
    plt.ylabel('Quantidade de Projetos')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()


    # Gerar e exibir o gráfico
    plot_language_distribution(queries, access_token)