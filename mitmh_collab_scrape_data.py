import urllib3
from bs4 import BeautifulSoup
import networkx as nx
from itertools import combinations 
import matplotlib.pyplot as plt

http = urllib3.PoolManager()
main_page = http.request('GET', 'https://devjoe.appspot.com/huntindex/index/puzzles.html')
soup = BeautifulSoup(main_page.data, 'html.parser')
links = soup.find_all('a')[2:-1]

g = nx.Graph()
fh = open("mitmh_collab_edges2.txt",'wb')

for i in links:
    puzzle_url = f"https://devjoe.appspot.com/huntindex{i['href'][2:]}"
    puzzle_page = http.request('GET', puzzle_url)
    soup_puzzle = BeautifulSoup(puzzle_page.data, 'html.parser') 
    puzzle_name = soup_puzzle.find('h2').text
    lines = soup_puzzle.find_all('p')
    for poss_line in lines:
        poss_line_text = poss_line.text
        if poss_line_text[:4] == "Hunt":
            hunt_name = poss_line_text.split(":")[1][1:-1]
        elif poss_line_text[:6] == "Author":
            authors = poss_line_text.split(":")[1].split(",")
            for (author1, author2) in combinations(authors, 2):
                g.add_edge(author1[1:], author2[1:], puzzle_name=puzzle_name, hunt_name=hunt_name)
                print(f"{i['href']}:{author1}{author2}")
            break
        # TODO Extract keywords
print(g.edges())

nx.write_edgelist(g, fh, delimiter=",")
fh.close()
