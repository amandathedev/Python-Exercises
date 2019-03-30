playlist = {
    'title': 'patagonia bus', 
    'author': 'colt steele', 
    'songs': [
        {'title': 'song1', 'artist': ['band'], 'duration': 2.5},
        {'title': 'song2', 'artist': ['band2', 'dj'], 'duration': 5.25},
        {'title': 'song3', 'artist': ['band3'], 'duration': 2.0}
        ]
    }

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)