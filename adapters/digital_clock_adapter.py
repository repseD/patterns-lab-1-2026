from datetime import datetime
from clocks import AnalogClock
from consts import DayNightDivision
from interfaces import BaseDigitalClock

_DEGREES_PER_HOUR = 30.0
_DEGREES_PER_MINUTE = 6.0

class DigitalClockAdapter(BaseDigitalClock):
    def __init__(self, clock: AnalogClock) -> None:
        self._clock = clock

    def set_date_time(self, date: datetime) -> None:
        self._clock.set_date_time(
            year=date.year,
            month=date.month,
            day=date.day,
            hour_angle=(date.hour % 12) * _DEGREES_PER_HOUR,
            minute_angle=date.minute * _DEGREES_PER_MINUTE,
            second_angle=date.second * _DEGREES_PER_MINUTE,
            day_night_division=DayNightDivision.AM if date.hour < 12 else DayNightDivision.PM,
        )

    def get_date_time(self) -> datetime:
        hour = int(self._clock.get_hour_angle() / _DEGREES_PER_HOUR) % 12
        if self._clock.get_day_night_division() is DayNightDivision.PM:
            hour += 12
        return datetime(
            self._clock.get_year(),
            self._clock.get_month(),
            self._clock.get_day(),
            hour,
            int(self._clock.get_minute_angle() / _DEGREES_PER_MINUTE),
            int(self._clock.get_second_angle() / _DEGREES_PER_MINUTE),
        )
