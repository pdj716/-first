from urllib.request import urlopen
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import font_manager, rc

html=urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=")
soup=BeautifulSoup(html, "lxml")

city_name = soup.find_all('th', {'scope':'row'})
all_patient = soup.find_all('td', {'headers':'status_con s_type1'})
new_patient = soup.find_all('td', {'headers':'status_level l_type1'})