import matplotlib.pyplot as plt

# Dados fornecidos
interacoes = list(range(1, 17))
tempos = [409.1087040901184, 526.8619549274445, 527.4418110847473, 400.1560699939728, 388.58452320098877, 406.71590185165405, 377.5452048778534, 386.74986386299133, 357.4903299808502, 378.7365400791168, 393.1876859664917, 419.67157793045044, 397.9976861476898, 402.20265102386475, 416.31346917152405, 393.1369969844818]
media = 411.368810698

# Plot dos dados
plt.plot(interacoes, tempos, label='Tempo')
plt.axhline(y=media, color='r', linestyle='--', label='Média')

# Adiciona rótulos aos eixos e título ao gráfico
plt.xlabel('Número da Interação')
plt.ylabel('Tempo')
plt.title('Tamanho 10^6 com lista')

# Adiciona uma legenda
plt.legend()

# Exibe o gráfico
plt.show()
