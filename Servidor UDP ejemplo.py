import sys
import socket

def main():
    if len(sys.argv) != 2:
        print("Formato Servidor UDP <puerto>")
        sys.exit()
    try:
        puerto = int(sys.argv[1])
        socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketServidor.bind(("",puerto))
        
        timeout = 300
        socketServidor.settimeout(timeout)
        
        print("Iniciando servidor en PUERTO: ",puerto)
        
        mensaje,direccion = socketServidor.recvfrom(4096)
        print("Recibido mensaje: {} de: {}:{}".format(mensaje.decode('UTF-8'),direccion[0],direccion[1]))
        socketServidor.sendto(mensaje,direccion)
            
        if __name == "__main__":
            main()
        
    except socket.timeout:
        print("{} segundos sin recibir nada.".format(timeout))
        
    except:
        print("Error: {}".format(sys.exc_info()[0]))
        
    finally:
        socketServidor.close()