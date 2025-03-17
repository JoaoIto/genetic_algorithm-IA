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
        print("Inicializando população...")
        for _ in range(self.TAM_POP):
            layout = random.sample(self.initial_layout, len(self.initial_layout))
            self.POP.append(layout)
        print(f"População inicializada com {len(self.POP)} indivíduos.")

    def evaluate(self):
        """Avalia a aptidão de cada indivíduo, considerando sobreposição permitida e área utilizada."""
        print("Avaliação de aptidão...")
        self.aptidao = []  # Resetando a lista de aptidões
        for i, individuo in enumerate(self.POP):
            print(f"Avaliando indivíduo {i + 1}...")
            ocupado = [[0] * self.sheet_width for _ in range(self.sheet_height)]  # Matriz para controlar áreas ocupadas
            area_utilizada = 0

            for recorte in individuo:
                largura, altura = (recorte["largura"], recorte["altura"]) if recorte["tipo"] != "circular" else (2 * recorte["r"], 2 * recorte["r"])

                posicao_encontrada = False
                for tentativa in range(5):  # Tentativas reduzidas para otimizar o tempo
                    start_x = random.randint(0, self.sheet_width - largura)
                    start_y = random.randint(0, self.sheet_height - altura)

                    # Verifica se o recorte cabe na área ocupada existente
                    sobreposicao = sum(ocupado[y][x] for x in range(start_x, start_x + largura) for y in range(start_y, start_y + altura))

                    if sobreposicao == 0:  # Não há sobreposição, pode colocar o recorte
                        posicao_encontrada = True
                        # Marca a área como ocupada
                        for x in range(start_x, start_x + largura):
                            for y in range(start_y, start_y + altura):
                                ocupado[y][x] = 1
                        area_utilizada += largura * altura if recorte["tipo"] != "circular" else 3.1415 * recorte["r"] ** 2
                        print(f"Recorte {recorte} colocado em posição ({start_x}, {start_y}).")
                        break  # Sai do loop de tentativas

                if not posicao_encontrada:  # Penaliza se não conseguir encontrar uma posição
                    print(f"Não foi possível colocar o recorte {recorte}.")
                    area_utilizada -= largura * altura if recorte["tipo"] != "circular" else 3.1415 * recorte["r"] ** 2  # Subtrai a área não colocada

            print(f"Indivíduo {i + 1} tem área utilizada: {area_utilizada}.")
            self.aptidao.append(area_utilizada)  # Armazena a aptidão

    def selection(self):
        """Seleciona indivíduos via torneio para crossover."""
        print("Seleção de indivíduos via torneio...")
        new_population = []
        for _ in range(self.TAM_POP):
            ind1, ind2 = random.sample(range(self.TAM_POP), 2)
            melhor = ind1 if self.aptidao[ind1] > self.aptidao[ind2] else ind2
            new_population.append(self.POP[melhor])
        self.POP = new_population
        print("Seleção concluída.")

    def crossover(self):
        """Realiza crossover entre pares de indivíduos."""
        print("Crossover entre indivíduos...")
        for i in range(0, self.TAM_POP, 2):
            if i + 1 < self.TAM_POP:
                ponto = random.randint(1, len(self.POP[i]) - 1)
                self.POP[i][:ponto], self.POP[i+1][:ponto] = self.POP[i+1][:ponto], self.POP[i][:ponto]
                print(f"Crossover entre indivíduos {i} e {i + 1} no ponto {ponto}.")
        print("Crossover concluído.")

    def mutate(self, mutation_rate=0.1):
        """Aplica mutação trocando dois elementos aleatórios em um indivíduo."""
        print("Aplicando mutação...")
        for individuo in self.POP:
            if random.random() < mutation_rate:
                idx1, idx2 = random.sample(range(len(individuo)), 2)
                individuo[idx1], individuo[idx2] = individuo[idx2], individuo[idx1]
                print(f"Mutações aplicadas no indivíduo.")
        print("Mutação concluída.")

    def run(self):
        """Executa o algoritmo genético."""
        print(f"Executando o algoritmo genético por {self.numero_geracoes} gerações...")
        for geracao in range(self.numero_geracoes):
            print(f"Iniciando geração {geracao + 1}...")
            self.evaluate()
            self.selection()
            self.crossover()
            self.mutate()
            print(f"Geração {geracao + 1} concluída.")
        print("Algoritmo genético concluído.")
        self.optimized_layout = max(zip(self.POP, self.aptidao), key=lambda x: x[1])[0]
        return self.optimized_layout

    def optimize_and_display(self):
        """Exibe o layout inicial e o otimizado."""
        self.display_layout(self.initial_layout, title="Initial Layout - Genetic Algorithm")
        self.optimized_layout = self.run()
        self.display_layout(self.optimized_layout, title="Optimized Layout - Genetic Algorithm")
        return self.optimized_layout
