from selenium import webdriver
import chromedriver_binary
from PIL import Image
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

browser = webdriver.Chrome()
browser.get('https://tabelog.com/')

#検索
write_form = browser.find_element_by_class_name('js-adjust-position-nav')
wite_area = write_form.find_element_by_id('sa').send_keys(input('エリア・駅名を入力してください。'))

serch = write_form.find_element_by_id('js-global-search-btn').click()

restinformation = []
rightinfo = []
left = []
alllist = []

#ページ移動前　店名
info = browser.find_elements_by_class_name('cpy-rst-name')

for k in range(len(info)):
    scroll_element = info[k]
# 初期化
    actions = ActionChains(browser)
# 動作の決定
    actions.move_to_element(scroll_element)
# 実行
    actions.perform()

    #ページ移動
    info[k].click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    #遷移後データ取得用
    time.sleep(1)
    #tag td を取る用
    information2 = browser.find_element_by_class_name('rstinfo-table__table')
    #店情報取る用
    information = browser.find_elements_by_class_name('rstinfo-table__table')

    rightinfo = information2.find_elements_by_tag_name('td')
    rightinfotext = []
    restinformation = []
    for j in rightinfo:
        rightinfotext = j.text
        restinformation.append(rightinfotext)

    alllist.append(restinformation)


    browser.close()
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])

    time.sleep(1)

    k = k +1


browser.quit()
