import speech_recognition as sr


class SpeechRecognition:
    recognized_text = ''

    def get_microphone_to_text(self) -> str:
        print("Приём голоса...")
        # Создаем объект recognizer
        recognizer = sr.Recognizer()

        # Используем микрофон как источник звука
        with sr.Microphone() as source:

            # Захватываем звук из микрофона
            audio = recognizer.listen(source)

            try:
                self.recognized_text += recognizer.recognize_google(audio, language='ru-RU')
            except sr.UnknownValueError:
                self.recognized_text += "Кажется, не удалось распознать речь"
            except sr.RequestError as e:
                self.recognized_text += e

        print("Приём окончен.")
        print(self.recognized_text)
        return self.recognized_text
