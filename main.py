from src.file_processing import read_csv_operations, read_excel_operations
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import load_operations
from src.widget import get_date, mask_account_card

# from src.external_api import convert_currency


def main() -> None:
    """Основная функция программы"""

    # 1. Выбор источника данных

    while True:
        choice = input(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
            ":"
        )
        if choice == "1":
            file_path = "data/operations.json"
            print("Для обработки выбран JSON-файл")
            operations = load_operations(file_path)
            break
        elif choice == "2":
            file_path = "data/transactions.csv"
            print("Для обработки выбран csv файл")
            operations = read_csv_operations(file_path)
            break
        elif choice == "3":
            file_path = "data/transactions_excel.xlsx"
            print("Для обработки выбран XLSX-файл.")
            operations = read_excel_operations(file_path)
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

    if not operations:
        print("Не удалось загрузить транзакции. Проверьте наличие файла.")
        return

    print(f"Загружено {len(operations)} операций")
    print()

    # 2. Фильтр по статусу

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()

        if status in valid_statuses:
            print(f"Операция отфильтрована по статусу {status}")
            operations = filter_by_state(operations, status)
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    if not operations:
        print("Не найдено ни одной операции с таким статусом.")
        return

    print()

    # 3. Сортировка по дате

    while True:
        sort_data_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
        if sort_data_choice in ["да", "нет"]:
            if sort_data_choice == "да":
                while True:
                    order = input(
                        "Отсортировать по возрастанию или по убыванию? "
                        "(введите 'по возрастанию' или 'по убыванию'): "
                    ).lower()
                    if "по возрастанию" in order:
                        operations = sort_by_date(operations, reverse=False)
                        print("Операции отсортированы по возрастанию даты.")
                        break
                    elif "по убыванию" in order:
                        operations = sort_by_date(operations, reverse=True)
                        print("Операции отсортированы по убыванию даты.")
                        break
                    else:
                        print("Пожалуйста, введите как отсортировать: 'по возрастанию' или 'по убыванию'?")
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')
    print()
    # 4. Фильтрация только рублевых транзакций да/нет
    while True:
        rub_choice = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
        if rub_choice in ["да", "нет"]:
            if rub_choice == "да":
                rub_operations = []
                for operation in operations:
                    currency = operation.get("currency", "RUB")
                    if "operationAmount" in operation:
                        currency = operation["operationAmount"].get("currency", {}).get("code", "RUB")
                    if currency.upper() == "RUB":
                        rub_operations.append(operation)
                operations = rub_operations

                if not operations:
                    print("Не найдено ни одной рублевой транзакции.")
                    return
                print(f"Отфильтровано {len(operations)} рублевых транзакций.")
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')
    print()

    # 5. Поиск по описанию

    while True:
        search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
        if search_choice in ["да", "нет"]:
            if search_choice == "да":
                search_string = input("Введите слово для поиска в описании: ")
                if search_string:
                    operations = process_bank_search(operations, search_string)
                    if not operations:
                        print("Не найдено транзакций, содержащих указанное слово.")
                        return
                    print(f"Найдено {len(operations)} транзакций по запросу '{search_string}'")
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')
    print()

    # 6. Вывод результата

    print("Распечатываю итоговый список транзакций...\n")

    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n")
        return

    print(f"Всего банковских операций в выборке: {len(operations)}")

    for operation in operations:
        # Форматируем дату
        date = operation.get("date", "")
        formatted_date = get_date(date) if date else "Дата не указана"

        # Получаем описание
        description = operation.get("description", "Описание отсутствует")

        # Получаем сумму и валюту
        amount = operation.get("amount")
        currency = operation.get("currency", "RUB")

        if "operationAmount" in operation:
            amount = operation["operationAmount"].get("amount", 0)
            currency = operation["operationAmount"].get("currency", {}).get("code", "RUB")

        # Без конвертации
        if currency == "RUB":
            amount_display = f"{amount} руб."
        else:
            amount_display = f"{amount} {currency}"

        # # Конвертация валюты
        # if currency in ["USD", "EUR"]:
        #     amount_in_rub = convert_currency({"amount": amount, "currency": currency})
        #     if amount_in_rub > 0:
        #         amount_display = f"{amount_in_rub} руб."
        #     else:
        #         amount_display = f"{amount} {currency}"
        # else:
        #     amount_display = f"{amount} руб."

        # Маскируем данные
        from_info = operation.get("from", "")
        to_info = operation.get("to", "")

        from_masked = mask_account_card(from_info) if from_info else ""
        to_masked = mask_account_card(to_info) if to_info else ""

        print(f"\n{formatted_date} {description}")

        if from_info and to_info:
            print(f"{from_masked} -> {to_masked}")
        elif to_info:
            print(f"{to_masked}")

        print(f"Сумма: {amount_display}")


if __name__ == "__main__":
    main()
