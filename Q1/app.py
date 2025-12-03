"""

def calcular_media(notas, pesos):
    
    # 1. Defeito Lógico 1 (Cálculo Incorreto): Fórmula da média ponderada errada
    # 2. Defeito Lógico 2 (Risco de Falha): Não trata divisão por zero
    
    p1 = pesos[0]
    p2 = pesos[1]
    p3 = pesos[2]

    # CÁLCULO INCORRETO
    soma_pesos = p1 + p2 + p3
    media = (notas[0] + notas[1] + notas[2]) / soma_pesos

    return media

# 3. Defeito de Estilo 1 (Magic Numbers e Nomenclatura Ruim):
dados_notas = [7.0, 8.5, 9.0]
valores_importantes = [2, 3, 5]

resultado = calcular_media(dados_notas, valores_importantes)

# 4. Defeito de Estilo 2 (Formato de Output Ruim):
print("O resultado da media é: " + str(resultado))

"""

"""
ERROS ENCONTRADOS NO CÓDIGO 'calcula_notas.py':

1. ❌ ERRO LÓGICO CRÍTICO (Funcionalidade):
   - O cálculo da média ponderada na linha 'media = ...' está incorreto. O numerador 
     apenas soma as notas, **esquecendo-se de multiplicar cada nota pelo seu respectivo peso**.
     (Ex: O correto seria (n1*p1 + n2*p2 + n3*p3) / soma_pesos).

2. 💥 ERRO LÓGICO DE RESILIÊNCIA (Risco de Falha):
   - Falta de tratamento para a divisão por zero. Se 'soma_pesos' for 0, o programa
     irá parar com um 'ZeroDivisionError' em tempo de execução.

3. 📝 ERRO DE ESTILO/MANUTENÇÃO (Nomenclatura e Clareza):
   - **Nomenclatura Vaga:** Variável 'valores_importantes' não é clara e não indica que são pesos.
   - **Magic Numbers:** Os valores literais ([7.0, 8.5, 9.0] e [2, 3, 5]) não são definidos
     como constantes globais, dificultando sua alteração futura e compreensão.
"""


# REVISÃO DE CÓDIGO - VERSÃO CORRIGIDA

def calcular_media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        return "Erro: O número de notas deve ser igual ao número de pesos."

    soma_pesos = sum(pesos)
    
    if soma_pesos == 0:
        return "Erro: A soma dos pesos é zero, impossível calcular a média (divisão por zero)."

    soma_ponderada = sum(nota * peso for nota, peso in zip(notas, pesos))

    media_corrigida = soma_ponderada / soma_pesos
    
    return media_corrigida



NOTAS_DO_ALUNO = [7.0, 8.5, 9.0]
PESOS_DAS_AVALIACOES = [2, 3, 5]

resultado_final = calcular_media_ponderada(NOTAS_DO_ALUNO, PESOS_DAS_AVALIACOES)


print(f"Notas: {NOTAS_DO_ALUNO}, Pesos: {PESOS_DAS_AVALIACOES}")
print(f"A média ponderada correta é: {resultado_final:.2f}")



