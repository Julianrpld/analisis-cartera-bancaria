# Analisis-cartera-bancaria
Análisis de cartera bancaria con Python — pandas, seaborn, funciones"
# Análisis de Cartera Bancaria con Python

Análisis end-to-end de la cartera de productos de una entidad financiera, 
desde la carga de datos crudos hasta insights de negocio y visualización.

## Objetivo

Identificar qué productos, segmentos de cliente y sucursales generan mayor 
rentabilidad, y detectar anomalías en la evolución temporal del margen.

## Datos

Seis tablas relacionadas de una entidad bancaria:

| Tabla | Registros | Contenido |
|-------|-----------|-----------|
| transacciones | 19.915 | Ingreso, costo y margen por operación |
| contratos | 959 | Productos contratados por cliente |
| clientes | 400 | Segmento, edad, scoring, ingresos |
| ventas | 800 | Operaciones comerciales |
| productos | 12 | Categoría, tasa de interés |
| sucursales | 8 | Ciudad de cada sucursal |

## Análisis realizado

- **Carga y auditoría** de las 6 tablas (control de nulos y tipos de datos)
- **Margen por categoría** de producto
- **Evolución mensual** del margen (2023–2024)
- **Margen por segmento** de cliente (Retail, Premium, Empresas, Jóvenes)
- **Ranking de sucursales** por ciudad
- **Perfil estadístico** de cada segmento (edad, ingresos, scoring)
- **Función reutilizable** para generar el resumen de cualquier categoría

## Hallazgos principales

- Periféricos es la categoría de mayor margen total
- El segmento Retail genera el mayor margen agregado pese a ser clientes individuales
- Madrid y Barcelona lideran el ranking de sucursales
- Se detectaron picos anómalos de margen en enero y mayo de 2023 que 
  requerirían investigación adicional

## Tecnologías

- Python (pandas, matplotlib, seaborn)
- VS Code
