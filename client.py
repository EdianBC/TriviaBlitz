import socket
import keyboard

# Función para conectarse al servidor del host
def client():
    server_ip = input("Ingresa la IP del host: ")
    port = 12345  # Puerto del servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    print("Conectado al host. Esperando la autorización para responder...")

    # Esperar hasta que se presione la tecla espacio
    while True:
        if keyboard.is_pressed('space'):
            client_socket.sendall('SPACE_PRESSED'.encode())
            print("Solicitaste responder.")
            time.sleep(0.5)  # Para evitar múltiples envíos involuntarios

if __name__ == '__main__':
    client()
