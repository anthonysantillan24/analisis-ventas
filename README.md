# Análisis de Ventas - Pipeline de Limpieza, Procesamiento y Dashboard

Este repositorio contiene un proyecto completo de análisis de datos enfocado en el procesamiento, limpieza, agregación y visualización de un conjunto de datos de ventas de comida/restaurante.

---

## Estructura del Repositorio

| Archivo / Carpeta | Descripción |
| :--- | :--- |
| `ventas_sucias.csv` | Dataset original con datos inconsistentes, duplicados y faltantes. |
| `limpieza_datos.py` | Script en Python (Pandas) encargado de depurar y estandarizar la información. |
| `ventas_limpias.csv` | Dataset procesado y listo para el análisis. |
| `analisis.py` | Script en Python para realizar agrupaciones, cálculos de KPI y resúmenes. |
| `resultados.txt` | Salida de texto con las métricas clave y métricas calculadas. |
| `insights.txt` | Conclusiones de negocio, hallazgos principales y recomendaciones estratégicas. |
| `Análisis de Ventas.pbix` | Dashboard interactivo desarrollado en Power BI para la visualización de datos. |

---

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Librerías:** Pandas
* **Visualización & BI:** Power BI (`.pbix`)
* **Control de Versiones:** Git & GitHub

---

## Proceso de Limpieza y Transformación (ETL)

El script `limpieza_datos.py` realiza los siguientes pasos automatizados sobre el archivo inicial:
1. **Manejo de Valores Nulos:** Eliminación de registros vacíos en variables críticas.
2. **Conversión y Validación de Tipos:** Formateo correcto de fechas a `datetime` y precios a numérico (`float`).
3. **Depuración:** Eliminación de filas duplicadas y valores fuera de rango o inválidos.
4. **Estandarización de Texto:** Limpieza de espacios en blanco (`strip`) y formato Título (`title`) en clientes, productos y ciudades.
5. **Ingeniería de Características:** Creación de la columna `total = precio * cantidad`.

---

## Hallazgos Clave (Insights de Negocio)

*  **Producto Estrella:** Los **Tacos** representan el volumen más alto de ventas con **110 unidades** vendidas.
*  **Cliente Principal:** **Ana** lidera las compras con un acumulado total de **$7,000.0**.
*  **Top Ciudad en Ingresos:** **Toluca** es la plaza más rentable con un total de **$12,760.0** recopilados.
*  **Ticket Promedio:** El valor medio por transacción en el negocio se ubica en **$305.89**.

---

##  Cómo Ejecutar el Proyecto

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/anthonysantillan24/analisis-ventas.git](https://github.com/anthonysantillan24/analisis-ventas.git)
   cd analisis-ventas
