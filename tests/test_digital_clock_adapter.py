from datetime import datetime

import pytest

from adapters import DigitalClockAdapter
from clocks import AnalogClock
from consts import DayNightDivision
from interfaces import BaseDigitalClock


def make_adapter() -> DigitalClockAdapter:
    return DigitalClockAdapter(AnalogClock())


def test_adapter_is_digital_clock() -> None:
    assert isinstance(make_adapter(), BaseDigitalClock)


@pytest.mark.parametrize(
    "value",
    [
        datetime(2026, 11, 12, 3, 7, 42),
        datetime(2026, 11, 12, 0, 0, 0),
        datetime(2026, 11, 12, 12, 0, 0),
        datetime(2026, 11, 12, 11, 59, 59),
        datetime(2026, 11, 12, 23, 59, 59),
        datetime(2024, 2, 29, 12, 30, 15),
    ],
)
def test_adapter_round_trip(value: datetime) -> None:
    adapter = make_adapter()
    adapter.set_date_time(value)
    assert adapter.get_date_time() == value


def test_adapter_converts_to_angles() -> None:
    adapter = make_adapter()
    adapter.set_date_time(datetime(2026, 11, 12, 15, 30, 15))

    assert adapter._clock.get_hour_angle() == 90.0
    assert adapter._clock.get_minute_angle() == 180.0
    assert adapter._clock.get_second_angle() == 90.0
    assert adapter._clock.get_day_night_division() is DayNightDivision.PM


def test_adapter_midnight_is_am() -> None:
    adapter = make_adapter()
    adapter.set_date_time(datetime(2026, 11, 12, 0, 0, 0))

    assert adapter._clock.get_hour_angle() == 0.0
    assert adapter._clock.get_day_night_division() is DayNightDivision.AM


def test_adapter_noon_is_pm() -> None:
    adapter = make_adapter()
    adapter.set_date_time(datetime(2026, 11, 12, 12, 0, 0))

    assert adapter._clock.get_hour_angle() == 0.0
    assert adapter._clock.get_day_night_division() is DayNightDivision.PM
