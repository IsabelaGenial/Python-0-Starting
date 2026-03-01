def all_thing_is_obj(object: any) -> int:
    # Obtemos o tipo do objeto
    obj_type = type(object)

    # Verificamos o nome do tipo para a lógica condicional
    type_name = obj_type.__name__

    if type_name == "list":
        print(f"List : {obj_type}")
    elif type_name == "tuple":
        print(f"Tuple : {obj_type}")
    elif type_name == "set":
        print(f"Set : {obj_type}")
    elif type_name == "dict":
        print(f"Dict : {obj_type}")
    elif type_name == "str":
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
