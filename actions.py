from rasa_core.events import Restarted
from rasa_core.events import StoryExported
from rasa_core.actions import Action

class ActionByeBye (Action):
	def name(self):
		return 'action_bye'
	def run (self, dispatcher, tracker, domain):
		return[StoryExported("data.md"),Restarted()]