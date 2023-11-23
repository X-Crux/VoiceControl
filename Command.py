
class Command:
    data = dict()
    context = dict()
    analyze = dict()
    # action = {
    #     'verb': 'create',  # context
    #     'noun': 'file',    # context
    #     'adj': 'txt',      # analyze
    #     'num': 1           # analyze
    # }

    def __init__(self, data):
        self.data = data

    def get_data(self) -> dict:
        return self.data

    def set_context(self, context: dict):
        for k, v in context.items():
            self.context[k] = v

    def set_analyze(self, analyze: dict):
        for k, v in analyze.items():
            self.analyze[k] = v

    def get_action(self) -> str:
        return ' '.join([str(value) for value in self.context.values()] + [str(value) for value in self.analyze.values()])
