import pandas as pd

# Cargar datos limpios
df = pd.read_csv("ventas_limpias.csv")

print("\n--- ANÁLISIS ---")

# Top productos
top_productos = df.groupby("producto")["cantidad"].sum().sort_values(ascending=False)
print("\nTop productos:")
print(top_productos)

# Mejor cliente
mejor_cliente = df.groupby("cliente")["total"].sum().sort_values(ascending=False)
print("\nMejor cliente:")
print(mejor_cliente)

# Ventas por ciudad
ventas_ciudad = df.groupby("ciudad")["total"].sum()
print("\nVentas por ciudad:")
print(ventas_ciudad)

# Ticket promedio
ticket_promedio = df["total"].mean()
print("\nTicket promedio:", ticket_promedio)

# Ventas por día
ventas_fecha = df.groupby("fecha")["total"].sum()
print("\nVentas por fecha:")
print(ventas_fecha)

# Guardar resultados
with open("resultados.txt", "w") as f:
    f.write("Top productos:\n")
    f.write(str(top_productos))
    f.write("\n\nMejor cliente:\n")
    f.write(str(mejor_cliente))
    f.write("\n\nVentas por ciudad:\n")
    f.write(str(ventas_ciudad))
    f.write("\n\nTicket promedio:\n")
    f.write(str(ticket_promedio))