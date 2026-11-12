from datetime import datetime
from adapters import DigitalClockAdapter
from clocks import AnalogClock
from services import ClockFormatter, ClockHistory

class ClockFacade:

    def __init__(self) -> None:
        self._adapter = DigitalClockAdapter(AnalogClock())
        self._formatter = ClockFormatter()
        self._history = ClockHistory()

    def set_date_time(self, date: datetime) -> None:
        self._adapter.set_date_time(date)
        self._history.add(date)

    def get_date_time(self) -> datetime:
        return self._adapter.get_date_time()

    def get_formatted(self) -> str:
        return self._formatter.format(self._adapter.get_date_time())

    def get_history(self) -> tuple[datetime, ...]:
        return self._history.all()
