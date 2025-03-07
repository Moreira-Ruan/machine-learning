# Importe a biblioteca NumPy
import numpy as np

# Crie um array 1D com os números de 1 a 10
array_1d = np.arange(1, 11);

# Crie um array 2D (matriz) 3x3 com valores aleatórios
array_2d = np.random.rand(3, 3);

# Imprima os arrays 
print("Array 1D:", array_1d);
print("Array 2D", array_2d);

# Calcule a média do array 1D
media = np.mean(array_1d);
print("Média do array 1D:", array_1d);

# Some todos os elementos do array 2D
soma = np.sum(array_2d);
print("Soma dos elementos do array 2D", soma);