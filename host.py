import socket
import threading
import time

# Lista para almacenar el orden de los concursantes que piden responder
contestants_queue = []

# Función para manejar a los concursantes
def handle_contestant(conn, addr):
    print(f"Conexión establecida con {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()
            if data == 'SPACE_PRESSED':
                print(f"El concursante {addr} solicitó responder")
                contestants_queue.append(addr)
        except:
            conn.close()
            break

# Función principal del servidor
def server():
    host = socket.gethostbyname(socket.gethostname())  # Obtener la IP local
    port = 12345  # Puerto para la conexión

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    # Hilo para controlar la cola de concursantes
    def manage_queue():
        while True:
            input("Presiona espacio para permitir las respuestas: ")
            if contestants_queue:
                print("Orden de respuestas:")
                for i, contestant in enumerate(contestants_queue):
                    print(f"{i + 1}. {contestant}")
                contestants_queue.clear()
            else:
                print("Nadie ha solicitado responder aún.")

    # Inicia el manejo de la cola
    queue_thread = threading.Thread(target=manage_queue)
    queue_thread.start()

    # Esperar conexiones de concursantes
    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_contestant, args=(conn, addr)).start()

if __name__ == '__main__':
    server()
