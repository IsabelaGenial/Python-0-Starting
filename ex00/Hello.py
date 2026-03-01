ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# O foco aqui não é apenas "mudar strings",
# mas mostrar as propriedades fundamentais das
# estruturas de dados nativas do Python: a
# mutabilidade da List, a imutabilidade
# da Tuple, a natureza não ordenada do Set e o mapeamento Key-Value do Dict

# alteração de valores da ft_list
ft_list[1] = "World!"

# alteração de valores de tupla
ft_tuple = ("Hello", "Brasil!")


# alterando valores no set
ft_set.discard("tutu!")
ft_set.add("Sao Paulo!")

# alterando valores em dic
ft_dict['Hello'] = "42SaoPaulo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
