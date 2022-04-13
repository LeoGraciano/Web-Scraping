import requests
from bs4 import BeautifulSoup


url = "https://pt.stackoverflow.com/questions/tagged/python"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for question in html.select('.s-post-summary'):
    title = question.select_one('.s-link')
    date = question.select_one('.relativetime')
    vote = question.select_one('.s-post-summary--stats-item-number')

    print(f"Voto: {vote.text}", f"Titulo: {title.text}",
          f"Publicado {date['title']}", sep="\t")
