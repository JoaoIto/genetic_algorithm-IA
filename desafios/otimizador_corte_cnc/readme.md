# Algoritmo Genético para Otimização de Corte de Chapa CNC

## 📌 Introdução
Este projeto implementa um **Algoritmo Genético** para otimizar o corte de chapas CNC, buscando minimizar desperdícios e organizar a melhor disposição possível dos recortes dentro de uma chapa de material.

O objetivo do algoritmo é encontrar um layout otimizado para organizar recortes de diferentes tamanhos dentro de uma chapa de largura e altura fixas, garantindo o máximo aproveitamento de material e reduzindo perdas.

O código é baseado nos princípios de **evolução genética**, utilizando os operadores de **seleção, crossover e mutação** para gerar novas soluções e iterativamente aprimorar a distribuição dos recortes na chapa.

---

## 🚀 Como Funciona o Algoritmo
O algoritmo segue a estrutura básica de um Algoritmo Genético (GA), dividida nas seguintes etapas:

### 1️⃣ **Inicialização da População**
- O algoritmo começa criando uma população inicial de soluções aleatórias.
- Cada indivíduo da população representa uma possível disposição dos recortes na chapa.
- Os layouts iniciais são gerados embaralhando os recortes disponíveis.

### 2️⃣ **Avaliação (Cálculo da Aptidão)**
- Cada indivíduo é avaliado de acordo com um critério de **aptidão**, que mede a eficiência do uso do material.
- A aptidão é calculada com base na área utilizada e penalidades para peças que não couberem na chapa.

### 3️⃣ **Seleção**
- Utiliza o método de **torneio**, onde dois indivíduos são comparados e o melhor é selecionado para a próxima geração.
- Isso garante que layouts mais eficientes tenham maior chance de serem propagados.

### 4️⃣ **Crossover (Recombinação Genética)**
- Pares de indivíduos são combinados para gerar novos layouts.
- O crossover é feito trocando segmentos das soluções entre os pais, criando novas variações.

### 5️⃣ **Mutação**
- Em algumas soluções, duas peças trocam de posição de forma aleatória.
- Isso mantém a diversidade genética e evita que o algoritmo fique preso em soluções subótimas.

### 6️⃣ **Execução por Gerações**
- O processo de seleção, crossover e mutação se repete por várias gerações.
- A cada geração, o melhor layout encontrado é armazenado.

### 7️⃣ **Resultado Final**
- Após um número definido de gerações, o melhor layout encontrado é considerado a solução final.
- O código exibe o layout inicial e o otimizado, permitindo a comparação.

---

## 📜 Estrutura do Código
O código está organizado da seguinte forma:

### 🔹 `GeneticAlgorithm`
Classe principal do algoritmo, responsável por todas as operações genéticas.

- **`__init__()`** → Inicializa os parâmetros do algoritmo.
- **`initialize_population()`** → Gera uma população inicial aleatória.
- **`evaluate()`** → Calcula a aptidão de cada indivíduo na população.
- **`selection()`** → Aplica o método de seleção por torneio.
- **`crossover()`** → Realiza o cruzamento entre pares de indivíduos.
- **`mutate()`** → Aplica mutação aleatória aos indivíduos.
- **`run()`** → Executa o algoritmo genético por várias gerações.
- **`optimize_and_display()`** → Roda o algoritmo e exibe os layouts inicial e final.

### 🔹 `position_layout()`
Função que verifica se um layout de recortes cabe dentro da chapa sem sobreposição.

---

## 🎯 Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone ou baixe o repositório.
3. Execute o código principal:
   ```bash
    python ./desafios/otimizador_corte_cnc/app.py
   ```
4. O algoritmo irá gerar e exibir o layout inicial e o otimizado.

---

## 🛠️ Parâmetros Importantes

Os principais parâmetros do algoritmo são:

| Parâmetro          | Descrição |
|--------------------|-----------|
| `TAM_POP`         | Tamanho da população inicial |
| `sheet_width`     | Largura da chapa |
| `sheet_height`    | Altura da chapa |
| `numero_geracoes` | Quantidade de gerações a serem executadas |

---



