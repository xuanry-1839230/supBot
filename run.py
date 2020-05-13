from selenium import webdriver

name = "Susan Yang"
email = "syang1507@gmail.com"
tel = "4250000000"
address = "1000 1st Ave Ne"
cc = "1111 1111 1111 1111"
city = "Seattle"
state = "WA"
zip = "98000"
exp_month = "03"
exp_year = "23"
cvv = "123"

chromedriver_location = "chromedriver.exe"

# set website locaiton
driver = webdriver.Chrome(chromedriver_location)
driver.get("https://www.supremenewyork.com/shop/accessories/nq5hkuef2")

# add item to cart
add_to_cart = '//*[@id="add-remove-buttons"]/input'
driver.find_element_by_xpath(add_to_cart).click()

# delay execution
time.sleep(2)

check_out = '//*[@id="cart"]/a[2]'
driver.find_element_by_xpath(check_out).click()

name_xpath = '//*[@id="order_billing_name"]'
driver.find_element_by_xpath(name_xpath).send_keys(name)

email_xpath = '//*[@id="order_email"]'
driver.find_element_by_xpath(email_xpath).send_keys(email)

tel_xpath = '//*[@id="order_tel"]'
driver.find_element_by_xpath(tel_xpath).send_keys(tel)

add_xpath = '//*[@id="bo"]'
driver.find_element_by_xpath(add_xpath).send_keys(address)

zip_xpath = '//*[@id="order_billing_zip"]'
driver.find_element_by_xpath(zip_xpath).send_keys(zip)

city_xpath = '//*[@id="order_billing_city"]'
driver.find_element_by_xpath(city_xpath).send_keys(city)

state_xpath = '//*[@id="order_billing_state"]/option[56]'
driver.find_element_by_xpath(state_xpath).click()

cc_xpath = '//*[@id="rnsnckrn"]'
driver.find_element_by_xpath(card_month_xpath).click()

card_month_xpath = '//*[@id="credit_card_month"]/option[5]'
driver.find_element_by_xpath(card_month_xpath).click()

card_year_xpath = '//*[@id="credit_card_year"]/option[4]'
driver.find_element_by_xpath(card_year_xpath).click()

cvv_xpath = '//*[@id="orcer"]'
driver.find_element_by_xpath(cvv_xpath).send_keys(cvv)

i_agree_xpath = '//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins'
driver.find_element_by_xpath(i_agree_xpath).click()

pay_xpath = '//*[@id="pay"]/input'
driver.find_element_by_xpath(pay_xpath).click()

print("web driver run")
