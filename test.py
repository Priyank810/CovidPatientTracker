import json
import requests
from bs4 import BeautifulSoup
import schedule
import time


def scrapper():
    URL = "https://www.mohfw.gov.in/"

    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html5lib')

    table = soup.find('div' , attrs={'class':'newtab'})
    table_rows = table.find_all('tr')

    d = {}
    m_list = []
    m_dict = {}

    with open('data.json', 'r') as openfile:
        dd = json.load(openfile)

    c = 0
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text.replace('\n        ', '').replace('#','').replace('*' , '') for i in td]
        for j in range(len(row)):
            if (c != 0):
                d[j] = row[j]

        if (c != 0):
            m_list.append(d.copy())
        c = c + 1

    for i in range(len(m_list)):
        m_dict[i] = m_list[i]

    # temp1 = json.dumps(m_dict)
    # temp2 = json.load(temp1)

    # print(dd)

    for i in range(22):
        s = str(i)
        if (dd[s]["2"] == m_dict[i][2]):
            print(dd[s]["1"])
            print(dd[s]["2"])
            print(m_dict[i][1])
            print(m_dict[i][2])
            print('No Change')
            print("--------------------------")
        else:
            print(dd[s]["1"])
            print(dd[s]["2"])
            print(m_dict[i][1])
            print(m_dict[i][2])
            print('Change : '+ str(int(m_dict[i][2])-int(dd[s]["2"])))
            print("--------------------------")

    print(dd['23']['1'])
    print(m_dict[23][1])
    m_dict[24] = str(time.ctime())
    xx = json.dumps(m_dict)
    print(time.ctime())
    with open("data.json", "w") as outfile:
        outfile.write(xx)

    print("--------------------------------------------------------------------------------------")
#schedule.every(1).minutes.do(scrapper)
'''
while True:
    schedule.run_pending()
    time.sleep(1)

'''
scrapper()