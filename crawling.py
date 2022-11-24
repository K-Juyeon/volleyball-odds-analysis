import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = selenium.webdriver.Chrome('./chromedriver/chromedriver')

for i in range(1, 19):
    if i < 10:
        page_name = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season=00' + str(i)
    else:
        page_name = 'https://www.kovo.co.kr/game/v-league/11110_schedule_list.asp?season=0' + str(i)

    driver.get(page_name)

    WebDriverWait(driver, 5)
    time.sleep(0.5)

    print()
    select = Select(driver.find_element(By.CSS_SELECTOR, "#wrp_content > article > div.wrp_date > form > fieldset > select.selectbox_table.w120.selectBox"))
    try :
        for j in range(2, len(select.options) + 1):
            select_option = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article > div.wrp_date > form > fieldset > select.selectbox_table.w120.selectBox > option:nth-child(" + str(j) + ")").get_attribute("value")
            page_name_new = page_name + "&team=&yymm=" + select_option + "&r_round="
            driver.get(page_name_new)
            table = driver.find_element(By.XPATH, "//*[@id='type1']/div/table/tbody")
            tr = table.find_elements(By.TAG_NAME, "tr")

            # 여자 경기인지 판단
            for k in range(1, len(tr) + 1) :
                time.sleep(0.2)
                gender = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td:nth-child(3)").get_attribute("innerText")
                if (gender == "여자") :
                    # 흥국생명의 경기인지 판단
                    left = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td.tleft").get_attribute("innerText")
                    right = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td.tright").get_attribute("innerText")
                    if "흥국생명" in left or "흥국생명" in right :
                        # 상세결과에 들어가서 데이터 가져오기
                        driver.find_element(By.CSS_SELECTOR,"#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td:nth-child(10) > a").click()

                        time = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(3) > table > tbody > tr.last > td:nth-child(7)").get_attribute("innerText")

                        h_team =  driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td.first.team > p.match > span.team").get_attribute("innerText")
                        h_score = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(2) > p.num").get_attribute("innerText")
                        h_attack = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(1) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_block = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(2) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_serve = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(3) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_miss = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(4) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_all = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(5) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_dig = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(6) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_recieve = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(7) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_set = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(8) > dd.chart.clearfix.on > div.bar.c1.left > span").get_attribute("innerText")
                        h_attackpercent = driver.find_element((By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.r.w470 > div > div.con.compare2.clearfix > div.chart.left.on > div.bar.c1 > span > span > span")).get_attribute("innerText")
                        h_recievepercent = driver.find_element((By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.r.w470 > div > div.con.compare2.clearfix > div.chart.right.on > div.bar.c1 > span > span > span")).get_attribute("innerText")

                        a_team = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td.first.team > p.match > span.team").get_attribute("innerText")
                        a_score = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(4) > p.num").get_attribute("innerText")
                        a_attack = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(1) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_block = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(2) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_serve = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(3) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_miss = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(4) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_all = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(5) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_dig = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(6) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_recieve = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(7) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_set = driver.find_element(By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.l.w470 > div > div > dl:nth-child(8) > dd.chart.clearfix.on > div.bar.c2.right > span").get_attribute("innerText")
                        a_attackpercent = driver.find_element((By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.r.w470 > div > div.con.compare2.clearfix > div.chart.left.on > div.bar.c2 > span > span > span")).get_attribute("innerText")
                        a_recievepercent = driver.find_element((By.CSS_SELECTOR, "#tab1 > div.scrollfit.clearfix > div.fitcon.r.w470 > div > div.con.compare2.clearfix > div.chart.right.on > div.bar.c2 > span > span > span")).get_attribute("innerText")

                        # 선수 기록 페이지
                        driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_tab.mt60 > ul > li:nth-child(2) > a").click()

                        h_teamcheck = driver.find_element((By.CSS_SELECTOR, "#tab2 > div.wrp_tab > ul > li.first.w480.wrp_rounded.on > a")).get_attribute("innerText")

                        if "흥국생명" in h_teamcheck :
                            driver.find_element((By.CSS_SELECTOR, "#tab2 > div.wrp_tab > ul > li.first.w480.wrp_rounded.on > a")).click()
                            table = driver.find_element(By.XPATH, "//*[@id='team1']/div/div[2]/table[1]/tbody")
                            tr = table.find_elements(By.TAG_NAME, "tr")
                        else :
                            driver.find_element((By.CSS_SELECTOR, "#tab2 > div.wrp_tab > ul > li.last.w480.wrp_rounded > a")).click()
                            table = driver.find_element(By.XPATH, "//*[@id='team2']/div/div[2]/table[1]/tbody")
                            tr = table.find_elements(By.TAG_NAME, "tr")

                        for n in range(1, len(tr) + 1):
                            kim_check = driver.find_element((By.CSS_SELECTOR, "#team2 > div > div.wrp_lst > table.lst_board.lst_fixed.w123 > tbody > tr:nth-child(" + str(n) + ") > td.name")).get_attribute("innerText")
                            if "김연경" in kim_check :
                                for m in range(1, 6) :
                                    starting_check = driver.find_element((By.CSS_SELECTOR, "#team2 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(m) + ") > td:nth-child(1) > span")).get_attribute("class")
                                    if starting_check == "starting" :
                                        starting = "선발"
                                        break;
                                    elif starting_check == "switch" :
                                        starting = str(m) + "세트 교체"
                                        break;

    except NoSuchElementException as e:
        print(e)

driver.quit()  # driver 종료