import csv
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

    select = Select(driver.find_element(By.CSS_SELECTOR, "#wrp_content > article > div.wrp_date > form > fieldset > select.selectbox_table.w120.selectBox"))

    try :
        f = open('volleyball.csv', 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(['상대팀', '공격득점', '블로킹득점', '서브득점', '팀범실', '상대범실', '전체득점', '상대득점', '디그성공', '리시브정확', '세트성공', '공격성공률', '리시브효율', '경기시간', '세트승', '세트패', '결과', '김연경', '김연경득점', '김연경시도', '김연경성공', '김연경공격차단', '김연경범실', '김연경성공률', '김연경점유율'])
        for j in range(2, len(select.options) + 1):
            select_option = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article > div.wrp_date > form > fieldset > select.selectbox_table.w120.selectBox > option:nth-child(" + str(j) + ")").get_attribute("value")
            page_name_new = page_name + "&team=&yymm=" + select_option + "&r_round="
            driver.get(page_name_new)
            table = driver.find_element(By.XPATH, "//*[@id='type1']/div/table/tbody")
            tr = table.find_elements(By.TAG_NAME, "tr")

            # 여자 경기인지 판단
            for k in range(1, len(tr) + 1):
                gender = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td:nth-child(3)").get_attribute("innerText")
                if (gender == "여자"):
                    # 흥국생명의 경기인지 판단
                    left = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td.tleft").get_attribute("innerText")
                    right = driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td.tright").get_attribute("innerText")
                    if "흥국생명" in left or "흥국생명" in right:
                        # 상세결과의 데이터 가져오기
                        if i < 10 :
                            driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td:nth-child(10) > a").click()
                        else :
                            driver.find_element(By.CSS_SELECTOR, "#type1 > div > table > tbody > tr:nth-child(" + str(k) + ") > td:nth-child(10) > a.btn.btn_lst.wrp_rounded.w82.btn_grey").click()

                        game_time_array = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(3) > table > tbody > tr.last > td:nth-child(7)").get_attribute("innerText").rstrip("m").split("h")
                        game_time = 60 * int(game_time_array[0]) + int(game_time_array[1])

                        h_team = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td.first.team > p.match > span.team").get_attribute("innerText")
                        h_score = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(2) > p.num").get_attribute("innerText")
                        h_attack = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[1]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_block = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[2]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_serve = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[3]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_miss = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[4]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_all = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[5]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_dig = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[6]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_recieve = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[7]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_set = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[8]/dd[1]/div[1]/span").get_attribute("innerText")
                        h_attackpercent = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[2]/div/div[1]/div[1]/div[1]/span/span/span").get_attribute("innerText").rstrip("%")
                        h_recievepercent = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[2]/div/div[1]/div[2]/div[1]/span/span/span").get_attribute("innerText").rstrip("%")

                        a_team = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td.first.team > p.match > span.team").get_attribute("innerText")
                        a_score = driver.find_element(By.CSS_SELECTOR, "#wrp_content > article.wrp_recentgame.wrp_result > table > tbody > tr > td:nth-child(4) > p.num").get_attribute("innerText")
                        a_attack = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[1]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_block = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[2]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_serve = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[3]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_miss = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[4]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_all = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[5]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_dig = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[6]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_recieve = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[7]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_set = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[1]/div/div/dl[8]/dd[1]/div[2]/span").get_attribute("innerText")
                        a_attackpercent = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[2]/div/div[1]/div[1]/div[2]/span/span/span").get_attribute("innerText").rstrip("%")
                        a_recievepercent = driver.find_element(By.XPATH, "//*[@id='tab1']/div[1]/div[2]/div/div[1]/div[2]/div[2]/span/span/span").get_attribute("innerText").rstrip("%")

                        # 선수 기록 페이지
                        driver.find_element(By.XPATH, "//*[@id='wrp_content']/article[2]/ul/li[2]/a").click()

                        if "흥국생명" in h_team :
                            driver.find_element(By.XPATH, "//*[@id='tab2']/div[1]/ul/li[1]/a").click()
                        else :
                            driver.find_element(By.XPATH, "//*[@id='tab2']/div[1]/ul/li[2]/a").click()

                        table = driver.find_element(By.XPATH, "//*[@id='team2']/div/div[2]/table[1]/tbody")
                        tr = table.find_elements(By.TAG_NAME, "tr")

                        for n in range(1, len(tr) + 1):
                            kim_check = driver.find_element(By.CSS_SELECTOR, "#team2 > div > div.wrp_lst > table.lst_board.lst_fixed.w123 > tbody > tr:nth-child(" + str(n) + ") > td.name").get_attribute("innerText")
                            if "김연경" in kim_check :
                                for m in range(1, 6) :
                                    starting_check = driver.find_element(By.CSS_SELECTOR, "#team2 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(m) + ") > td:nth-child(1) > span").get_attribute("class")
                                    if starting_check == "starting" :
                                        starting = "선발"
                                        kim_score = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(6)").get_attribute("innerText")
                                        kim_trial = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(7)").get_attribute("innerText")
                                        kim_success = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(8)").get_attribute("innerText")
                                        kim_block = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(9)").get_attribute("innerText")
                                        kim_miss = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(10)").get_attribute("innerText")
                                        kim_successpercent = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(11)").get_attribute("innerText")
                                        kim_share = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(12)").get_attribute("innerText")
                                        break;
                                    elif starting_check == "switch" :
                                        starting = str(m) + "세트 교체"
                                        kim_score = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(6)").get_attribute("innerText")
                                        kim_trial = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(7)").get_attribute("innerText")
                                        kim_success = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(8)").get_attribute("innerText")
                                        kim_block = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(9)").get_attribute("innerText")
                                        kim_miss = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(10)").get_attribute("innerText")
                                        kim_successpercent = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(11)").get_attribute("innerText")
                                        kim_share = driver.find_element(By.CSS_SELECTOR, "#team1 > div > div.wrp_lst > table.lst_board.lst_scroll.w837.record_1 > tbody > tr:nth-child(" + str(n) + ") > td:nth-child(12)").get_attribute("innerText")
                                        break;
                                    else :
                                        starting = "미출전"
                                        kim_score = ""
                                        kim_trial = ""
                                        kim_success = ""
                                        kim_block = ""
                                        kim_miss = ""
                                        kim_successpercent = ""
                                        kim_share = ""
                            else :
                                starting = "미출전"
                                kim_score = ""
                                kim_trial = ""
                                kim_success = ""
                                kim_block = ""
                                kim_miss = ""
                                kim_successpercent = ""
                                kim_share = ""

                        if "흥국생명" in h_team :
                            result = '승' if int(h_score) > int(a_score) else '패'
                            wr.writerow([a_team, h_attack, h_block, h_serve, a_miss, h_miss, h_all, a_all, h_dig, h_recieve, h_set, h_attackpercent, h_recievepercent, game_time, h_score, a_score, result, starting, kim_score, kim_trial, kim_success, kim_block, kim_miss, kim_successpercent, kim_share])
                        else:
                            result = '승' if int(h_score) < int(a_score) else '패'
                            wr.writerow([h_team, a_attack, a_block, a_serve, h_miss, a_miss, a_all, h_all, a_dig, a_recieve, a_set, a_attackpercent, a_recievepercent, game_time, a_score, h_score, result, starting, kim_score, kim_trial, kim_success, kim_block, kim_miss, kim_successpercent, kim_share])

                        driver.find_element(By.XPATH, "//*[@id='wrp_content']/article[1]/div/a").click()

        f.close()

    except NoSuchElementException as e:
        print(e)

driver.quit()  # driver 종료