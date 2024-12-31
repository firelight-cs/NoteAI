import os

class FileEdit:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        print(f'Reading from {self.filename}...')
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f'File {self.filename} does not exist.')
        with open(self.filename, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, data, filename='cache/processed_text.txt'):
        target_file = filename if filename else self.filename
        if not os.path.exists(target_file):
            print(f'File {target_file} does not exist. Creating it...')
            open(target_file, 'w').close()
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(data)
        print(f'New text saved to: {target_file}')

    def append(self, data, filename=None):
        target_file = filename if filename else self.filename
        if not os.path.exists(target_file):
            print(f'File {target_file} does not exist. Creating it...')
            open(target_file, 'w').close()
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write(data)
        print(f'Text appended to: {target_file}')
