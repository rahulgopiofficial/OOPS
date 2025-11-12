class musicplayer:
    def __init__(self, playlist, current_song) -> None:
        self.playlist = playlist
        self.current_song = current_song

    def add(self, song_name):
        self.playlist.append(song_name)
        print(f"The updated playlist is {self.playlist}")

    def remove(self, song_name):
        if song_name not in self.playlist:
            print("Song not present in the list")
        else:
            self.playlist.remove(song_name)
            print(f"The updated playlist is {self.playlist}")

    def next(self):
        print(f"The current song is {self.current_song}")

        if self.current_song not in self.playlist:
            self.current_song = self.playlist[0]
            print(f"Current song changing to {self.current_song}")
        else:
            index = self.playlist.index(self.current_song)

            if index == (len(self.playlist)-1):
                self.current_song = self.playlist[0]
                print(f"Current song changing to {self.current_song}")
            else:
                index += 1
                self.current_song = self.playlist[index]
                print(f"Current song changing to {self.current_song}")

s1 = musicplayer(['teri dewani', 'tere naina', 'jalakkari', 'husn'], None)
s1.add('minnal vala')
s1.remove('tei dewani')
s1.next()
s1.next()