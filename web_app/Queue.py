from Song import Song

class Queue:

    def __init__(self, capacity):
        self._queue = []
        self.size = 0
        self._capacity = capacity

    def organise(self):

        self._queue = sorted(self._queue, key=lambda song: song.get_votes(), reverse=True)

        return self._queue

    def enqueue(self, new_song):

        if not new_song:
            return

        if self.size == self._capacity:
            print("\nCapacity Reached.\n")
            return

        self.size += 1
        self._queue.append(new_song)

        return self._queue

    def dequeue(self):

        self._queue.pop(0)
        self.size -= 1

        return self._queue

    def clear_queue(self):
        
        self._queue = []

    def is_empty(self):

        if self.size == 0:
            return True

        return False

    def get_queue(self):
        return self._queue

    def up_vote_song(self, song):

        song.up_vote()
        
        self.organise()

        return song._votes

    def down_vote_song(self, song):

        song.down_vote()

        self.organise()

        return song._votes