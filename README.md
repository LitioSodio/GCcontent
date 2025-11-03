Análisis del contenido GC en Mycoplasma leachii

Este repositorio contiene un script en Python para calcular y visualizar el contenido de guanina y citosina (GC) a lo largo del genoma completo de Mycoplasma leachii (GenBank: FR668087.1), como adaptación de los ejercicios realizados en clase con Escherichia coli.
El análisis compara la secuencia real con una versión aleatoria del genoma, permitiendo observar la variación local del %GC y su distribución estadística.

Contenido del repositorio
├── gc_content_myco.py          # Script principal unificado
├── secuencias/
│   └── mycoplasma_leachii.fasta  # Secuencia genómica usada en el análisis
├── figuras/
│   ├── grafico_lineal.png        # Variación del GC por ventanas
│   └── histograma_gc.png         # Distribución del contenido GC
└── README.md                     # Documento explicativo

Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías de Python:

pip install pandas matplotlib seaborn biopython

Ejecución

Coloca el archivo mycoplasma_leachii.fasta en la carpeta secuencias/
(puedes descargarlo desde GenBank o usar el bloque del código que lo descarga automáticamente).

Ejecuta el script:

python gc_content_myco.py


El programa:

Calcula el %GC en ventanas deslizantes (10.000 pb con pasos de 1.000 pb).

Genera una secuencia aleatoria del mismo tamaño para comparar.

Produce dos gráficas:

Variación del contenido GC a lo largo del genoma.

Distribución del contenido GC en forma de histograma.

Imprime estadísticas descriptivas en consola (promedio, límites IQR, etc.).

Resultados esperados

El genoma de Mycoplasma leachii presenta un contenido GC promedio de alrededor del 24 %, con baja variabilidad a lo largo del genoma.

Esta característica es consistente con el patrón genómico típico de los Mycoplasma, organismos con genomas reducidos y ricos en adenina-timina (AT).
