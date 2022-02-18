import sys
import socket
import threading

def main():
    socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    direccion_del_servidor = ('localhost', 10000)
    print('Iniciando servidor en {} puerto {}'.format(*direccion_del_servidor))
    socketServidor.bind(direccion_del_servidor)
    
    timeout = 300
    socketServidor.settimeout(timeout)
        
    socketServidor.listen(1)
    
    while True:
        print('Esperando conexión...')
        conexion, direccion_del_cliente = socketServidor.accept()
        def multihilo():
            try:
                print('Conexión desde', direccion_del_cliente)
                while True:
                    mensaje = conexion.recv(16)
                    print('Recibido {!r}'.format(mensaje))
                    if mensaje:
                        print('Enviando el mensaje de vuelta...')
                        conexion.sendall(mensaje)
                    else:
                        print('No se ha recibido un mensaje desde', direccion_del_cliente)
                        break
                    threading.Thread(target = multihilo).start()
            except socket.timeout():
                print('{} segundos sin recibir nada'.format(timeout))
                
            except:
                print('Error: {}'.format(sys.exc_info()[0]))
                raise
            
            finally:
               socketServidor.close()