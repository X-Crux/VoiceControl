import time
from pathlib import Path
import os
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)


class ComputerControl:
    path = 'data'
    local_path = resource_path(path)

    def control_computer(self, action: str):
        if action.startswith('create file'):
            _, _, extension, amount = action.split(' ')
            self.create_files(extension, amount)
        elif action.startswith('remove file'):
            _, _, extension, amount = action.split(' ')
            self.remove_files(extension, amount)
        elif action.startswith('exit app'):
            self.close_app()
        elif action == 'command4':
            self.command4()
        elif action == 'command5':
            self.command5()
        elif action == 'command6':
            self.command6()
        else:
            print(f'Команда не распознана > {action}')

    def create_files(self, extension, amount):

        for i in range(int(amount)):
            f = open(f"{self.local_path}/{i}.{extension}", "w")
            f.close()

        print(f'Выполнена команда: create_files({extension}, {amount})')

    def remove_files(self, extension, amount):
        if amount == 'all':
            for file in Path(self.local_path).glob(f'*.{extension}'):
                print(f"Удаление файла {file}")
                try:
                    file.unlink()
                except Exception:
                    with open(file, mode='r'):
                        pass
                    file.unlink()
        else:
            for file in Path(self.local_path).glob(f'{amount}.{extension}'):
                print(f"Удаление файла {file}")
                try:
                    file.unlink()
                except Exception:
                    with open(file, mode='r'):
                        pass
                    file.unlink()

        print(f'Выполнена команда: remove_files({extension}, {amount})')

    def close_app(self):
        print('Выход из программы...')
        time.sleep(3)
        sys.exit(0)

    def command4(self):
        print('Выполнена команда 4')

    def command5(self):
        print('Выполнена команда 5')

    def command6(self):
        print('Выполнена команда 6')
