from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

search = input('Что ищем в Википедии? ')

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search)
search_box.send_keys(Keys.RETURN)

while True:
    # Листаем параграфы текущей статьи
    paragraphs = browser.find_elements(By.TAG_NAME, 'p')
    print("\nПараграфы статьи:")
    for i, paragraph in enumerate(paragraphs):
        print(f"{i + 1}: {paragraph.text}")

    print("\nВыберите действие:")
    print("1: Листать параграфы статьи")
    print("2: Перейти на одну из связанных страниц")
    print("3: Выйти из программы")

    choice = input("Введите номер действия (1/2/3): ")

    if choice == '1':
        print("Листаем параграфы... (нажмите Enter для продолжения)")
        input()  # Ждем нажатия Enter для продолжения
    elif choice == '2':
        # Получаем связанные страницы
        links = browser.find_elements(By.XPATH, "//a[@href and not(contains(@href, ':'))]")[:5]
        print("\nСвязанные страницы:")
        for i, link in enumerate(links):
            print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")

        link_choice = int(input("Выберите номер связанной страницы (1/2/3/4/5): ")) - 1
        if 0 <= link_choice < len(links):
            links[link_choice].click()
            time.sleep(2)  # Ждем загрузки страницы
        else:
                print("Неправильный выбор!")
    elif choice == '3':
        print("Выход из программы...")
        break
    else:
        print("Неправильный ввод. Пожалуйста, выберите 1, 2 или 3.")

browser.quit()