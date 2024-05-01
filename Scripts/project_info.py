from github import Github
import pandas as pd 
import matplotlib.pyplot as plt

acess_token = "your_github_access_token"
    
def extract_project_info():
    df_project = pd.DataFrame()
    
    # Lista de consultas para buscar projetos nas linguagens desejadas
    queries = ['language:xml stars:>100', 'language:rdf stars:>100', 'language:owl stars:>100', 'language:sparql stars:>100']
    
    for query in queries:
        g = Github(acess_token)
        search_results = g.search_repositories(query)
        
        # Quantidade de projetos encontrados para a consulta atual
        num_projects = search_results.totalCount
        print("Quantidade de projetos encontrados para a linguagem '{}': {}".format(query.split(':')[1], num_projects))
        
        for repo in search_results:
            PRs = repo.get_pulls(state='all')
        
            df_project = df_project.append({
                'Project_ID': repo.id,
                'Name': repo.name,
                'Full_Name': repo.full_name,
                'Language': repo.language,
                'Forks': repo.forks_count,
                'Stars': repo.stargazers_count,
                'Watchers': repo.watchers_count,
                'PRs_count': PRs.totalCount
            }, ignore_index=True)
        
    df_project.to_csv('./Dataset/project_dataset.csv', sep=',', encoding='utf-8', index=True)

    extract_project_info()