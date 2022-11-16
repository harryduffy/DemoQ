class Song:

    def __init__(self, uri, name):
        self.uri = uri
        self.name = name
        self._votes = 1

    def up_vote(self):
        self._votes += 1

    def down_vote(self):
        self._votes -= 1

    def get_votes(self):
        return str(self._votes)
