from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def scraping_google(request):
    # Configuración de Selenium
    options = Options()
    options.add_argument('--headless')  # Para ejecución sin ventana del navegador
    driver = webdriver.Chrome(options=options)  # Asegúrate de tener el driver de Chrome en tu PATH

    # URL de Google a scrapear
    url = "https://www.google.com"

    # Realizar scraping
    driver.get(url)
    line_text = driver.find_element_by_css_selector("div#main > footer div").text

    # Cerrar el navegador
    driver.quit()

    # Retornar la línea obtenida como respuesta JSON
    return JsonResponse({'line_text': line_text})





from django.urls import path
from .views import scraping_google

urlpatterns = [
    path('scrape-google/', scraping_google, name='scrape_google'),
]
