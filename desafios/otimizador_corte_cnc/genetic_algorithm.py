import random
from common.layout_display import LayoutDisplayMixin

class GeneticAlgorithm(LayoutDisplayMixin):
    def __init__(self, TAM_POP, recortes_disponiveis, sheet_width, sheet_height, numero_geracoes=100):
        print("Algoritmo Genético para Otimização do Corte de Chapa. Executado por Marco.")
        self.TAM_POP = TAM_POP
        self.initial_layout = recortes_disponiveis
        self.sheet_width = sheet_width
        self.sheet_height = sheet_height
        self.POP = []
        self.aptidao = []
        self.numero_geracoes = numero_geracoes
        self.melhor_aptidoes = []
        self.optimized_layout = None
        self.initialize_population()

    def initialize_population(self):
        """Cria a população inicial com layouts aleatórios."""
        for _ in range(self.TAM_POP):
            layout = random.sample(self.initial_layout, len(self.initial_layout))
            self.POP.append(layout)

    def evaluate(self):
       self.aptidao = []  # Resetando a lista de aptidões

       for individuo in self.POP:  # POP parece ser a população
           area_utilizada = sum(
               recorte["largura"] * recorte["altura"] if recorte["tipo"] in ["retangular", "diamante"]
               else 3.1415 * recorte["r"] ** 2 if recorte["tipo"] == "circular"
               else 0
               for recorte in individuo
           )
           self.aptidao.append(area_utilizada)  # Armazena a aptidão em uma lista separada

    def selection(self):
        """Seleciona indivíduos via torneio para crossover."""
        new_population = []
        for _ in range(self.TAM_POP):
            ind1, ind2 = random.sample(range(self.TAM_POP), 2)
            melhor = ind1 if self.aptidao[ind1] > self.aptidao[ind2] else ind2
            new_population.append(self.POP[melhor])
        self.POP = new_population

    def crossover(self):
        """Realiza crossover entre pares de indivíduos."""
        for i in range(0, self.TAM_POP, 2):
            if i + 1 < self.TAM_POP:
                ponto = random.randint(1, len(self.POP[i]) - 1)
                self.POP[i][:ponto], self.POP[i+1][:ponto] = self.POP[i+1][:ponto], self.POP[i][:ponto]

    def mutate(self, mutation_rate=0.1):
        """Aplica mutação trocando dois elementos aleatórios em um indivíduo."""
        for individuo in self.POP:
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(individuo)), 2)
                individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]

    def run(self):
        """Executa o algoritmo genético."""
        for _ in range(self.numero_geracoes):
            self.evaluate()
            self.selection()
            self.crossover()
            self.mutate()
        self.optimized_layout = max(zip(self.POP, self.aptidao), key=lambda x: x[1])[0]
        return self.optimized_layout

    def optimize_and_display(self):
        """Exibe o layout inicial e o otimizado."""
        self.display_layout(self.initial_layout, title="Initial Layout - Genetic Algorithm")
        self.optimized_layout = self.run()
        self.display_layout(self.optimized_layout, title="Optimized Layout - Genetic Algorithm")
        return self.optimized_layout
