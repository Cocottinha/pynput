import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device)  # Exibe todas as portas COM disponíveis

try:
    ser = serial.Serial('COM4', 115200, timeout=1)  # Altere para a porta correta
    print("Conectado com sucesso!")
    ser.close()
except serial.SerialException as e:
    print(f"Erro ao conectar: {e}")
