from SpeechRecognition import SpeechRecognition
from CommandExecutor import CommandExecutor
from CommandParser import CommandParser


class VoiceCommand:
    speech_recognition = None
    command_text = ''

    def __init__(self):
        self.speech_recognition = SpeechRecognition()

    def get_audio_command(self):
        self.command_text = self.speech_recognition.get_microphone_to_text()

    def execute(self):
        command_parser = CommandParser()
        command = command_parser.parse_command(self.command_text)

        command_executor = CommandExecutor()
        command_executor.execute_command(command)
