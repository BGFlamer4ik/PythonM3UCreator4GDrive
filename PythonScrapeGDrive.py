from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

folder_id = ''

file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

audio_files = [file for file in file_list if file['mimeType'].startswith('audio/')]

playlist_name = 'gdrive_playlist.m3u'
with open(playlist_name, 'w', encoding='utf-8') as playlist_file:
    playlist_file.write('#EXTM3U\n\n')
    for audio_file in audio_files:
        playlist_file.write(f'#EXTINF:-1,{audio_file["title"]}\n')
        playlist_file.write(audio_file['webContentLink'] + '\n\n')

print(f'Playlist "{playlist_name}" successfully created!')
