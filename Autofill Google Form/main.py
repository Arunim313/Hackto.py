#requirements: selenium
from selenium import webdriver
import random

browser = webdriver.Firefox()
browser.get("Add your form here")
times = 50
try:
    while times:
        #Hardcoded logic
        test = 0

        radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")

        check1 = random.choice([0,1,2])

        radiobuttons[check1].click()

        if check1 == 2 or check1 == 1:
            test = 4
            radiobuttons[test].click()

        else:
            test = 3
            radiobuttons[test].click()

        textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
        if test == 3:
            crypto = ["BTC", "ETH", "XRP", "LTC", "USDT", "BCH", "LIBRA", "XMR", "EOS", "BSV", "BNB"]
            textboxes[0].send_keys(random.choice(crypto))


        if check1 == 2:
            radiobuttons[7].click()
        else:
            check2 = random.choice([5,6])
            radiobuttons[check2].click()

        testcheck = browser.find_elements_by_class_name("freebirdMaterialScalecontentColumn")
        testvar = random.choice([0,1,2,3,4])
        testcheck[testvar].click()

        check3 = random.choice([8,9,10])
        radiobuttons[check3].click()
        check4 = random.choice([11,12,13])
        radiobuttons[check4].click()


        check5 = random.choice([14,15,16])
        radiobuttons[check5].click()

        checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")

        if check1 == 0:
            c1 = random.choice([0,1])
            checkboxes[c1].click()
            c2 = random.choice([2,3])
            checkboxes[c2].click()
            c3 = random.choice([4,5])
            checkboxes[c3].click()
            browser.implicitly_wait(4)
        else:
            checkboxes[6].click()

        browser.implicitly_wait(7)

        c4 = random.choice([8,9])
        checkboxes[c4].click()

        c5 = random.choice([10,11, 12, 13])
        checkboxes[c5].click()

        browser.find_element_by_xpath("//*[contains(text(), 'Submit')]").click()
        browser.implicitly_wait(4)
        browser.get("Add your form here")
        times-=1
        print(times)
finally:
	browser.quit()	



