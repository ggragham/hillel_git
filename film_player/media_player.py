import requests


class Player:
	def __init__(self, name):
		self.name = name
		self.duration = 0
		self.currentPosition = 0
		self.isPlaying = False
		self.videoLink = ""

	def Play(self, videoLink, duration):
		response = requests.get(videoLink)

		if response.status_code == 200:
			self.videoLink = videoLink
			self.duration = duration
			self.isPlaying = True
			print(f"Playing {self.name} at {self.videoLink} for {self.duration} minutes")
			return True
		else:
			print(f"Video at {videoLink} not found")
			return False

	def Pause(self):
		if self.isPlaying:
			self.isPlaying = False
			print(f"Paused {self.name} at {self.currentPosition} minutes")
		else:
			print(f"Video is not playing")

	def Stop(self):
		if self.isPlaying:
			self.isPlaying = False
			self.currentPosition = 0
			print(f"Stopped {self.name}")
		else:
			print(f"Video is not playing")

	def Forward(self, minutes):
		if self.isPlaying:
			if self.currentPosition + minutes <= self.duration:
				self.currentPosition += minutes
				print(f"Forwarded to {self.currentPosition} minutes")
			else:
				print(f"Can't forward beyond the total video duration")
		else:
			print(f"Video is not playing")

	def Rewind(self, minutes):
		if self.isPlaying:
			self.currentPosition = max(0, self.currentPosition - minutes)
			print(f"Rewinded to {self.currentPosition} minutes")
		else:
			print(f"Video is not playing")
