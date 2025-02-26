import serial
import time

# Configuração da porta serial
ser = serial.Serial('COM4', 115200, timeout=1)  # Ajuste para a porta correta
time.sleep(2)  # Aguarde a inicialização da porta serial

def send_gcode(command):
    """ Envia um comando G-code e imprime a resposta """
    ser.write((command + '\n').encode())  
    time.sleep(0.5)  # Tempo de espera para resposta
    response = ser.readlines()  # Lê todas as linhas de resposta
    for line in response:
        print(line.decode().strip())  # Exibe a resposta no terminal

try:
    send_gcode("G90")   # Modo absoluto
    send_gcode("G1 X100 F100")  # Move o motor para X=10
except KeyboardInterrupt:
    print("Movimentação interrompida")
finally:
    ser.close()  # Fecha a conexão serial
