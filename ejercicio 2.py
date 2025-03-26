# Definimos los valores de la matriz de confusión
TP = 40  # Verdaderos Positivos
TN = 30  # Verdaderos Negativos
FP = 20  # Falsos Positivos
FN = 10  # Falsos Negativos

# Calculamos el total de ejemplos
total = TP + TN + FP + FN

# 1. Cálculo del Accuracy (Exactitud)
accuracy = (TP + TN) / total

# 2. Cálculo de la Precision (Precisión)
precision = TP / (TP + FP)

# 3. Cálculo del Recall (Sensibilidad)
recall = TP / (TP + FN)

# 4. Cálculo del F1-Measure (Medida F1)
f1_measure = 2 * (precision * recall) / (precision + recall)

# Mostramos los resultados
print("--- Métricas de Evaluación ---")
print(f"Accuracy (Exactitud): {accuracy:.2f} ({accuracy*100:.2f}%)")
print(f"Precision (Precisión): {precision:.4f} ({precision*100:.2f}%)")
print(f"Recall (Sensibilidad): {recall:.2f} ({recall*100:.2f}%)")
print(f"F1-Measure: {f1_measure:.4f} ({f1_measure*100:.2f}%)")

 
​


​


​

​
