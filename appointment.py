from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

data = {"City": "Zaragoza","Form_tramite": "INFORMACIÓN","Form_policia": "POLICIA-CARTA DE INVITACIÓN", "DNI": "12345678A", "Nombre": "Mariantonieta"}
json_dump = json.dumps(data)
json_object = json.loads(json_dump)

options = Options()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications":1})


chromedriver = "/home/marina/chromedriver"
driver = webdriver.Chrome(chromedriver,chrome_options=options)
driver.get("https://sede.administracionespublicas.gob.es/icpplustiem/index")

driver.find_element_by_xpath(f"//select[@name='form']/option[text()='{json_object['City']}']").click()

driver.find_element_by_id("btnAceptar").click()


driver.find_element_by_xpath(f"//select[@name='tramiteGrupo[0]']/option[text()='{json_object['Form_tramite']}']").click()
driver.find_element_by_xpath(f"//select[@name='tramiteGrupo[1]']/option[text()='{json_object['Form_policia']}']").click()

driver.find_element_by_id("btnAceptar").click()


driver.execute_script("window.scrollTo(0, 1080)") 

driver.find_element_by_id("btnEntrar").click()

dni = driver.find_element_by_id('txtIdCitado')
dni.click()
dni.send_keys(json_object['DNI'])

nombre = driver.find_element_by_id('txtDesCitado')
nombre.click()
nombre.send_keys(json_object['Nombre'])

driver.switch_to_frame(driver.find_elements_by_tag_name("iframe")[0])


CheckBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))) 
#wait_between(0.5, 0.7)  
CheckBox.click() 


driver.find_element_by_id("btnEnviar").click()


#driver.quit()
