import pandas as pd #Manipulación y análisis de datos
import matplotlib.pyplot as plt #permite crear visualizaciones
from sklearn.preprocessing import StandardScaler#Normalización de datos
from sklearn.cluster import KMeans #  algoritmo de agrupamiento K-Means

# Cargar y preprocesar datos
df = pd.read_csv('force2020_data_unsupervised_learning.csv', index_col='DEPTH_MD')# Lee el archivo CSV 'force2020_data_unsupervised_learning.csv' y establece 'DEPTH_MD' como índice.
df.dropna(inplace=True)# Elimina las filas con valores faltantes

# Escalamiento
scaler = StandardScaler()# Crea una instancia del escalador StandardScaler.
df[['RHOB_T', 'NPHI_T', 'GR_T', 'PEF_T', 'DTC_T']] = scaler.fit_transform(df[['RHOB', 'NPHI', 'GR', 'PEF', 'DTC']])# Escala las columnas 'RHOB', 'NPHI', 'GR', 'PEF', 'DTC' y las guarda en nuevas columnas con el sufijo '_T'.

# Optimizar K-Means
def optimise_k_means(data, max_k):# Define una función para optimizar K-Means.
    means = []# Lista para almacenar el número de clusters.
    inertias = []# Lista para almacenar las inercias.
    for k in range(1, max_k):# Itera a través de diferentes valores de k (número de clusters).
        kmeans = KMeans(n_clusters=k) # Crea una instancia de KMeans con k clusters.
        kmeans.fit(data) # Ajusta el modelo a los datos.
        means.append(k)# Agrega el valor de k a la lista 'means'.
        inertias.append(kmeans.inertia_)# Agrega la inercia a la lista 'inertias'.

    # Crea una nueva figura para el gráfico.
    # figsize especifica el tamaño de la figura en pulgadas (ancho, alto).
    plt.figure(figsize=(10, 5))  # En este caso, la figura tendrá 10 pulgadas de ancho y 5 pulgadas de alto.
    plt.plot(means, inertias, 'o-')# 'o-' especifica que se utilicen círculos como marcadores y una línea continua para conectarlos.
    plt.xlabel('Number of clusters')# Agrega una etiqueta al eje x.
    plt.ylabel('Inertia')# Agrega una etiqueta al eje y.
    plt.show()# Muestra el gráfico

optimise_k_means(df[['RHOB_T', 'NPHI_T']], 10)#llama a la función optimise_k_means

# Aplicar K-Means con 3 clusters
kmeans = KMeans(n_clusters=3)# Crea una instancia del modelo KMeans con 3 clusters.
kmeans.fit(df[['NPHI_T', 'RHOB_T']])# Ajusta el modelo a los datos utilizando las columnas 'NPHI_T' y 'RHOB_T'.
# Agrega una nueva columna al DataFrame llamada 'kmeans_3'
df['kmeans_3'] = kmeans.labels_# que contiene las etiquetas de los clusters asignadas a cada punto de datos.

# Visualización
plt.scatter(x=df['NPHI_T'], y=df['RHOB_T'], c=df['kmeans_3'], cmap='viridis')
plt.xlabel('NPHI_T')# Etiqueta del eje x.
plt.ylabel('RHOB_T')# Etiqueta del eje y.
plt.colorbar(label='Cluster')# label: etiqueta de la barra de colores.
plt.xlim(-0.1, 1)# Establece los límites del eje x.
plt.ylim(3, 1.5)# Establece los límites del eje y.
plt.show()# Muestra el gráfico.

# Visualización para diferentes números de clusters
# Crea una figura con una fila y 5 columnas de subplots (axs).
# figsize: tamaño de la figura en pulgadas (ancho, alto).
fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(20, 5))
for K in range(1, 6):# Itera a través de diferentes valores de K (número de clusters) de 1 a 5.
    kmeans = KMeans(n_clusters=K) # Crea una instancia del modelo KMeans con K clusters.
    kmeans.fit(df[['RHOB_T', 'NPHI_T']]) # Ajusta el modelo a los datos utilizando las columnas 'RHOB_T' y 'NPHI_T'.
    df[f'kmeans_{K}'] = kmeans.labels_ # Agrega una nueva columna al DataFrame con las etiquetas de los clusters para el valor actual de K.
    ax = axs[K - 1]# Selecciona el subplot correspondiente al valor actual de K.
    ax.scatter(x=df['NPHI_T'], y=df['RHOB_T'], c=df[f'kmeans_{K}'], cmap='viridis')# Crea un gráfico de dispersión en el subplot actual.
    ax.set_ylim(3, 1.5)# Establece los límites del eje y para el subplot actual.
    ax.set_xlim(0, 1)# Establece los límites del eje x para el subplot actual.
    ax.set_title(f'N Clusters: {K}') # Establece el título del subplot actual, indicando el número de clusters.
plt.show()# Muestra la figura con todos los subplots
