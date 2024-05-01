from github import Github

acess_token = "your_github_access_token"

g = Github(acess_token)
   
current_user = g.get_user()
print (current_user.name)
print(current_user.email)

# repos = g.get_user().get_repos()

# for repo in repos:
#     print (repo.name)
    
rdf_repos = g.search_repositories(query="language:xml stars:>=100")

for repo in rdf_repos:
    print (repo.name) 
    
