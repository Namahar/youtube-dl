'''
repo found at https://github.com/ytdl-org/youtube-dl

uses repo to download music from youtube
'''

import os
import sys

def get_file(original_files):
   '''
   original_files: list of directory before audio file was downloaded
   returns name of audio file
   '''

   new_files = os.listdir()

   for f in new_files:
      if f not in original_files:
         return f

   return None


def main():

   # starting directiory is /Documents
   # need to go to youtube-dl
   os.chdir('youtube-dl')
   print(os.getcwd())

   # save file list for comparison
   files = os.listdir()

   # download youtube video
   url = sys.argv[1]
   command = 'python3 -m youtube_dl --default-search "auto" -x --audio-format "mp3" --audio-quality 0 '
   os.system(command + url)

   # convert audio file to mp3
   audio_file = get_file(files)

   if audio_file == None:
      print('no audio file found')
      return

   # check if already mp3 file

   if audio_file[-1] != '3':
      dot = audio_file.index('.') + 1
      output_file = audio_file[:dot] + 'mp3'

      convert = 'ffmpeg -i "' + audio_file + '" -ab 320 "' + output_file + '"'
      os.system(convert)

      # delete old file and move new file
      os.system('rm "' + audio_file + '"')
      os.system('mv "' + output_file + '" ../')

   else:
      os.system('mv "' + audio_file + '" ../')

   return

if __name__ == '__main__':
   if len(sys.argv) != 2:
      print('please enter a youtube url')
      exit()

   main()