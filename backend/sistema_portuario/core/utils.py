def validar_imo(imo):
    """
    Este é constituído por um número de seis dígitos sequenciais únicos
    seguido por um dígito de verificação. A integridade de um número IMO pode
    ser verificada usando o seu dígito de verificação. Isto é feito multiplicando
    cada um dos primeiros seis dígitos por um fator de 2 para 7 correspondente à
    posição da direita para a esquerda. O dígito mais à direita dessa soma é o dígito
    de verificação. Por exemplo, para IMO 9074729:
    (9×7) + (0×6) + (7x5) + (4×4) + (7×3) + (2×2) = 139
    """
    if len(imo) != 7:
        return False

    try:
        # separar digitos posicionais do verificador em ordem reversa
        # por exemplo "3074729", pos ficará 274703, verificador igual a 9
        pos = map(int, imo[-2::-1])
        verificador = imo[-1]
        soma = sum(p * i for p, i in enumerate(pos, start=2))
    except ValueError:
        return False

    return str(soma)[-1] == verificador
