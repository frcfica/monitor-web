import time
import random

def chequear_servidor():
    print("=== [SISTEMA DE MONITOREO INICIADO] ===")
    sitios = ["google.com", "mi-universidad.cl", "github.com", "mi-api-privada.net"]
    
    # Haremos que revise los sitios 5 veces y luego termine
    for i in range(5):
        sitio = random.choice(sitios)
        # Simulamos un código de respuesta HTTP (200 es OK, 500 es Error de Servidor)
        codigo_estado = random.choice([200, 200, 200, 404, 500]) 
        
        print(f"\n[Intento {i+1}] Conectando a https://{sitio}...")
        time.sleep(1.5) # Pausa de 1.5 segundos para simular la espera de red
        
        if codigo_estado == 200:
            print(f"🟩 ÉXITO: {sitio} está respondiendo correctamente (HTTP 200).")
        elif codigo_estado == 404:
            print(f"🟨 ADVERTENCIA: {sitio} no encontrado (HTTP 404).")
        else:
            print(f"🟥 CRÍTICO: {sitio} ha caído o tiene un error interno (HTTP 500).")
            
    print("\n=== [MONITOREO FINALIZADO TEMPORALMENTE] ===")

if __name__ == "__main__":
    chequear_servidor()