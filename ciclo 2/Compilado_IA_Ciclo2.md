
# Compilado Completo - Inteligência Artificial (Ciclo 2)

Professor: Dr. Henrique Valle de Lima  
Centro Universitário UniEVANGÉLICA

---

## 📖 Sumário
1. Classificadores Baseados em Regras
2. Teorema de Bayes e Naive Bayes
3. Regressão Linear Simples
4. Cálculos Resolvidos (Exercícios Práticos)
5. Questões Dissertativas e Respostas

---

## 1️⃣ Classificadores Baseados em Regras

### O que são?
- Modelo do tipo if-then-else que associa condições a uma classe.
- Ex: Se "Gives Birth = yes" e "Body Temperature = warm_blooded" → Mammals.

### Construção das Regras
- Geral para Específico: Adiciona restrições gradativamente.
- Específico para Geral: Remove restrições para aumentar cobertura.

### Métricas
- **Cobertura**: Quantos exemplos a regra cobre.
- **Acurácia**: acertos / cobertos pela regra.
- **Laplace**: Estimativa de probabilidade corrigida: (acertos + 1) / (total + |classes|).
- **FOIL's Gain**: Mede informação adicional da regra.

### RIPPER Algorithm
- Indução de regras com poda (pruning).
- Focado em datasets desbalanceados.

---

## 2️⃣ Teorema de Bayes e Naive Bayes

### Teorema de Bayes
- P(H|X) = (P(X|H) * P(H)) / P(X)
- **P(H|X)**: probabilidade a posteriori.
- **P(H)**: probabilidade a priori.
- **P(X|H)**: likelihood.
- **P(X)**: evidência.

### Naive Bayes
- Assume independência condicional dos atributos.
- Fórmula: P(C|X) ∝ P(C) * Π P(Xi|C)
- Utilizado em: diagnóstico médico, filtragem de spam, classificação de textos.

### Exemplo - Diagnóstico de Câncer
- P(H_c) = 0,0002
- P(Positivo|H_c) = 0,95 / P(Positivo|¬H_c) = 0,10
- Cálculo posteriori: P(H_c|Positivo) ≈ 0,19%

### Interpretação
Mesmo com teste positivo, a baixa prevalência da doença reduz a chance real de ser um caso verdadeiro.

---

## 3️⃣ Regressão Linear Simples

### Conceito
- Modela relação entre variável dependente (Y) e independente (X).
- Fórmula: Y = a + bX

### Correlação de Pearson
- Mede força e direção da relação linear entre X e Y.

### Coeficiente de Determinação (R²)
- Mede proporção da variação de Y explicada por X.
- Varia de 0 a 1.

### Estimação de a e b (Mínimos Quadrados)
- Inclinação (b): cov(X,Y) / var(X)
- Intercepto (a): Ȳ - bX̄

---

## 4️⃣ Cálculos Resolvidos

### Regressão: Fertilizante vs Produtividade
- Regressão Linear Simples aplicada.
- Y = 2.0667 + 0.0607X
- R² = 0.998
- Previsão para 45kg/ha: 5.06 ton/ha

### Teorema de Bayes - Câncer
- P(Positivo) = 0.10017
- P(H_c|Positivo) ≈ 0.19%

### Regressão: Peso pela Altura
- Ex: Y = -190 + 1.5X
- R² = 1.0 (dataset artificial simples)
- Previsão para 170cm: 70kg

### Regressão: Octanagem vs Aditivo
- Y = 85.571 + 1.571X
- R² = 0.995
- Previsão para 5.5% de aditivo: 93.21

---

## 5️⃣ Questões Dissertativas e Respostas

### Q1. Explique o funcionamento do algoritmo RIPPER e suas vantagens em datasets desbalanceados.
**Resposta**:  
O RIPPER é um algoritmo de indução de regras baseado em cobrir exemplos positivos enquanto minimiza erros em negativos. Ele aplica poda para evitar overfitting e é robusto em bases desbalanceadas pois otimiza cobertura específica por classe, mantendo regras concisas.

### Q2. Em um teste com 90% sensibilidade, 95% especificidade e prevalência de 1%, calcule P(doença|positivo).
**Resposta**:  
P(H) = 0.01, P(Pos|H) = 0.9, P(Pos|¬H) = 0.05  
P(Pos) = (0.9 * 0.01) + (0.05 * 0.99) = 0.009 + 0.0495 = 0.0585  
P(H|Pos) = (0.9 * 0.01) / 0.0585 = 0.009 / 0.0585 ≈ 15.38%

### Q3. Explique a importância do coeficiente de determinação (R²) em regressões lineares.
**Resposta**:  
O R² indica a proporção da variação da variável dependente explicada pelo modelo em relação à variável independente. Valores próximos de 1 indicam forte relação linear e bom ajuste. É fundamental para validar a qualidade do modelo preditivo.

---

## 🔚 Fim do Compilado
