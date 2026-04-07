import socket

"/* Le pedimos al usuario la dirección IP que vamos a escanear */"

ip = input("Ingrese la dirección IP a escanear: ")

"/* indicamos la cantidad de puertos de 1 a 65535 */"
for puerto in range(1,65535): 
    "/* espeficiamos que usamos IPV4 (EJ: xxx.xxx.1.1) */"
    "/* Sock stream indica que usamos protocolo TCP */"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    "/* Usamos el socket para conectarnos a un puerto y ver está abierto o no */"
    result = sock.connect_ex((ip, puerto))
    if result == 0:
        print("Puerto Abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto Cerrado: " + str(puerto))