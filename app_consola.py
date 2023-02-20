def octetos_ip(ip):
    oct = ip.split(".")
    val = 1
    if len(oct) != 4:
        val = 0
    for octeto in oct:
        if not octeto.isdigit() or int(octeto) > 255:
            val = 0

    return oct, val

def clasificar(oct):
    p_octeto = int(oct[0])
    s_octeto = int(oct[1])

    tipo = 'privada'
    clase = ''
    # Rangos clases ip privadas
    if p_octeto == 10:
        clase = 'A'
    elif p_octeto == 172 and 16 <= s_octeto <= 31:
        clase = 'B'
    elif p_octeto == 192 and s_octeto == 168:
        clase = 'C'
    else:
        tipo = 'publica'
    
    # Rangos clases ip publicas
    if 0 <= p_octeto <= 126:
        clase = 'A'
    if 128 <= p_octeto <= 191:
        clase = 'B'
    if 192 <= p_octeto <= 223:
        clase = 'C'
    if 224 <= p_octeto <= 239:
        clase = 'D'
    if 240 <= p_octeto <= 254:
        clase = 'E'

    resultado = f'IP {tipo} de clase {clase}'
    return resultado

print("Ingrese una direccion IP: ")
ip = str(input())
ip = octetos_ip(ip)
#ip = octetos_ip('192.169.0.0')
if ip[1] == 0:
    print('Direccion ip no valida. :(')
else:
    print(clasificar(ip[0]))