import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random
# Función para calcular el contenido de guanina y citosina (GC)
def GC_content(sequence):
    """Calcula el porcentaje de GC en una secuencia de ADN."""
    count_G = sequence.count('G')
    count_C = sequence.count('C')
    GC_content = (count_G + count_C) / len(sequence)
    return round(100 * GC_content, 2)
# Parámetros generales
WINDOW_SIZE = 10000   # Tamaño de la ventana (nucleótidos)
STEP_SIZE = 1000      # Paso entre ventanas
filename = 'mycoplasma.fasta'  # ruta del archivo

# Lectura de la secuencia desde un archivo FASTA
sequence = ""
with open(filename) as file:
    next(file)  # salta la primera línea del encabezado FASTA
    for line in file:
        sequence += line.strip().upper()  # limpia espacios y pone en mayúscula

# Secuencia aleatoria para comparación
random_seq = list(sequence)
random.shuffle(random_seq)
random_seq = "".join(random_seq)

# Cálculo de contenido GC por ventanas
positions = []
GC_real = []
GC_random = []
for pos in range(0, len(sequence) - WINDOW_SIZE + 1, STEP_SIZE):
    subseq_real = sequence[pos:pos + WINDOW_SIZE]
    subseq_rand = random_seq[pos:pos + WINDOW_SIZE]
    positions.append(pos)
    GC_real.append(GC_content(subseq_real))
    GC_random.append(GC_content(subseq_rand))
# Creación del DataFrame
df = pd.DataFrame({
    'Position': positions,
    'GC_real': GC_real,
    'GC_random': GC_random
})
# Cálculo de límites (cuartiles e IQR)
q75 = df['GC_real'].quantile(0.75)
q25 = df['GC_real'].quantile(0.25)
IQR = q75 - q25
upper_bound = q75 + 1.5 * IQR
lower_bound = q25 - 1.5 * IQR

# Gráficas
sns.lineplot(data=df, x='Position', y='GC_real', label='Mycoplasma real')
sns.lineplot(data=df, x='Position', y='GC_random', label='Secuencia aleatoria')
plt.axhline(GC_content(sequence), color='black', linestyle='--', label='GC promedio')
plt.axhline(upper_bound, color='red', linestyle=':')
plt.axhline(lower_bound, color='red', linestyle=':')
plt.title("Contenido GC por ventana en Mycoplasma leachii")
plt.legend()
plt.show()

# Histograma
sns.histplot(df['GC_real'], kde=True)
plt.axvline(upper_bound, color='red', linestyle=':')
plt.axvline(lower_bound, color='red', linestyle=':')
plt.title("Distribución del contenido GC (Mycoplasma leachii)")
plt.xlabel("%GC por ventana")
plt.show()
# Estadísticas finales
print("GC promedio del genoma completo:", GC_content(sequence), "%")
print("GC promedio de la secuencia aleatoria:", GC_content(random_seq), "%")
print("Límites IQR:", lower_bound, "-", upper_bound)
