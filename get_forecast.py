from datetime import datetime

import pytz


class GetForeCast:

    @staticmethod
    def get_current_date_and_days_difference(place, future_date):
        ist_time = pytz.timezone(f'Asia/{place}')
        time_now = datetime.now(ist_time)
        datetime_ist = time_now.strftime("%Y-%m-%d %H:%M:%S %p")
        current_date = time_now.strftime("%Y-%m-%d")
        days_difference = datetime.strptime(future_date, "%Y-%m-%d").date() - \
                          datetime.strptime(current_date, "%Y-%m-%d").date()
        date_and_difference = [datetime_ist, days_difference.days]
        return date_and_difference
