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

city_name_list = []
for a in soup.find_all('th', {'scope':'row'}):
    city_name_list.append(a.get_text())

all_patient_list = []
for a in soup.find_all('td', {'headers':'status_con s_type1'}):
    all_patient_list.append(a.get_text())

new_patient_list = []
for a in soup.find_all('td', {'headers':'status_level l_type1'}):
    new_patient_list.append(a.get_text())

import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
font_location = 'C:/Windows/Fonts/H2GTRM.ttf'
font_name = fm.FontProperties(fname = font_location).get_name()
mpl.rc('font', family = font_name)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
plt.bar(x, new_patient_list)
plt.xticks(x, city_name_list)
plt.suptitle('전국 일일 확진자 수')
plt.show()

x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.bar(x,all_patient_list)
plt.xticks(x,city_name_list,rotation='vertical')
plt.show()

for i in all_patient_list:
    i_1=i.replace(',','')
    all_patient_list.append(i_1)
    del all_patient_list[0]

all_patient_list = [int (i) for i in all_patient_list]
new_patient_list = [int (i) for i in new_patient_list]


x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
plt.bar(x,all_patient_list)
plt.xticks(x,city_name_list,rotation='vertical')
plt.show()