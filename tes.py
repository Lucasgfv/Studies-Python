
nav.get("https://portal.milvus.com.br/#/login")

# Loga no milvus

nav.find_element(By.XPATH,
    '//*[@id="wrap"]/div/div/div/div/form/div[1]/input').send_keys("lucascomput23@gmail.com")
nav.find_element(By.XPATH,
    '//*[@id="wrap"]/div/div/div/div/form/div[2]/input').send_keys("Comput2021")
nav.find_element(By.XPATH,
    '//*[@id="wrap"]/div/div/div/div/form/div[4]/button').click()

# Arrumando o terrno antes de começar o ticket
time.sleep(8)
pyautogui.click(x=916, y=928)

# Abrir ticket

nav.find_element(By.XPATH,
    '//*[@id="topnav"]/ul/ul/li[5]/a/button').click()


# Cliente
nav.find_element((By.XPATH,
                  '//html/body/div[8]/div/div/form/div[2]/div/div[1]/div[2]/div[1]/div/select-header/div/div')).click()
nav.find_element((By.XPATH,
                  '//*[@id="ui-select-choices-row-1-0"]/div'))