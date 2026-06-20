import streamlit as st
import subprocess
import pandas as pd

# Configuración básica de la página
st.set_page_config(page_title="Sensor Dashboard", layout="wide")
st.title("📊 Monitor Concurrente de Sensores (C + Python)")
st.markdown("Este panel está leyendo datos de un proceso en C en tiempo real mediante **Pipes (IPC)**.")

# Creamos "contenedores" vacíos en la interfaz que luego vamos a actualizar
col1, col2 = st.columns(2)
metric_temp = col1.empty()
metric_hum = col2.empty()
grafico = st.empty()

# Guardaremos el historial de datos aquí para graficarlos
historial = pd.DataFrame(columns=["Temperatura", "Humedad"])

# Valores iniciales
temp_actual = 25
hum_actual = 50

# Botón para arrancar el motor
if st.button("Iniciar Lectura desde C"):
    
    # ---------------------------------------------------------
    # ¡EL PUENTE! (IPC) 
    # Ejecutamos el programa en C en segundo plano y capturamos su stdout
    # OJO: Si usas Windows, cambia './sensors' por 'sensors.exe'
    # ---------------------------------------------------------
    proceso = subprocess.Popen(['./sensors'], stdout=subprocess.PIPE, text=True)
    
    # Leemos la salida de C línea por línea en un bucle infinito
    for linea in proceso.stdout:
        linea = linea.strip() # Limpiamos los saltos de línea (\n)
        
        # Clasificamos el dato que vino de C
        if linea.startswith("TEMP"):
            temp_actual = int(linea.split(',')[1])
        elif linea.startswith("HUM"):
            hum_actual = int(linea.split(',')[1])
            
        # Agregamos los datos nuevos al historial
        nuevo_dato = pd.DataFrame({"Temperatura": [temp_actual], "Humedad": [hum_actual]})
        historial = pd.concat([historial, nuevo_dato], ignore_index=True)
        
        # Para que el gráfico no se vuelva infinito y consuma toda la RAM, 
        # mantenemos solo los últimos 30 datos
        if len(historial) > 30:
            historial = historial.tail(30)
            
        # ¡La magia visual! Actualizamos la interfaz en vivo
        metric_temp.metric("🌡️ Temperatura", f"{temp_actual} °C")
        metric_hum.metric("💧 Humedad", f"{hum_actual} %")
        grafico.line_chart(historial)