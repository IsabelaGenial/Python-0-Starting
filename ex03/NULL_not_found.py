def NULL_not_found(object: any) -> int:

    typer = type(object)

    if str(object) == "None":
        print(f'Nothing : None {typer}')
        return 0
    elif typer is float and str(object) == "nan":
        print(f'Cheese:  NaN {typer}')
        return 0
    elif typer is int and object == 0:
        print(f'Zero : 0 {typer}')
        return 0
    elif typer is str and object == "":
        print(f'Empty : {typer}')
        return 0
    elif typer is bool and object is False:
        print(f'Fake : False {typer}')
        return 0

    print("Type not found")
    return 1
