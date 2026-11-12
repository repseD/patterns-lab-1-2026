from datetime import datetime

from facades import ClockFacade


def test_facade_round_trip() -> None:
    facade = ClockFacade()
    value = datetime(2026, 11, 12, 23, 59, 59)

    facade.set_date_time(value)
    assert facade.get_date_time() == value


def test_facade_formatted() -> None:
    facade = ClockFacade()
    facade.set_date_time(datetime(2026, 11, 12, 12, 30, 15))

    assert facade.get_formatted() == "12.11.2026 12:30:15"


def test_facade_history_stores_all_values() -> None:
    facade = ClockFacade()
    first = datetime(2026, 11, 12, 10, 0, 0)
    second = datetime(2026, 11, 12, 20, 30, 15)

    facade.set_date_time(first)
    facade.set_date_time(second)

    assert facade.get_history() == (first, second)


def test_facade_history_empty_by_default() -> None:
    assert ClockFacade().get_history() == ()
