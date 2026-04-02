from fastapi import FastAPI
from playwright.sync_api import sync_playwright


app = FastAPI()

def get_chile_time() -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        page.goto("https://www.horaoficial.cl", wait_until="domcontentloaded")
        page.wait_for_timeout(5000)  
        
        hora  = page.inner_text("#timer2")
        fecha = page.inner_text("#fecha2")
        dia   = page.inner_text("#dia2")
        
        browser.close()
        
        return {
            "hora": hora.strip(),
            "fecha": fecha.strip(),
            "dia": dia.strip()
        }
@app.get("/time")
def read_time():
    return get_chile_time()
