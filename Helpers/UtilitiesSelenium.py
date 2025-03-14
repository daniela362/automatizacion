
import datetime
import os 
import json
import configparser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import logging


class UtilitiesSelenium:

    def __init__(self, config_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.page_home_url = self.config.get('Page', 'page_home')

    def take_screenshot(driver, filename="screenshot.png"):
        base_path = r"C:\prueba\evidencias"
        if not os.path.exists(base_path):
            os.makedirs(base_path)
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(base_path, f"{filename}_{timestamp}.png")
        driver.save_screenshot(filename)
        print(f"Captura de pantalla guardada en: {filename}")


    def json_data(archivo_json):
        ruta = os.getcwd()
        ruta_archivo= os.path.join(ruta,r'C:\prueba\recourse', archivo_json )
        with open(ruta_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
