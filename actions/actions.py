from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionConfirmReservation(Action):
    def name(self):
        return "action_confirm_reservation"

    def run(self, dispatcher, tracker, domain):
        date = tracker.get_slot('date')
        number_of_people = tracker.get_slot('number_of_people')
        name = tracker.get_slot('name')
        phone_number = tracker.get_slot('phone_number')

        if date and number_of_people and name and phone_number:
            message = f"Votre réservation pour {number_of_people} personnes le {date} au nom de {name} a été confirmée."
        else:
            missing_info = []
            if not date:
                missing_info.append("la date")
            if not number_of_people:
                missing_info.append("le nombre de personnes")
            if not name:
                missing_info.append("le nom")
            if not phone_number:
                missing_info.append("le numéro de téléphone")

            message = f"Je n'ai pas toutes les informations nécessaires. Pouvez-vous préciser : {', '.join(missing_info)} ?"
        
        dispatcher.utter_message(text=message)
        return []

class ActionCancelReservation(Action):
    def name(self):
        return "action_cancel_reservation"

    def run(self, dispatcher, tracker, domain):
        cancel_code = tracker.get_slot('cancel_code')

        if cancel_code:
            message = f"Votre réservation avec le code {cancel_code} a été annulée."
        else:
            message = "Je n'ai pas trouvé de réservation avec ce code pour annuler."
        
        dispatcher.utter_message(text=message)
        return []

class ActionReservationInfo(Action):
    def name(self):
        return "action_reservation_info"

    def run(self, dispatcher, tracker, domain):
        info_code = tracker.get_slot('info_code')

        if info_code:
            message = f"Voici les informations sur votre réservation avec le code {info_code}."
        else:
            message = "Je n'ai pas trouvé de réservation avec ce code pour obtenir les informations."

        dispatcher.utter_message(text=message)
        return []