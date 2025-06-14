# Madrid_rental_price_prediction

## Descripción

Este proyecto utiliza un dataset obtenido de Kaggle, generado mediante un scraper de Idealista, para predecir el precio de alquiler de viviendas en Madrid. La predicción se realiza a partir de los datos que el usuario introduce a través de una aplicación web desarrollada con Streamlit.

---

## Requisitos / Dependencias

- Python (versión recomendada: 3.8+)
- pandas
- scikit-learn
- streamlit
- pickle

Todas las librerías necesarias están listadas en el archivo `requirements.txt`.

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone <URL-del-repositorio>
   cd Madrid_rental_price_prediction
   ```

2. Instala las dependencias

   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución

Para lanzar la aplicación web, abre una terminal, navega a la carpeta prediction (donde está app.py) y ejecuta:
  ```bash
  streamlit run app.py
  ```

Después, abre el navegador en la URL que te indique Streamlit (normalmente http://localhost:8501).

---

## Estructura del proyecto

Madrid_rental_price_prediction/

│

├── data/                   # Datos originales en formato CSV

│   └── dataset.csv

│

├── notebooks/              # Notebook con análisis exploratorio, preprocesamiento y entrenamiento

│   └── exploracion.ipynb

│   └── model.pkl           # Modelo entrenado serializado

│   └── scaler.pkl           # normalización aplicada 

│

├── app.py              # Aplicación Streamlit que carga el modelo y realiza predicciones

├── requirements.txt        # Dependencias necesarias para ejecutar el proyecto

└── README.md               # Este archivo

--- 

## Uso básico
Ejecuta la app con el comando indicado en la sección Ejecución. En la interfaz web de Streamlit, introduce los datos requeridos para la predicción. El sistema mostrará automáticamente el precio estimado del alquiler en Madrid según los datos ingresados.


