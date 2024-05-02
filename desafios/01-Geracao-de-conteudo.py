# Dicionário associando características aos modelos Claude 3
caracteristicas_modelos = {
    "automatizar tarefas": "Claude 3 Opus",
    "pesquisa e desenvolvimento": "Claude 3 Opus",
    "resposta rápida e capacidade de resposta quase instantânea": "Claude 3 Haiku",
    "motores de chatbots de lojas": "Claude 3 Haiku",
    "moderação de conteúdo": "Claude 3 Haiku",
    "processamento de tarefas mais básicas": "Claude 3 Haiku",
    "raciocínio cuidadoso": "Claude 3 Sonnet",
    "processamento de dados": "Claude 3 Sonnet",
    "aplicações de vendas": "Claude 3 Sonnet",
    "extração de texto de imagens": "Claude 3 Sonnet",
    "equilíbrio ideal entre inteligência e velocidade": "Claude 3 Sonnet",
   
}

def encontrar_modelo(caracteristica_fornecida):
    """
    Função para encontrar o modelo Claude 3 correspondente a uma característica fornecida.
    """
    # Iterar sobre cada chave e valor no dicionário caracteristicas_modelos
    for caracteristica, modelo in caracteristicas_modelos.items():
        # Verificar se a palavra-chave (característica) está contida na característica fornecida (ignorando maiúsculas/minúsculas)
        if caracteristica.lower() in caracteristica_fornecida.lower():
            # Se encontrada, retornar o modelo correspondente
            return modelo
    
    # Se não encontrada, retornar uma mensagem indicando que o modelo não foi encontrado
    return "Modelo não encontrado."

# Entrada do usuário
caracteristica_fornecida = input()

# Encontrar e imprimir o modelo correspondente
modelo_correspondente = encontrar_modelo(caracteristica_fornecida)
print(modelo_correspondente)
