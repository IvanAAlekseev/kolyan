import argparse
import sys


class DependencyVisualizer:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Dependency Graph Visualizer')
        self.setup_arguments()

    def setup_arguments(self):
        """Настройка параметров командной строки"""
        self.parser.add_argument('--package', '-p', required=True,
                                 help='Имя анализируемого пакета')
        self.parser.add_argument('--repository', '-r', required=True,
                                 help='URL-адрес репозитория или путь к файлу тестового репозитория')
        self.parser.add_argument('--test-mode', '-t', action='store_true',
                                 help='Режим работы с тестовым репозиторием')
        self.parser.add_argument('--version', '-v',
                                 help='Версия пакета')
        self.parser.add_argument('--output', '-o', default='graph.png',
                                 help='Имя сгенерированного файла с изображением графа')
        self.parser.add_argument('--ascii-tree', '-a', action='store_true',
                                 help='Режим вывода зависимостей в формате ASCII-дерева')
        self.parser.add_argument('--filter', '-f',
                                 help='Подстрока для фильтрации пакетов')

    def validate_parameters(self, args):
        """Валидация параметров"""
        errors = []

        if not args.package:
            errors.append("Имя пакета не может быть пустым")

        if not args.repository:
            errors.append("URL репозитория не может быть пустым")

        if args.version and not isinstance(args.version, str):
            errors.append("Версия пакета должна быть строкой")

        if args.filter and not isinstance(args.filter, str):
            errors.append("Подстрока для фильтрации должна быть строкой")

        return errors

    def print_parameters(self, args):
        """Вывод всех параметров в формате ключ-значение"""
        print("=== Параметры конфигурации ===")
        params = {
            'Имя анализируемого пакета': args.package,
            'URL-адрес репозитория': args.repository,
            'Режим работы с тестовым репозиторием': 'Включен' if args.test_mode else 'Выключен',
            'Версия пакета': args.version if args.version else 'Не указана',
            'Имя сгенерированного файла': args.output,
            'Режим вывода ASCII-дерева': 'Включен' if args.ascii_tree else 'Выключен',
            'Подстрока для фильтрации': args.filter if args.filter else 'Не указана'
        }

        for key, value in params.items():
            print(f"{key}: {value}")
        print("===============================")

    def run(self):
        """Основной метод запуска приложения"""
        try:
            # Парсинг аргументов командной строки
            args = self.parser.parse_args()

            # Валидация параметров
            errors = self.validate_parameters(args)
            if errors:
                print("Ошибки валидации параметров:")
                for error in errors:
                    print(f"  - {error}")
                sys.exit(1)

            # Вывод параметров (требование этапа)
            self.print_parameters(args)

            print("Приложение успешно запущено с указанными параметрами!")

        except argparse.ArgumentError as e:
            print(f"Ошибка в аргументах командной строки: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
            sys.exit(1)


if __name__ == "__main__":
    app = DependencyVisualizer()
    app.run()