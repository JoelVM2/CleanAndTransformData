# limpieza.py
# Ejercicios prácticos – Unidad 3
# Librería principal: pandas

import pandas as pd

# ============================================================
# 🟢 NIVEL 1 – OPERACIONES BÁSICAS
# ============================================================

print("=== NIVEL 1: Operaciones básicas ===")

# Crear un DataFrame con valores nulos y duplicados
datos = {
    "Nombre": ["Ana", "Juan", "María", "Pedro", None, "Juan"],
    "Edad": [20, 21, None, 22, 21, 21],
    "Nota": [8.5, 7.0, 6.5, None, 9.0, 7.0],
    "Precio": ["12.5", "8.0", None, "10.0", "9.5", "8.0"]
}

df = pd.DataFrame(datos)
print("\nDatos originales:\n", df)

# Eliminar filas con valores vacíos
df_sin_nulos = df.dropna()
print("\nSin filas vacías:\n", df_sin_nulos)

# Sustituir valores nulos por la media
df["Edad"].fillna(df["Edad"].mean(), inplace=True)
df["Nota"].fillna(df["Nota"].mean(), inplace=True)
df["Precio"].fillna("0", inplace=True)

# Eliminar duplicados
df = df.drop_duplicates()

# Convertir "Precio" de texto a float y calcular la media
df["Precio"] = df["Precio"].astype(float)
media_precio = df["Precio"].mean()
print("\nPrecio medio:", media_precio)

print("\nDatos limpios (Nivel 1):\n", df)


# ============================================================
# 🟡 NIVEL 2 – TRANSFORMACIÓN Y FILTRADO
# ============================================================

print("\n=== NIVEL 2: Transformación y filtrado ===")

# Añadir columna de "Resultado"
df["Resultado"] = df["Nota"].apply(lambda x: "Aprobado" if x >= 5 else "Suspenso")
print("\nCon columna 'Resultado':\n", df)

# DataFrame de ventas
ventas = pd.DataFrame({
    "Producto": ["A", "B", "C", "D", "E"],
    "Cantidad": [5, 12, 8, 20, 3],
    "Precio": [10.0, 5.0, 7.5, 12.0, 9.0]
})

# Filtrar productos con más de 10 unidades vendidas
filtro = ventas[ventas["Cantidad"] > 10]
print("\nProductos con más de 10 unidades vendidas:\n", filtro)

# Ordenar alumnos por nota de mayor a menor
df_ordenado = df.sort_values(by="Nota", ascending=False)
print("\nAlumnos ordenados por nota (descendente):\n", df_ordenado)


# ============================================================
# 🟠 NIVEL 3 – DATOS REALES (CSV / EXCEL)
# ============================================================

print("\n=== NIVEL 3: CSV y fusión de datos ===")

# Crear y guardar un CSV de ejemplo
df.to_csv("alumnos.csv", index=False)

# Leer CSV y mostrar las primeras 5 filas
df_csv = pd.read_csv("alumnos.csv")
print("\nPrimeras 5 filas del CSV:\n", df_csv.head())

# Eliminar valores nulos y guardar nuevo archivo
df_limpio = df_csv.dropna()
df_limpio.to_csv("limpieza.csv", index=False)
print("\nArchivo 'limpieza.csv' creado con datos limpios.")

# Fusionar datos (simulación)
alumnos = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "María", "Pedro"],
    "Edad": [20, 21, 22, 22],
    "Clase": ["A", "B", "A", "B"]
})
notas = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "María", "Pedro"],
    "Nota": [8.5, 7.0, 6.5, 9.0]
})

fusion = pd.merge(alumnos, notas, on="Nombre")
print("\nFusión de alumnos y notas:\n", fusion)


# ============================================================
# 🔵 NIVEL 4 – MINI PROYECTOS
# ============================================================

print("\n=== NIVEL 4: Mini proyectos ===")

# Simulación de notas de clase
notas_clase = pd.DataFrame({
    "Nombre": ["Ana", "Juan", "María", "Pedro", "Luis"],
    "Nota": [9.2, 7.5, 5.0, 4.3, 8.8]
})

# Calcular estadísticas
print("\nMedia:", notas_clase["Nota"].mean())
print("Máximo:", notas_clase["Nota"].max())
print("Mínimo:", notas_clase["Nota"].min())

# Añadir columna "Categoría"
def categoria(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"

notas_clase["Categoría"] = notas_clase["Nota"].apply(categoria)
print("\nNotas con categorías:\n", notas_clase)

# Limpieza de datos de ventas
ventas2 = pd.DataFrame({
    "Producto": ["A", "B", "C", "D", "E"],
    "Cantidad": [10, -5, 15, 0, 8],
    "Precio": [10.0, 5.0, 7.5, 12.0, 9.0],
    "Fecha": ["2025-10-01", "2025-10-02", "", "2025-10-03", "2025-10-04"]
})

# Eliminar errores: cantidades negativas o fechas vacías
ventas2 = ventas2[(ventas2["Cantidad"] > 0) & (ventas2["Fecha"] != "")]
ventas2["Total"] = ventas2["Cantidad"] * ventas2["Precio"]

# Calcular total por producto
print("\nTotal de ventas por producto:\n", ventas2[["Producto", "Total"]])


# ============================================================
# 🔴 NIVEL 5 – RETO EXTRA
# ============================================================

print("\n=== NIVEL 5: Reto extra ===")
print("→ Consigue un dataset real (por ejemplo, desde Kaggle o data.gov).")
print("→ Aplica los mismos pasos: limpieza, conversión, nuevas columnas y exportación final a CSV.")
print("Este paso requiere un dataset descargado manualmente.")
