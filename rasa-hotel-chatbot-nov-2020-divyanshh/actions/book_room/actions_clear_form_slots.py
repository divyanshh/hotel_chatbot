from rasa_sdk import Action

from rasa_sdk.events import SlotSet


class ClearFormSlots(Action):
    def name(self):
        return 'custom_action_clear_form_slots'

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("no_of_rooms", None),
                SlotSet("type_of_room", None),
                SlotSet("no_of_people", None)]
