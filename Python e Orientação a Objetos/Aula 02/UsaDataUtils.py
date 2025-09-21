from DataUtils import DataUtils

# Validando datas
print(DataUtils.validar_data("2025-09-13"))  # True
print(DataUtils.validar_data("2025-02-30"))  # False

# Calculando diferença de dias
dias = DataUtils.dias_entre_datas("2025-09-01", "2025-09-13")
print(f"Dias entre datas: {dias}")  # 12

# Obtendo a data atual
print(f"Hoje é: {DataUtils.hoje()}")