from rasa_sdk import Action
from datetime import datetime, timedelta


class GetRoomCleaningAfterHours(Action):
    def name(self):
        return 'custom_action_get_room_cleaning_after_hours'

    def run(self, dispatcher, tracker, domain):
        try:
            after_hours = tracker.get_slot('room_cleaning_hours')
            after_hours = int(after_hours.strip().split(' ')[0])
            curr_date = datetime.now()
            room_cleaning_time = curr_date + timedelta(hours=after_hours)
            today_or_tomorrow = ''
            if format(curr_date, '%d') == format(room_cleaning_time, '%d'):
                today_or_tomorrow = "today"
            else:
                today_or_tomorrow = "tomorrow"
            dispatcher.utter_message("I have scheduled a cleaning for " + format(room_cleaning_time, '%I:%M %p') + " "
                                     + today_or_tomorrow)
        except:
            dispatcher.utter_message("Couldn't understand the request. Please rephrase your request")
        finally:
            return []
