
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests


# In[2]:


CidadesPesquisa = ['Bauru, São Paulo, Brasil', 'Ribeirão Preto, São Paulo, Brasil', 'Lençóis Paulista']

#Browser Visible
driver = webdriver.Chrome(executable_path="C:/Users/Avell 1555 IRON/chromedriver_win32/chromedriver")
url = 'https://weather.com/pt-BR/clima/10dias/l/BRMG0645:1:BR';
driver.get(url)

for cidade in CidadesPesquisa:
    txtName = cidade + ".txt";
    f = open(txtName,"w+")
    print("Cidade escolhida: ", cidade)
    #tabTemp = driver.find_elements(By.CSS_SELECTOR, ".clickable.closed")[0].click()
    fieldSearch = driver.find_element(By.CSS_SELECTOR, ".theme__inputElement__4bZUj.input__inputElement__1GjGE")
    time.sleep(5);
    fieldSearch.send_keys(cidade)
    time.sleep(3)
    fieldClicked = driver.find_element(By.CSS_SELECTOR, ".styles__item__3sdr8.styles__selected__SEH0e")
    time.sleep(2)
    fieldClicked.click()
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find('table', attrs={'class':'twc-table'})
    data = []
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
     cols = row.find_all('td')
     cols = [ele.text.strip() for ele in cols]
     data.append([ele for ele in cols if ele])
     info = [ele for ele in cols if ele]
     post = {
     "Dia" : info[0],
     "Descrição" : info[1],
     "Max/Min" : info[2],
     "Precipitação" : info[3],
     "Vento" : info[4],
     "Umidade" : info[5]
     }
     txtLine = "Dia: " + info[0] + " Descrição: " + info[1] + " Max/Min: " + info[2] + " Precipitação: " + info[3] + " Vento: " + info[4] + " Umidade: " + info[5]
     txtLine += "\n"
     f.write(txtLine)
     f.write("---------------\n")
     print(post)
    
     print("---------------")

