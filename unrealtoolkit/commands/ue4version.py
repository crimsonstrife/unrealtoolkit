import os
import glob

import unrealtoolkit.ubt


from unrealtoolkit.commands.base import BaseCommand
class Command(BaseCommand):
	def get_description(self):
		return "Prints the Unreal Engine 4 version the project uses"

	def run(self, args):
		uproject = unrealtoolkit.ubt.get_uproject()
		if uproject == None:
			print("No uproject file found")
			exit()

		print(uproject.info['EngineAssociation'])
		