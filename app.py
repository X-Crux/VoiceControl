from VoiceCommand import VoiceCommand


def voice_command():
    while True:
        input('\n>>> Нажмите Enter, чтобы принять голосовую команду.')
        vc = VoiceCommand()
        vc.get_audio_command()
        vc.execute()


if __name__ == '__main__':
    voice_command()

