"""Task2_2
Створіть два класи Directory (тека) і File (файл) з типами (анотацією).
Клас Directory має мати такі поля:
·        назва (name типу str);
·        батьківська тека (root типу Directory);
·        список файлів (список типу files, який складається з екземплярів File);
·        список підтек (список типу sub_directories, який складається з
екземплярів Directory).

Клас Directory має мати такі методи:
·        додавання теки до списку підтек (add_sub_directory, який приймає
екземпляр Directory та присвоює поле root для приймального екземпляра);
·        видалення теки зі списку підтек (remove_sub_directory, який приймає
екземпляр Directory та обнуляє поле root. Метод також видаляє теку зі списку
sub_directories);
·        додавання файлу в теку (add_file, який приймає екземпляр File і
присвоює йому поле directory – див. клас File нижче);
·        видалення файлу з теки (remove_file, який приймає екземпляр File
та обнуляє у нього поле directory. Метод видаляє файл зі списку files).

Клас File має мати такі поля:
·        назва (name типу str);
·        тека (Directory типу Directory).
"""

from typing import Optional


class File:
    def __init__(self, name: str,
                 directory: Optional['Directory'] = None) -> None:

        self.name = name
        self.directory = directory


class Directory:
    def __init__(self,
                 name: str,
                 root: Optional['Directory'] = None,
                 files: Optional[list[File]] = None,
                 sub_directories: Optional[list['Directory']] = None) -> None:

        self.name = name                                # Directory_name
        self.root = root                                # Parental directory
        # List of files in current directory
        self.files = [] if files is None else files
        # List of directories in current directory
        self.sub_directories = [] if sub_directories is None else sub_directories


    def add_sub_directory(self, new_sub_directory: 'Directory') ->  None:
        new_sub_directory.root = self.name
        self.sub_directories.append(new_sub_directory.name)

    def remove_sub_directory(self, directory_to_remove: 'Directory') -> None:
        if directory_to_remove.root:
            directory_to_remove.root = None
        if directory_to_remove.name in self.sub_directories:
            self.sub_directories.remove(directory_to_remove.name)

    def add_file(self, new_file: File) ->  None:
        new_file.directory = self.name
        self.files.append(new_file.name)

    def remove_file(self, file_to_remove: File) -> None:
        if file_to_remove.directory:
            file_to_remove.directory = None
        if file_to_remove.name in self.files:
            self.files.remove(file_to_remove.name)


if __name__ == '__main__':

    # create directories and files
    directory1 = Directory(name='d1')
    directory2 = Directory(name='d2')
    directory3 = Directory(name='d3')
    file1 = File('f1')
    file2 = File('f2')

    print('Check directory1.add_sub_directory(directory2),(directory3): ')
    directory1.add_sub_directory(directory2)
    directory1.add_sub_directory(directory3)
    print(f'directory1.sub_directories: {directory1.sub_directories}')
    print(f'directory2.root: {directory2.root}\n')

    print('Check directory1.remove_sub_directory(directory2): ')
    directory1.remove_sub_directory(directory2)
    print(f'directory1.sub_directories: {directory1.sub_directories}')
    print(f'directory2.root: {directory2.root}\n')

    print('Check directory1.add_file(file1), (file2): ')
    directory1.add_file(file1)
    directory1.add_file(file2)
    print(f'directory1.files: {directory1.files}')
    print(f'file1.directory: {file1.directory}\n')

    print('Check directory1.remove_file(file1)')
    directory1.remove_file(file1)
    print(f'directory1.files: {directory1.files}')
    print(f'file1.directory: {file1.directory}')
