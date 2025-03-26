import audioread
import sounddevice as sd
import numpy as np


import subprocess
import json


class Sound:
    def __init__(self):
        pass

    def change_micro(self, num):
        def list_microphones():
            command = ['powershell', '-Command',
                'Get-AudioDevice -List | Where-Object { $_.Type -eq "Recording" } | ConvertTo-Json']
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
                devices = json.loads(result.stdout)
                return devices if isinstance(devices, list) else [devices]
            except Exception as e:
                print(f"Ошибка: {e}")
                return []

        def set_default_microphone(device_id):
            command = ['powershell', '-Command', f'Set-AudioDevice -ID "{device_id}"']

            try:
                subprocess.run(command, check=True, shell=True)
                print("Микрофон успешно изменен!")
            except subprocess.CalledProcessError:
                print(f"Ошибка: Не удалось изменить микрофон. Запустите скрипт от имени администратора.")

        microphones = list_microphones()
        for idx, mic in enumerate(microphones):
            print(f"{idx + 1}. {mic['Name']} (ID: {mic['ID']})")
        selected_mic = microphones[num]
        set_default_microphone(selected_mic['ID'])

    def play_test(self):
        filename = 'C:\\Programming\\Python\\Projects\\SoundPad\\sound\\test.mp3'
        if filename.endswith('.mp3'):
            # Для MP3
            with audioread.audio_open(filename) as f:
                samplerate = f.samplerate
                raw_data = []
                for buffer in f:
                    raw_data.append(np.frombuffer(buffer, dtype=np.int16))
                audio_data = np.concatenate(raw_data)
                audio_data = audio_data.astype(np.float32) / 32768.0  # Нормализация
                if f.channels > 1:
                    audio_data = audio_data.reshape((-1, f.channels))
        else:
            raise ValueError("Формат файла не поддерживается!")

        print(1)
        self.change_micro(0)
        sd.play(audio_data, samplerate=samplerate, device=14)
        print(2)
        sd.wait()
        self.change_micro(1)
        print(3)


print(sd.query_devices())
s = Sound()
s.play_test()


# 1 - micro
# 4 - head