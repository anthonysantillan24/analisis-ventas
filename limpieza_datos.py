import pandas as pd

# Cargar datos
df = pd.read_csv("ventas_sucias.csv")

# Mostrar info inicial
print("Datos originales:")
print(df)

# Eliminar filas con valores nulos
df = df.dropna()

# Convertir fechas
df["fecha"] = pd.to_datetime(df["fecha"], errors='coerce')

# Eliminar fechas inválidas
df = df.dropna(subset=["fecha"])

# Convertir precio a número
df["precio"] = pd.to_numeric(df["precio"], errors='coerce')

# Eliminar precios inválidos
df = df.dropna(subset=["precio"])

# Eliminar duplicados
df = df.drop_duplicates()

# Estandarizar texto
df["cliente"] = df["cliente"].str.strip().str.title()
df["producto"] = df["producto"].str.strip().str.title()
df["ciudad"] = df["ciudad"].str.strip().str.title()

# Crear columna total
df["total"] = df["precio"] * df["cantidad"]

# Guardar archivo limpio
df.to_csv("ventas_limpias.csv", index=False)

print("\nDatos limpios:")
print(df)