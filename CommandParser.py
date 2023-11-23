import spacy
from Command import Command
from ContextAnalyzer import ContextAnalyzer

# Загрузка модели языка для обработки текста
nlp = spacy.load("ru_core_news_sm")


class CommandParser:
    data = dict()
    command_executor = None

    def parse_command(self, command_text) -> Command:
        doc = nlp(command_text)
        # Ищем глаголы, прилагательные, существительные и числа в команде
        self.data['verbs'] = [token.text.lower() for token in doc if token.pos_ == "VERB"]
        self.data['adjs'] = [token.text.lower() for token in doc if token.pos_ == "ADJ"]
        self.data['nouns'] = [token.text.lower() for token in doc if token.pos_ == "NOUN"]
        self.data['nums'] = [token.text.lower() for token in doc if token.pos_ == "NUM"]
        self.data['dets'] = [token.text.lower() for token in doc if token.pos_ == "DET"]

        if 'ноль' in self.data['nouns']:
            self.data['nouns'].remove('ноль')
            self.data['nums'].append('ноль')

        if 'закрой' in self.data['nouns']:
            self.data['nouns'].remove('закрой')
            self.data['verbs'].append('закрой')

        # print('data:', self.data)

        context_analyzer = ContextAnalyzer(self.data)
        context = context_analyzer.analyze_context()

        command = Command(self.data)
        command.set_context(context)

        return command
