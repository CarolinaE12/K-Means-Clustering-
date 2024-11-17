# K-Means-Clustering-
El objetivo del ejercicio es aplicar K-Means Clustering con los datos almacenados en el archivo force2020_data_unsupervised_learning.csv 
Requisitos
Python 3.x
Bibliotecas de Python:
pandas
matplotlib
scikit-learn
Si aún no tienes estas bibliotecas instaladas, puedes instalar todas las dependencias ejecutando:

bash
Copiar código
pip install -r requirements.txt

Datos
El archivo de datos necesario para ejecutar el código es force2020_data_unsupervised_learning.csv
Asegúrate de tener este archivo CSV en el directorio de trabajo del proyecto o de actualizar la ruta del archivo en el código si está en otro directorio.

Ejecución
Para ejecutar el código, sigue estos pasos:

1.Asegúrate de tener Python y las bibliotecas necesarias instaladas.
2.Coloca el archivo force2020_data_unsupervised_learning.csv en el directorio de trabajo.
3.Ejecuta el script de Python usando el siguiente comando:
python clustering_analysis.py

Explicación del Código

Cargar y Preprocesar los Datos: El código comienza cargando el archivo CSV y eliminando cualquier fila con datos faltantes (dropna()).

python
Copiar código
df = pd.read_csv('force2020_data_unsupervised_learning.csv', index_col='DEPTH_MD')
df.dropna(inplace=True)
Normalización de los Datos: Se utiliza el StandardScaler para normalizar las columnas de datos relevantes (porosidad, densidad, etc.). Esto es importante para que el algoritmo K-Means no esté influenciado por las diferentes escalas de las variables.

python
Copiar código
scaler = StandardScaler()
df[['RHOB_T', 'NPHI_T', 'GR_T', 'PEF_T', 'DTC_T']] = scaler.fit_transform(df[['RHOB', 'NPHI', 'GR', 'PEF', 'DTC']])
Método del Codo: El método del codo se utiliza para determinar el número óptimo de clusters. Se ejecuta la función optimise_k_means, que evalúa cómo cambia la inercia con diferentes números de clusters y genera un gráfico para visualizar el "codo" (el punto donde la mejora en la reducción de la inercia se estabiliza).

python
Copiar código
optimise_k_means(df[['RHOB_T', 'NPHI_T']], 10)
Aplicar K-Means: El algoritmo K-Means se aplica con un número de clusters determinado (por ejemplo, 3). Los resultados se asignan a nuevas columnas en el DataFrame y se visualizan.

python
Copiar código
kmeans = KMeans(n_clusters=3)
kmeans.fit(df[['NPHI_T', 'RHOB_T']])
df['kmeans_3'] = kmeans.labels_
Visualización: Finalmente, se genera un gráfico de dispersión para mostrar cómo se agrupan los datos según el algoritmo K-Means. El color de los puntos indica a qué cluster pertenecen.

python
Copiar código
plt.scatter(x=df['NPHI_T'], y=df['RHOB_T'], c=df['kmeans_3'], cmap='viridis')
plt.xlabel('NPHI_T')
plt.ylabel('RHOB_T')
plt.colorbar(label='Cluster')
plt.show()
