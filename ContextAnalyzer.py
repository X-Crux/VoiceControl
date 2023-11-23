
class ContextAnalyzer:
    data = dict()

    def __init__(self, data):
        self.data = data

    def analyze_context(self) -> dict:
        context = {
            'verb': 'create',
            'noun': 'file'
        }

        if 'создай' in self.data['verbs'] or 'создать' in self.data['verbs']:
            context['verb'] = 'create'
        elif 'удали' in self.data['verbs'] or 'удалить' in self.data['verbs']:
            context['verb'] = 'remove'
        elif 'закрой' in self.data['verbs'] or 'закрыть' in self.data['verbs']:
            context['verb'] = 'exit'

        if 'файл' in self.data['nouns'] \
                or 'файлов' in self.data['nouns'] \
                or 'файлы' in self.data['nouns'] \
                or 'файла' in self.data['nouns'] \
                or 'документ' in self.data['nouns'] \
                or 'документов' in self.data['nouns'] \
                or 'документы' in self.data['nouns'] \
                or 'документа' in self.data['nouns']:
            context['noun'] = 'file'
        elif 'программу' in self.data['nouns']:
            context['noun'] = 'app'
        elif 'выход' in self.data['nouns']:
            context['verb'] = 'exit'
            context['noun'] = 'app'

        return context
