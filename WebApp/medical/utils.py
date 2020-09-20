from datetime import date, timedelta
from calendar import HTMLCalendar
from .models import Wizyta


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formatowanie dnia jako jednej komórki w tabeli
    # filtrowanie wizyt
    def formatday(self, day, wizyty):
        wizyty_na_dzien = wizyty.filter(day__day=day)
        d = ''
        for wizyta in wizyty_na_dzien:
            d += f'<p><a href="update"> {wizyta.start_time}</a></p>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formatowanie tygodni w wierszu
    def formatweek(self, theweek, wizyty):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, wizyty)
        return f'<tr> {week} </tr>'

    # formatowanie miesiaca jako tabela
    # filtrowanie wizyt po roku i miesiącu
    def formatmonth(self, withyear=True):
        wizyty = Wizyta.objects.filter(day__year=self.year, day__month=self.month)

        cal = f'<table border="0" cellpadding="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, wizyty)}\n'
        return cal