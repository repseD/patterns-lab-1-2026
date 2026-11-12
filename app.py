from datetime import datetime

from facades import ClockFacade


def main() -> None:
    facade = ClockFacade()

    facade.set_date_time(datetime.now())
    print(f"Сейчас: {facade.get_date_time()}")
    print(f"Форматировано: {facade.get_formatted()}")

    facade.set_date_time(datetime(2026, 11, 12, 12, 0, 0))
    print(f"Полдень: {facade.get_date_time()}")

    print("История изменений:")
    for item in facade.get_history():
        print(f"  {item}")


if __name__ == "__main__":
    main()
