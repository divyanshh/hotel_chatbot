from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from math import ceil


class ClearFormSlots(Action):
    def name(self):
        return 'custom_action_set_rooms_for_n_people'

    def run(self, dispatcher, tracker, domain):
        try:
            no_of_people = tracker.get_slot('no_of_people')
            no_of_people = int(no_of_people.strip().split(' ')[0])
            no_of_rooms = ceil(no_of_people / 2)  # assuming most hotels allow only 2 people per room
            return [SlotSet("no_of_rooms", no_of_rooms)]
        except:
            dispatcher.utter_message("Couldn't understand the request. Please rephrase your request")
