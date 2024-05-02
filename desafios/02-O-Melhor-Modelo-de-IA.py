# Definindo a classe ModeloIA para representar os modelos de IA com suas características
class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades
    
    def __str__(self):
        return self.nome

# Lista de modelos de IA com suas características pontuadas na descrição:
modelos = [
    ModeloIA("Claude 3 Opus", 9, 10, 5, ["Pesquisa", "Desenvolvimento Acelerado"]),
    ModeloIA("Claude 3 Sonnet", 8, 5, 7, ["Codificação", "Recuperação de informações"]),
    ModeloIA("Claude 3 Haiku", 7, 9, 6, ["Velocidade", "Resumo de dados não estruturados"])
]

# Função para recomendar um modelo de IA com base nas características fornecidas
def recomendar_modelo(caracteristicas):
    modelo_recomendado = None
    capacidades_usuario = [capacidade.lower() for capacidade in caracteristicas['Capacidades']]

      # Itera sobre os modelos para encontrar o mais adequado
    for modelo in modelos:
        capacidades_modelo = [capacidade.lower() for capacidade in modelo.capacidades]
        
      # Verifica se todas as capacidades do modelo estão presentes nas características fornecidas
        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo
              
    # Retorna o modelo recomendado ou uma mensagem indicando que nenhum modelo foi encontrado
    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."
  
# Função para gerar uma explicação para o modelo recomendado
def gerar_explicacao(modelo, caracteristicas):
    if isinstance(modelo, ModeloIA):
        explicacao = f"O {modelo.nome} é o modelo recomendado."
        return explicacao
    else:
        return modelo

# Função para solicitar características desejadas ao usuário
def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(input())
    caracteristicas['Velocidade'] = int(input())
    caracteristicas['Custo'] = int(input())
    capacidades = input().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
    return caracteristicas

# Solicita características ao usuário
caracteristicas_entrada = obter_caracteristicas()
# Recomenda um modelo com base nas características fornecidas
melhor_modelo = recomendar_modelo(caracteristicas_entrada)
# Gera uma explicação para o modelo recomendado e a imprime
explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)

print(explicacao)
