from datetime import datetime

# Define a data de início (Ex: 1º de Janeiro de 1970)
data_inicio = datetime(1970, 1, 1)
agora = datetime.now()

# A subtração gera um objeto 'timedelta'
diferenca = agora - data_inicio

# Converte a diferença total para segundos
segundos_passados = diferenca.total_seconds()


print(f"Seconds since January 1, 1970: {segundos_passados:,.3f} or \
       {segundos_passados:.2e} in scientific notation")
print(agora.strftime("%b %d %Y"))
