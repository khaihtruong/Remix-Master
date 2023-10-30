"""

   CS5001 - Fall 2023


   Khai Truong


   remix_master.py


   A remix master program that allow user to remix the songs in a playlist

"""
# import the playlist
from music import *

def substitute(song, old_word, new_word):
    '''
    FUNCTIONS - substitute
    substitute a word in the lyrics with a new one
    return True if the word was in the song and the original
    list will be mutate
    return False if the word wasn't in the song

    PARAMETER
    song - list, contain the lyrics of the song
    old_word - word that want to be replaced
    new_word - word that want to be replaced with

    RETURN
    Boolean value indicate whether the word was in the song
    the original list will be mutated
    '''
    # word counter to keep track if the word is in the song
    word_count = 0

    # check word by word to see if the word is in the song
    for sentence in song:

        # split the string into list to check word by word
        sentence = sentence.split()
        for word in sentence:

            # if the word is in the string then increase word count by 1 
            if old_word == word:
                word_count += 1

    # if word count is larger than zero meaning the word is in the song
    if word_count > 0:

        # remove punctuation and replace the word sentence by sentence
        for sentence in range(len(song)):

            # remove all the punctuation
            song[sentence] = song[sentence].replace(',', '')
            song[sentence] = song[sentence].replace('.', '')
            song[sentence] = song[sentence].replace('?', '')
            song[sentence] = song[sentence].replace('!', '')
            song[sentence] = song[sentence].replace(':', '')

            # split the sentence to a list to replace the word
            song[sentence] = song[sentence].split()
            
            # replace the word with a new one
            for word in range(len(song[sentence])):
                if song[sentence][word] == old_word:
                    song[sentence][word] = new_word

            # turn the sentence back into a string       
            song[sentence] = ' '.join(song[sentence])

        # return True because the word was in the song
        return True

    # if the word not in the song return False
    else:
        print(f'We can\'t find the word {old_word} in the song\n')
        return False

def reverse_it(song):
    '''
    FUNCTIONS - reverse_it
    given a song reverses the song
    such that the words (not letters) are in the reverse order

    PARAMETER
    song - list containing multiple strings

    RETURN
    the list of the original song altered in the reverse order
    '''
    # reverse the list by reverse multiple string
    for i in range(len(song)):

        # remove punctuation 
        song[i] = song[i].replace(',', '')
        song[i] = song[i].replace('.', '')
        song[i] = song[i].replace('?', '')
        song[i] = song[i].replace('!', '')
        song[i] = song[i].replace(':', '')

        # split the string into a list then reverse the order
        song[i] = song[i].split(' ')
        song[i].reverse()

        # turn the list into a string again 
        song[i] = ' '.join(song[i])
    return song

def load_song(selection):
    '''
    FUNCTINONS - load_song
    load a new song based on user selection
    which include the title and the lyrics

    PARAMETERS
    selection - integers indicate a song and corresponding lyrics

    RETURN
    return a new song which is a list contain the title and lyrics
    if the integers is out of range an empty list will be return 
    '''
    # user_centered operation so we need to -1 to adjust the position
    position_adjustment = 1
    song_choice = selection - position_adjustment

    # set up a list for the chosen song
    chosen_song = [[]]

    # if the input is within the range of the song then we will return it
    if 0 < selection <= len(PLAYLIST):
        song_name = PLAYLIST[song_choice]
        song_lyrics = SONGS[song_choice]
        
        chosen_song.append(song_name)
        
        chosen_song[0].extend(song_lyrics)
        return chosen_song

    # if the input is outside of the range, an empty list will be return
    else:
        print('Invalid input')
        empty_list = []
        return empty_list        

def remix_master():
    # import random module
    import random

    # load the first song as the default song
    current_song = load_song(1)
    original_song = current_song[1]
    original_lyrics = current_song[0]

    # make a copy of the lyrics for remix
    current_song_title = original_song
    current_song_lyrics = original_lyrics.copy()
    
    print('Welcome to ReMix-Master. You can remix the greatest hits!')
    print('Here\'s your remix:')

    # print each sentence of the lyrics on a separate line
    for i in range(len(current_song_lyrics)):
        print(f'{current_song_lyrics[i]}')
    print()

    # the loop will repeat until the user select Q for Quit
    again = ''
    while again.upper() != 'Q':

        # load the remix master menu
        print('Remix-Master: \n L: Load a different song \n \
T: Title of current song \n S: Substitue a word \n P: Playback \
your song \n R: Reverse it! \n X: Reset to original song \n Q: Quit?\n')

        # require user to input correctly according to menu
        while True:
            
            # user input
            choice = input("What's your choice? ")
            print(f'Your choice: {choice}\n')

            # if the user input match one of the following
            # option the program will move on
            valid_choice = ['L', 'T', 'S', 'P', 'R', 'X', 'Q']
            if choice.upper() in valid_choice:
                break

            # if it doesn't match error will print out
            else:
                print('Invalid input\n')

        # if user select L, it will load a new song  
        if choice.upper() == 'L':
            
            # assign number with the song for user to select
            number = 1
            for i in range(len(PLAYLIST)):
                print(f'{number}. {PLAYLIST[i]}')
                number += 1
                
            while True:

                # user input
                selection = int(input(f'Choose the number for song \
you want to load:\n'))
                
                # the program will only load the song if it's in the playlist
                if 0 < selection <= len(PLAYLIST):
                    current_song = load_song(selection)
                    original_song = current_song[1]
                    original_lyrics = current_song[0]

                    current_song_title = original_song
                    current_song_lyrics = original_lyrics.copy()
                    break

                # if user select a song outside the playlist
                # the error will pop up
                else:
                    print('Invalid input')

        # if user select T then it will show the title of the current song
        elif choice.upper() == 'T':
            print(f'Title of current song is {current_song_title}\n')

        # if user select S then it will substitute a word in the song
        elif choice.upper() == 'S':

            # user input
            old_word = input('What word do you want to replace \
in the existing song? ')
            new_word = input('What new word do you want to use for the song? ')

            # substitute the old word by a new one
            substitute(current_song_lyrics, old_word, new_word)

        # if user select P it will replay the lyrics of the song
        elif choice.upper() == 'P':

            # print each sentence of the lyrics on a new line
            for i in range(len(current_song_lyrics)):
                print(f'{current_song_lyrics[i]}')
            print()

        # if user select R it will reverse the song
        # such that the words (not letters) are in the reverse order
        elif choice.upper() == 'R':
            reverse_it(current_song_lyrics)

        # if user select X it will revert back to original version of the song    
        elif choice.upper() == 'X':
            current_song_lyrics = original_lyrics.copy()

        # if user select Q the program will stop running    
        elif choice.upper() == 'Q':
            again = 'Q'
                
def main():
    remix_master()
    
if __name__ == "__main__":
    main()
