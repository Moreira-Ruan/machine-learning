
# Compilado - Inteligência Artificial (Ciclo 2)

## Sumário
1. Classificadores Baseados em Regras
2. Naive Bayes e Aprendizado Probabilístico
3. Regressão Linear Simples
4. Exercícios Práticos
5. Questões Dissertativas Prováveis

---

## 1. Classificadores Baseados em Regras
### Teoria
- Conceito de Regras (if-then-else)
- Cobertura e Engatilhamento de Regras
- Métricas: Coverage, Accuracy, Laplace, FOIL's Gain
- Construção de Regras: Geral-para-Específico e Específico-para-Geral
- Algoritmo RIPPER
- Extração Indireta de Regras (Árvores de Decisão)

## 2. Naive Bayes e Aprendizado Probabilístico
### Teoria
- Teorema de Bayes: P(H|X) = (P(X|H) * P(H)) / P(X)
- Hipótese MAP (Maximum A Posteriori)
- Classificador Naive Bayes: Supondo Independência Condicional
- Aplicações em Diagnóstico Médico e Classificação de Textos
- Exemplo Prático: Diagnóstico de Câncer

## 3. Regressão Linear Simples
### Teoria
- Correlação Linear (coeficiente de Pearson)
- Regressão: Modelo Linear Simples Y = a + bX
- Método dos Mínimos Quadrados
- Coeficiente de Determinação (R²)
- Aplicação Prática: Fertilizante vs Produtividade, Octanagem vs Aditivo

## 4. Exercícios Práticos
### Classificador Regras - Vertebrados
- Dataset: Vertebrados (Mammals, Birds, Reptiles)
- Regras implementadas manualmente
- Métricas calculadas: Cobertura, Accuracy, Laplace, FOIL Gain

### Diagnóstico Médico (Bayes)
- Problema do Câncer
- Probabilidades a priori e a posteriori
- Conclusão: Interpretação de Testes com baixa prevalência

### Naive Bayes - PlayTennis
- Implementação com CategoricalNB
- Matriz de Confusão, Acurácia, Precision, Recall, F1

### Regressão Linear Simples
- Fertilizante vs Produtividade (previsão para 45kg/ha)
- Peso vs Altura (previsão para 170cm)
- Octanagem vs Percentual de Aditivo (previsão para 5,5%)

## 5. Questões Dissertativas Prováveis
### Exemplo 1
> Explique o funcionamento do Algoritmo RIPPER e suas vantagens em datasets desbalanceados.

### Exemplo 2
> Dado um problema de diagnóstico com sensibilidade de 90% e especificidade de 95%, com prevalência de 1%, calcule P(doença|positivo).

### Exemplo 3
> Explique o conceito de Coeficiente de Determinação (R²) e sua importância na avaliação de modelos de regressão linear simples.

---
