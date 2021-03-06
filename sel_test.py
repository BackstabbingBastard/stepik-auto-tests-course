from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# задание 2.4 настройка ожиданий 8 из 9 шагов
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/explicit_wait2.html")
# number100 = WebDriverWait(browser, 15).until(
#         EC.text_to_be_present_in_element((By.ID, "price"), '100')
#     )
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
# browser.implicitly_wait(2)
# x = browser.find_element_by_id("input_value")
# x = calc(int(x.text))
# input1 = browser.find_element_by_id("answer")
# input1.send_keys(x)
# button = browser.find_element_by_id("solve")
# button.click()


# задание 13
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/redirect_accept.html")
# button = browser.find_element_by_css_selector("button.trollface")
# button.click()
# time.sleep(1)
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# x = browser.find_element_by_id("input_value")
# x = calc(int(x.text))
# input1 = browser.find_element_by_css_selector("input.form-control")
# input1.send_keys(x)
# button = browser.find_element_by_css_selector("button.btn")
# button.click()


# задание 12
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/alert_accept.html')
# time.sleep(1)
# button = browser.find_element_by_tag_name("button")
# button.click()
# alert = browser.switch_to.alert
# alert.accept()
# # time.sleep(1)
# x = browser.find_element_by_id("input_value")
# x = calc(int(x.text))
# input1 = browser.find_element_by_id("answer")
# input1.send_keys(x)
# submit_button = browser.find_element_by_tag_name("button")
# submit_button.click()


# задание 11
# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'file.txt')

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/file_input.html")
# input1 = browser.find_element_by_name('firstname')
# input1.send_keys('Vasya')
# input2 = browser.find_element_by_name('lastname')
# input2.send_keys('Pupkin')
# input3 = browser.find_element_by_name('email')
# input3.send_keys('kinogovno@gmail.com')
# file_input = browser.find_element_by_name('file')
# file_input.send_keys(file_path)
# button = browser.find_element_by_tag_name("button")
# button.click()


# задание 10
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/execute_script.html')
# x = browser.find_element_by_id('input_value')
# x = int(x.text)
# x = calc(x)
# input1 = browser.find_element_by_id("answer")
# input1.send_keys(x)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# checkbox_element = browser.find_element_by_id('robotCheckbox')
# checkbox_element.click()
# radion_element = browser.find_element_by_css_selector("[value='robots']")
# radion_element.click()
# button.click()


# задание 9
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     num1 = browser.find_element_by_id('num1')
#     num1 = int(num1.text)
#     num2 = browser.find_element_by_id('num2')
#     num2 = int(num2.text)
#     sum = str(num1 + num2)
#     select = Select(browser.find_element_by_id("dropdown"))
#     select.select_by_value(sum)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#      # ожидание чтобы визуально оценить результаты прохождения скрипта
#      time.sleep(10)
#      # закрываем браузер после всех манипуляций
#      browser.quit()


# # задание 8
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x = browser.find_element_by_id('treasure')
#     x = x.get_attribute('valuex')
#     x = calc(x)
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(x)
#     checkbox_element = browser.find_element_by_id('robotCheckbox')
#     checkbox_element.click()
#     radion_element = browser.find_element_by_css_selector("[value='robots']")
#     radion_element.click()
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#     print(x)
#
# finally:
#      # ожидание чтобы визуально оценить результаты прохождения скрипта
#      time.sleep(10)
#      # закрываем браузер после всех манипуляций
#      browser.quit()


# задание 7
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element_by_id('input_value')
#     x = x_element.text
#     y = calc(x)
#     input1 = browser.find_element_by_id('answer')
#     input1.send_keys(y)
#     checkbox_element = browser.find_element_by_id('robotCheckbox')
#     checkbox_element.click()
#     radion_element = browser.find_element_by_css_selector("[value='robots']")
#     radion_element.click()
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#      # ожидание чтобы визуально оценить результаты прохождения скрипта
#      time.sleep(10)
#      # закрываем браузер после всех манипуляций
#      browser.quit()


# # задание 6
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element_by_xpath("//input[@placeholder='.name']")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
#     input2.send_keys("Ivanov")
#     input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
#     input3.send_keys("Ivanov")

#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# # задание 5
# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     # Ваш код, который заполняет обязательные поля
#     input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @placeholder='Input your first name']")
#     input1.send_keys("Ivan")

#     input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @placeholder='Input your last name']")
#     input2.send_keys("Ivanov")
#
#     input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @placeholder='Input your email']")
#     input3.send_keys("Ivanov")
#
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# задание 4
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# задание 3
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements_by_tag_name('input')
#     for element in elements:
#        element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#
# finally:
#      # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# задание2
# link = 'http://suninjuly.github.io/find_link_text'
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     crypt = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
#     link = browser.find_element_by_link_text(crypt)
#     link.click()
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#      # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


# задание 1
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

