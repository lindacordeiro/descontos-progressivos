def main():
    valor_compra = float(input("Digite o valor da compra: "))

    if valor_compra < 200:
        valor_final = valor_compra * 0.95
    elif valor_compra < 300:
        valor_final = valor_compra * 0.90
    else:
        valor_final = valor_compra * 0.85

    print("______________________________________________")
    print(f"O valor da compra foi de R${valor_compra:.2f}")
    print(f"O valor com desconto e R${valor_final:.2f}")

main()