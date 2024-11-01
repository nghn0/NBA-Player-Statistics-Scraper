import requests
from bs4 import BeautifulSoup

url = "https://www.nba.com/stats"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

table = soup.select(selector=".LeaderBoardWithButtons_lbwbCardWrapper__re1TJ")
table = table[0]


player_table = table.select(selector=".LeaderBoardPlayerCard_lbpcTable__q3iZD")


print("Find top 5 NBA players in \n31.Points Table\n2.Rebounds Table\n3.Assists\n4.Blocks Table\n5.Steals "
      "Table\n6.TurnOvers Table\n7.Three Pointers Made Table\n8.Free Throws Made Table\n9.Fantasy Points Table\n")
n = int(input("Enter your choice:"))

if 1 <= n <= len(player_table):
    player = player_table[n-1]
    player = player.select(selector="td a")
    for i in range(0,len(player),2):
        text = ""
        text = text + player[i].get_text()+'--'+player[i+1].get_text()
        print(text)
else:
    print("Invalid Number")
