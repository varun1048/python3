from Masstamilan import Masstamilan

inner = input("Album name :")
# inner = "sarkar"
songs  = Masstamilan(inner)
songs.albumInfo()
songs.displaySongs()
# songs.Download()
songs.playOnline()

