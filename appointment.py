from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import pandas as pd
df = pd.read_csv('./cita.csv')

options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications":1})


chromedriver = "/home/marina/chromedriver"
driver = webdriver.Chrome(chromedriver,chrome_options=options)
driver.get("https://sede.administracionespublicas.gob.es/icpplustiem/index")

driver.find_element_by_xpath(f"//select[@name='form']/option[text()='{df.Options[0]}']").click()

driver.find_element_by_id("btnAceptar").click()


driver.find_element_by_xpath(f"//select[@name='tramiteGrupo[0]']/option[text()='{df.Options[1]}']").click()
driver.find_element_by_xpath(f"//select[@name='tramiteGrupo[1]']/option[text()='{df.Options[2]}']").click()

driver.find_element_by_id("btnAceptar").click()


driver.execute_script("window.scrollTo(0, 1080)") 

entrar_btn = driver.find_element_by_id("btnEntrar").click()


#driver.quit()
