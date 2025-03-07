import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Criando dados de exemplo
# Características: [tem_pelo, late, perna_longa, focinho_achatado, rabo_enrolado]
X = np.array([
[1, 0, 0, 1, 1],# porco
[1, 0, 0, 1, 1],# porco
[1, 0, 0, 1, 0],# porco
[1, 1, 1, 0, 0],# cachorro
[1, 1, 1, 0, 1],# cachorro
[1, 1, 1, 0, 0] # cachorro
])

y = np.array(['porco', 'porco', 'porco', 'cachorro', 'cachorro', 'cachorro'])

# Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinando o modelo (LinearSVC é mais simples e rápido que o SVC tradicional)
modelo = LinearSVC(random_state=42)
modelo.fit(X_train, y_train)

# Fazendo uma previsão
animal_novo = np.array([[0, 0, 0, 0, 0]])
animal_novo02 = np.array([[1, 1, 1, 1, 1]])

# características do novo animal
previsao = modelo.predict(animal_novo)
print(f"O animal é provavelmente um: {previsao[0]}")

previsao02 = modelo.predict(animal_novo02)
print(f"O animal é provavelmente um: {previsao02[0]}")

y_predi = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_predi)
print('Acurácia:', accuracy)  
