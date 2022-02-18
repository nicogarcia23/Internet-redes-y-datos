import sys
import socket

def main():
 
    
        maquina = 'localhost'
        puerto = 8050
        
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        timeout = 300
        socketCliente.settimeout(timeout)
        
        socketCliente.connect((maquina, puerto))
        print('Conectado al servidor')
        
        try:
            mensaje = 'Este es el mensaje que será repetido.'
            print (sys.stderr, 'enviando "%s"' % mensaje)
            socketCliente.sendall(mensaje)
    
            cantidad_recibida = 0
            cantidad_esperada = len(mensaje)
        
            while cantidad_recibida < cantidad_esperada:
                 data = socketCliente.recv(16)
                 cantidad_recibida += len(data)
                 print(sys.stderr, 'recibido "%s"' % data)

        
        except socket.timeout:
            print("{} segundos sin recibir nada.".format(timeout))
     
        except:
            print("Error: {}".format(sys.exc_info()[0]))
            raise
    
        finally:
            socketCliente.close()
        