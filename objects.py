class New:
    def __init__(self, data):
        self.json = data
        self.generated = None
        self.scheme = None
        self.src = None
        self.name = None

    @property
    def new(self):
        try:
            self.generated = self.json['generated']
            self.scheme = self.json['scheme']
            self.src = self.json['src']
            self.name = self.json['name']
        except(KeyError, TypeError): pass
        return self