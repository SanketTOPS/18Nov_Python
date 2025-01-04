from pytubefix import YouTube

url="https://www.youtube.com/watch?v=vX7JUEvI92A"

YouTube(url).streams.first().download()