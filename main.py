import schedule
from selenium import webdriver
import random
import datetime
from time import sleep

CAMPO_USUARIO = 'userName_relogio_8001'
USUARIO = 'XXXX'
CAMPO_SENHA = 'password_relogio_8001'
SENHA = 'XXXX'

EL_BOTAO_PONTO = 'btEntrada_relogio_8001'
BOTAO = ''

def main():
    schedule_amanha()

def inicia_nav():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"./chromedriver9204.exe" ,options=options)


    driver.get('https://cliente.apdata.com.br/everis/')
    while not driver.find_elements_by_tag_name('input'):
        try:
            sleep(3)
            return driver, driver.find_elements_by_tag_name('input')
        except:
            continue
    
    
def preencher_dados(campos):
    for campo in campos:
        if(campo.get_attribute('lang') == CAMPO_USUARIO):
            campo.clear()
            campo.send_keys(USUARIO)
        
        if(campo.get_attribute('lang') == CAMPO_SENHA):
            campo.clear()
            campo.send_keys(SENHA)
        
        if(campo.get_attribute('lang') == EL_BOTAO_PONTO):
            botao = campo
    
    return botao

def bater_ponto():
    driver, campos = inicia_nav()
    botao = preencher_dados(campos)
    if(botao):
        botao.click()
        sleep(2)
        name = datetime.datetime.now().strftime("%d-%m-%Y %H%M")
        driver.save_screenshot(f'{name}.png')
        

def schedule_amanha():
    schedule.clear()
    schedule.every().day.at('19:40').do(schedule_amanha)


    rand = random.randint(-5,5)
    a = datetime.datetime.now()
    inicio = datetime.datetime(year=a.year, month=a.month, day=a.day ,hour=9, minute=0)
    almoco = datetime.datetime(year=a.year, month=a.month, day=a.day ,hour=12, minute=0)
    voltaalmoco = datetime.datetime(year=a.year, month=a.month, day=a.day ,hour=13, minute=0)
    saida = datetime.datetime(year=a.year, month=a.month, day=a.day ,hour=18, minute=0)


    inicio = inicio + datetime.timedelta(minutes=rand)
    almoco = almoco + datetime.timedelta(minutes=rand)
    voltaalmoco = voltaalmoco + datetime.timedelta(minutes=rand)
    saida = saida + datetime.timedelta(minutes=rand)
    
    schedule.every().day.at(str(inicio.time())).do(bater_ponto)
    schedule.every().day.at(str(almoco.time())).do(bater_ponto)
    schedule.every().day.at(str(voltaalmoco.time())).do(bater_ponto)
    schedule.every().day.at(str(saida.time())).do(bater_ponto)
    
if __name__ == "__main__":
    main()
    print(schedule.get_jobs())      
    while True:
        schedule.run_pending()
        sleep(300)