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
fh = open("mitmh_collab_edges.txt",'wb')

for i in links:
    puzzle_url = f"https://devjoe.appspot.com/huntindex{i['href'][2:]}"
    puzzle_page = http.request('GET', puzzle_url)
    soup_puzzle = BeautifulSoup(puzzle_page.data, 'html.parser') 
    lines = soup_puzzle.find_all('p')
    for poss_line in lines:
        author_line = poss_line.text
        if author_line[:6] == "Author":
            authors = author_line.split(":")[1].split(",")
            for (author1, author2) in combinations(authors, 2):
                g.add_edge(author1[1:], author2[1:])
                print(f"{i['href']}:{author1}{author2}")
            break
print(g.edges())

nx.write_edgelist(g, fh, delimiter=",")
fh.close()
