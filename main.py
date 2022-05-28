from threadmaid import ThreadMaid
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver_config = webdriver.FirefoxOptions()
driver_config.binary_location = "geckodriver.exe"
driver = webdriver.Firefox()


def start():
	global driver

	driver.get("https://web.whatsapp.com")


	while True:
		login_page = False

		try:
			login_page = driver.find_element(by=By.CLASS_NAME, value="b77wc")
		except Exception as i:
			print("waiting for login screen..")

		if login_page:
			while login_page:
				print("waiting for login..")
				sleep(5)
		else:
			print("login succeeded")
			exit()
		sleep(1)


main_thread = ThreadMaid().setup(start)
main_thread.run()
