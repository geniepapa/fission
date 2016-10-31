from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.msc.com/track-a-shipment?agencyPath=chn")

elem_input = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")
elem_input.send_keys("MSCUOL252100")

elem_cookie_accept = driver.find_element_by_id("lnkCookieAccept")
elem_cookie_accept.click()

elem_search = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")
driver.execute_script("WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions('ctl00$ctl00$plcMain$plcMain$TrackSearch$hlkSearch', '', true, 'BolSearchPage', '', false, true))")

elem_output = driver.find_element_by_xpath("//*[@id='ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_pnlBOLContent']/table")
print(elem_output.get_attribute("innerHTML"))


driver.get("https://www.msc.com/track-a-shipment?agencyPath=chn")

elem_input = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_txtBolSearch_TextField")
elem_input.send_keys("MSCUOL252100")


elem_search = driver.find_element_by_id("ctl00_ctl00_plcMain_plcMain_TrackSearch_hlkSearch")
driver.execute_script("WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions('ctl00$ctl00$plcMain$plcMain$TrackSearch$hlkSearch', '', true, 'BolSearchPage', '', false, true))")

elem_output = driver.find_element_by_xpath("//*[@id='ctl00_ctl00_plcMain_plcMain_rptBOL_ctl00_pnlBOLContent']/table")
print(elem_output.get_attribute("innerHTML"))

driver.close()
