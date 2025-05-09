import minimalmodbus
import serial
import time

# Настройка подключения
instrument = minimalmodbus.Instrument('COM1', 1)  # COM-порт и адрес устройства
instrument.serial.baudrate = 9600  # Скорость передачи
instrument.serial.parity = serial.PARITY_EVEN  # Четность
instrument.serial.stopbits = 2  # Стоп-биты
instrument.serial.bytesize = 8  # Биты данных
instrument.mode = minimalmodbus.MODE_RTU  # Режим RTU

# Включаем режим отладки
instrument.debug = True
minimalmodbus._print_out = True

# Адрес регистра в шестнадцатеричном формате
register_address = 0x0109

while True:
    try:
        # Чтение значения регистра (функция 3 - Read Holding Registers)
        value = instrument.read_register(register_address,
                                         functioncode=3,
                                         signed=False)  # unsigned int16

        print(f"BUILD_Y = {value}")

    except Exception as e:
        print(f"Ошибка: {e}")

    # Пауза 1 секунда
    time.sleep(1)
