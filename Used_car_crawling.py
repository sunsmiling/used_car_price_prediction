from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import Series, DataFrame
import pandas as pd
import sys

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('|%s| %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben


def get_soup(url):
    html_doc = urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup


x = {'a': if }
x = {key: value for key, value in x.items() if value != 20}
x



#승용차
def my_car(pagenum):
    site="http://www.bobaedream.co.kr/cyber/CyberCar.php?refer_page=%2Fcyber%2FCyberCar.php&gubun=K&order=S11&view_size=50&search_cat=C3&search_cat_gubun=s0&search_field=car_name&view_stat=0&page="+str(pagenum)
    soup_wt=get_soup(site)
    info = []
    num_carth=len(soup_wt.find("table",class_="cyber").tbody.find_all("a",class_="sub"))
    for i in range(num_carth):
        soup_wt_detail = get_soup(str('http://www.bobaedream.co.kr')+soup_wt.find("table",class_="cyber").tbody.find_all("a",class_="sub")[i]['href'])
        sp_thing=soup_wt_detail.find("table",class_="specmiddle").tbody.find_all("td")
        s_thing = soup_wt_detail.find("div",class_="information").find_all("span",class_="s")
        td_thing=soup_wt_detail.find("table",class_="spectop").tbody.find_all("td")
        if soup_wt_detail.find("span",class_="fl").find_all("li")==[]:
            d_thing =0
            try:
                temp_dict = {}
                temp_dict = {'a_1.회사':soup_wt_detail.find("div",class_="tit").get_text().replace('\xa0\xa0\xa0','').split(None, 1)[0],
                             'a_2.모델명':soup_wt_detail.find("div",class_="tit").get_text().replace('\xa0\xa0\xa0','').split(None, 1)[1],
                             'b.sell_price(만원)':soup_wt_detail.find("div",class_="information").span.get_text().replace("만원",""),
                             'c.차량번호': s_thing[0].get_text(),
                             'd.연식(년월)': s_thing[1].get_text().replace('\xa0','').replace('년','').replace('월','').split("(")[0],
                             'e.주행거리(km)': s_thing[2].get_text().replace(",","").replace("km","").replace(" ",""),
                             'f.연료': s_thing[3].get_text().replace(",",""),
                             'g_1.배기량(cc)': s_thing[4].get_text().replace(" ","").replace(")","").split("(")[0].replace("cc",""),
                             'g_2.배기량(마력)': s_thing[4].get_text().replace(" ","").replace(")","").split("(")[1].replace("마력",""),
                             'h.변속기': s_thing[5].get_text().replace(",",""),
                             'i.색상': s_thing[6].get_text().replace(",","").replace(" ",""),
                             'j.사고유무': s_thing[7].get_text().replace('(사고이력조회)\n','').replace('\t',''),
                             'k.제조국':td_thing[0].get_text(),
                             'l.출시(년형)' : td_thing[1].get_text().split("/")[0].replace("년",""),
                             'm.신차가격(만원)' : td_thing[2].get_text().replace(',','').replace("만원",""),
                             'n.번호변경횟수' : "0",
                             'o.소유자변경횟수' : "0",
                             'p.보험사고이력(내차피해)_c' :  "0",
                             'q.보험사고이력(내차피해)_m' :  "0",
                             'r.보험사고이력(타차가해)_c' :  "0",
                             's.보험사고이력(타차가해)_m' :  "0",
                             't.연비(km/l)' : sp_thing[3].get_text().replace("km/ℓ",""),
                             'u.구동방식' : sp_thing[10].get_text().replace(" ",""),
                             'v.보디형식' : sp_thing[11].get_text(),
                             'w.변속기' : sp_thing[12].get_text()}     
                info.append(temp_dict)

            except:
                pass           
            
        else:
            
            d_thing = soup_wt_detail.find("span",class_="fl").find_all("li")

            try:
                temp_dict = {}
                temp_dict = {'a_1.회사':soup_wt_detail.find("div",class_="tit").get_text().replace('\xa0\xa0\xa0','').split(None, 1)[0],
                             'a_2.모델명':soup_wt_detail.find("div",class_="tit").get_text().replace('\xa0\xa0\xa0','').split(None, 1)[1],
                             'b.sell_price(만원)':soup_wt_detail.find("div",class_="information").span.get_text().replace("만원",""),
                             'c.차량번호': s_thing[0].get_text(),
                             'd.연식(년월)': s_thing[1].get_text().replace('\xa0','').replace('년','').replace('월','').split("(")[0],
                             'e.주행거리(km)': s_thing[2].get_text().replace(",","").replace("km","").replace(" ",""),
                             'f.연료': s_thing[3].get_text().replace(",",""),
                             'g_1.배기량(cc)': s_thing[4].get_text().replace(" ","").replace(")","").split("(")[0].replace("cc",""),
                             'g_2.배기량(마력)': s_thing[4].get_text().replace(" ","").replace(")","").split("(")[1].replace("마력",""),
                             'h.변속기': s_thing[5].get_text().replace(",",""),
                             'i.색상': s_thing[6].get_text().replace(",","").replace(" ",""),
                             'j.사고유무': s_thing[7].get_text().replace('(사고이력조회)\n','').replace('\t',''),
                             'k.제조국':td_thing[0].get_text(),
                             'l.출시(년형)' : td_thing[1].get_text().split("/")[0].replace("년",""),
                             'm.신차가격(만원)' : td_thing[2].get_text().replace(',','').replace("만원",""),
                             'n.번호변경횟수' : d_thing[2].get_text().split(":")[1].replace(" ","").replace("회","").split("/")[0],
                             'o.소유자변경횟수' : d_thing[2].get_text().split(":")[1].replace(" ","").replace("회","").split("/")[1],
                             'p.보험사고이력(내차피해)_c' :  d_thing[4].get_text().replace(" ","").replace("보험사고이력(내차피해):","").split("회")[0],
                             'q.보험사고이력(내차피해)_m' :  d_thing[4].get_text().replace(" ","").replace("보험사고이력(내차피해):","").split("회")[1].replace(",","").replace("원",""),
                             'r.보험사고이력(타차가해)_c' :  d_thing[5].get_text().replace(" ","").replace("보험사고이력(타차가해):","").split("회")[0],
                             's.보험사고이력(타차가해)_m' :  d_thing[5].get_text().replace(" ","").replace("보험사고이력(타차가해):","").split("회")[1].replace(",","").replace("원",""),
                             't.연비(km/l)' : sp_thing[3].get_text().replace("km/ℓ",""),
                             'u.구동방식' : sp_thing[10].get_text().replace(" ",""),
                             'v.보디형식' : sp_thing[11].get_text(),
                             'w.변속기' : sp_thing[12].get_text()}     
                info.append(temp_dict)

            except:
                pass
        
 
    return DataFrame(info)


def concatthing(totpage):
    appended_data = []
    for k in range(totpage):
        try:
            progress(k+1,totpage,suffix='crawling car page')
            dfpg=my_car(k+1)
            appended_data.append(dfpg)
        
        except:
            pass
        
    appended_data = pd.concat(appended_data).reset_index(drop=True)
    
    return appended_data
        


used_car=concatthing(14)


used_car.to_csv('used_car_sago.csv',index=False)

