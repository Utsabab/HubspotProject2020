import dateutil.parser as parser
import datetime


class Process:

    @staticmethod
    def process_data(list_of_partners):
        """For each partner finds the start date with the most numbers of attendees. Returns the partner, list of
        attenders, and start date.
        """
        countries = []
        country_to_events = {}

        for each in list_of_partners["partners"]:
            if each["country"] not in country_to_events:
                country_to_events[each["country"]] = {}

            for date in each["availableDates"]:
                if date not in country_to_events[each["country"]]:
                    country_to_events[each["country"]][date] = []
                country_to_events[each["country"]][date].append(each)

        for curr_country, dates_to_each in country_to_events.items():
            sorted_dates = sorted(dates_to_each.keys())

            total_attenders = float('-inf')
            event_start_day = None
            most_attenders = []

            for ind in range(len(sorted_dates[:-1])):

                today = sorted_dates[ind]
                tomorrow = sorted_dates[ind + 1]

                if parser.parse(tomorrow) - parser.parse(today) != datetime.timedelta(1):
                    continue

                today_attenders = set([(el['firstName'], el['lastName'], el['email']) for el in dates_to_each[today]])
                tomorrow_attenders = set(
                    [(el['firstName'], el['lastName'], el['email']) for el in dates_to_each[tomorrow]])

                common_attenders = today_attenders.intersection(tomorrow_attenders)
                attenders_count = len(common_attenders)

                if attenders_count > total_attenders:
                    total_attenders = attenders_count
                    event_start_day = today
                    most_attenders = common_attenders

            countries.append({"attendeeCount": total_attenders,
                              "attendees": [x[2] for x in most_attenders],
                              "name": curr_country,
                              "startDate": None if total_attenders == 0 else event_start_day
                              })

        return {"countries": countries}
