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

En el archivo se limpian y se leen los datos; eliminando cualquier fila con datos faltantes (dropna()).
Se normaliza el tamaño de las columnas, se utiliza el método del codo, el cual permite establecer un número adecuado de clusters
se aplica el algoritmo de K-Means con el número de clusters definido anteriormente y finalmente se grafican los datos.

