# ---------------------------- IMPORTED MODULES ------------------------------- #
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# ---------------------------- SET UP WEB DRIVER SETTINGS------------------------------- #
firefox_web_driver = "/media/kemal/Kemal Data/Python/100DaysOfCode/geckodriver"
browser = webdriver.Firefox(executable_path=firefox_web_driver)


# ---------------------------- FUNCTIONS ------------------------------- #
def log_in_via_fb():
	log_fb = [inner_element for inner_element in browser.find_elements_by_tag_name("a") if
	          inner_element.get_attribute("title") == "Facebook"]
	log_fb[0].click()


def cover_letter_each_tab():
	browser.switch_to.window(browser.window_handles[i])
	apply_link = browser.find_element_by_link_text("Откликнуться").get_attribute("href")
	browser.get(apply_link)
	time.sleep(5)
	covering_letter = browser.find_element_by_css_selector(".bloko-toggle__expandable-reverse")
	covering_letter.click()
	text_area = browser.find_element_by_name("letter")
	header = browser.find_element_by_css_selector(".bloko-header-3_lite")
	header = header.text.split(",")[1]
	with open("cover_letter.txt") as file:
		content = file.read()
		text_area.send_keys(content.replace("company", header))
		# browser.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div[1]/div[2]/form/div[2]/button").click()


# ---------------------------- ENTERING PROCESS ------------------------------- #
browser.get("https://rabota.by/")
log_in = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[1]/div[1]/div/div[4]/a")
log_in.click()
time.sleep(3)
log_in_via_fb()
fb_email = browser.find_element_by_id("email")
fb_password = browser.find_element_by_id("pass")
fb_email.send_keys("prince_of_love93@mail.ru")
fb_password.send_keys("Rzvfkbr160393", Keys.ENTER)
time.sleep(10)

# ---------------------------- JOB SEEKING PROCESS ------------------------------- #
profession = browser.find_element_by_name("text")
profession.send_keys("Python Junior", Keys.ENTER)
time.sleep(5)
all_vacancies = browser.find_elements_by_css_selector(".vacancy-serp-item__row_header a")
matched_elements = []
for el in all_vacancies:
	if "Junior" in el.text and "Python" in el.text:
		matched_elements.append(el)
# ---------------------------- JOB APPLYING PROCESS ------------------------------- #
for element in matched_elements:
	element.click()

for i in range(1, len(matched_elements)):
	try:
		time.sleep(3)
		cover_letter_each_tab()
		time.sleep(5)
	except NoSuchElementException:
		log_in_via_fb()
		time.sleep(5)
		cover_letter_each_tab()


# ---------------------------- END OF PROGRAM ------------------------------- #
