import pandas as pd

# Cargar el dataset
ventas=pd.read_csv("ventas.csv", sep=";")
transacciones=pd.read_csv("transacciones.csv")
contratos=pd.read_csv("contratos.csv")
clientes=pd.read_csv("clientes.csv")
productos=pd.read_csv("productos.csv", sep=";")
sucursales=pd.read_csv("sucursales.csv")

dfs_dict = {"ventas": ventas, "transacciones": transacciones, "contratos": contratos, "clientes": clientes, "productos": productos, "sucursales": sucursales}
for nombre, df in dfs_dict.items():
    print(f"--- Mostrando:: {nombre}")
    print(df.head())
    print("\n")

print(f"{'ARCHIVO':<15} {'FILAS':>6} {'COLS':>5} {'NULOS':>6}")
print("-" * 35)
for nombre, df in dfs_dict.items():
    print(f"{nombre:<15} {df.shape[0]:>6} {df.shape[1]:>5} {df.isnull().sum().sum():>6}") 


# Margen por categoria de producto 

tx_productos = transacciones.merge(productos, on="id_producto")
resumen_categoria_margen = tx_productos.groupby("categoria")["margen"].sum().reset_index()
resumen_categoria_margen.columns = ["categoria", "margen_total"]
resumen_categoria_margen = resumen_categoria_margen.sort_values("margen_total", ascending=False)
print(resumen_categoria_margen.to_string(index=False))

# Evolución del margen mensual

transacciones["fecha"] = pd.to_datetime(transacciones["fecha"], dayfirst=False)
transacciones["mes"] = transacciones["fecha"].dt.to_period("M").astype(str)

mensual = transacciones.groupby("mes")["margen"].sum().reset_index()
mensual.columns = ["mes", "margen"] 
mensual = mensual.sort_values("mes", ascending=True)
print(mensual.to_string(index=False))


# Margen por segmento de clientes

segmento = transacciones.merge(clientes[["id_cliente", "segmento"]])
segmento = segmento.groupby("segmento")["margen"].sum().reset_index()
segmento.columns = ["segmento", "margen"]
segmento = segmento.sort_values("margen", ascending=False)
print(segmento.to_string(index=False))

# Ranking de sucursales por margen

cruzar = transacciones.merge(clientes, on="id_cliente")
rsucursales = cruzar.merge(sucursales, on="id_sucursal")
rsucursales = rsucursales.groupby("ciudad")["margen"].sum().reset_index()
rsucursales.columns = ["sucursales", "margen"]
rsucursales = rsucursales.sort_values("margen", ascending=False)
print(rsucursales.to_string(index=False))


# Perfil del cliente: estadística descriptiva por segmento

perfil = clientes.groupby("segmento")[["edad","ingresos_anuales","scoring_crediticio"]].mean().reset_index()
print(round(perfil,2).to_string(index=False))

# Función resumen de producto

print(tx_productos["categoria"].unique())

filtro = tx_productos[tx_productos["categoria"] == "Electrónica"]
total_transacciones = filtro["margen"].count()
margen_total = filtro["margen"].sum()
margen_promedio = filtro["margen"].mean()
margen_max = filtro["margen"].max()
margen_min = filtro["margen"].min()

print(f"Transacciones: {total_transacciones}")
print(f"Margen total: {margen_total:.2f}")
print(f"Margen promedio: {margen_promedio:.2f}")
print(f"Margen maximo: {margen_max:.2f}")
print(f"Margen minimo: {margen_min:.2f}")

# Ahora convertimos todo esto en una función 

def resumen_categoria(nombre): 
    filtro = tx_productos[tx_productos["categoria"] == nombre]
    if len(filtro) == 0: 
        print(f"No existe la categoría '{nombre}'")
        return
    total_transacciones = filtro["margen"].count()
    margen_total = filtro["margen"].sum()
    margen_promedio = filtro["margen"].mean()
    margen_max = filtro["margen"].max()
    margen_min = filtro["margen"].min()
    print(f"Transacciones: {total_transacciones}")
    print(f"Margen total: {margen_total:.2f}")
    print(f"Margen promedio: {margen_promedio:.2f}")
    print(f"Margen maximo: {margen_max:.2f}")
    print(f"Margen minimo: {margen_min:.2f}")
resumen_categoria("Electrónica")
resumen_categoria("Ropa")

# Gráfico de anomalias - Evolucion del margen mensual

import matplotlib.pyplot as plt
import seaborn as sns

#sns.set_theme(style="whitegrid") este es el tema del gráfico

sns.set_theme(style="whitegrid")
plt.figure(figsize=(12,6))
sns.lineplot(data=mensual, x="mes", y="margen", markers="o")
plt.title("Evolución del margen mensual", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.ylabel("Margen total ($)")
plt.tight_layout()
plt.savefig("evolucion_margen_mensual.png", dpi=300, bbox_inches="tight") 
plt.show()

