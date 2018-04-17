import random
import time
import webbrowser

belchior_breaks = 3
break_count = 0
belchior_songs = ['SEsWJJAZ8pY', 'nPbTs9ZJcfU', 'fDHQZ6v3OAA',
                  '3lwSZxYTCFU', 'js9CIyvm9rE', 'TeIiPgCNwj8',
                  'IICn0oM52zE']

while(break_count < belchior_breaks):
    time.sleep(7200)
    for song in belchior_songs:
        song = random.choice(belchior_songs)
        url = 'https://www.youtube.com/watch?v=' + song
        webbrowser.open(url, new = 2)
    break_count += 1
