import random
#Import Lyrics
from pathlib import Path
key = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
def keyselector():
    #Pick a key
    song_key_int = random.randrange(0, len(key))
    song_key = key[song_key_int]
    key_index = key.index(song_key)
    keydict = {"key": song_key, "key_index": key_index}
    return keydict

def modeselector():
    mode = ["Major", "Minor"]
    #Pick a mode
    song_mode_int = random.randrange(0, len(mode))
    song_mode = mode[song_mode_int]
    return song_mode

def txtload(inputtxt):
    lyrics = Path(inputtxt).read_text()
    lyriclist = lyrics.split(" ")
    #Initialize list for cleaned lyrics
    cleanedlyriclist = []
    #Remove any none alphabetical characters
    for clean in lyriclist:
        if clean.isalpha():
            cleanedlyriclist.append(clean)
    return cleanedlyriclist

def lyricgenerator(inputtxt):
    cleanedlyriclist = txtload(inputtxt)
    newlyric = []
    #counts frequency of certain lengths of words generated
    fourorless = 0
    fiveormore = 0
    #Lyric generator
    for count, lyric in enumerate(range(0,10)):
        #Picks a random int
        randomint = random.randrange(0, len(cleanedlyriclist))
        #Uses random int to select word at that position in cleaned lyric list
        new = cleanedlyriclist.pop(randomint)
        #Only adds word to the lyric list if not already in it
        if new in newlyric:
            #Generates a new int in an attempt to add a word not already in the list
            while new in newlyric:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
            #Avoids multiple single character words in succession
            while newlyric[count-1] == 1:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
        #Reduces frequency of low length words
        elif len(new) >= 5:
            fiveormore += 1
        elif len(new) <= 4:
            fourorless += 1
            if fourorless >= 5:
                while len(new) <= 4:
                    randomint = random.randrange(0, len(cleanedlyriclist))
                    new = cleanedlyriclist.pop(randomint)
        newlyric.append(new)
    return newlyric

def chordgenerator():
    keydict = keyselector()
    song_key = keydict.get("key")
    key_index = keydict.get("key_index")
    song_mode = modeselector()
    progression = []
    progressiondict = {}
    #Chord progression generator
    for randomchords in range(0,4):
        progression_num = []
        #Defines what makes up a major key and selects it
        if song_mode == "Major":
            #Chord numberings are their positions from the root key minus 1
            chords = [0, 2, 4, 5, 7, 9, 11]
            chord_modes = ["Major", "Minor", "Minor", "Major", "Major", "Minor", "Dim"]
        #Defines what makes up a minor key and selects it
        elif song_mode == "Minor":
            chords = [0, 2, 3, 5, 7, 8, 10]
            chord_modes = ["Minor", "Dim", "Major", "Minor", "Minor", "Major", "Major"]
        #Picks a random number from the "chords" list
        chord = chords[random.randrange(0, len(chords))]
        #Tracks chord frequency in progressiondict dictionary and prevents chords repeating too often
        if chord not in progressiondict.keys():
            progressiondict[chord] = 1
        elif chord in progressiondict.keys():
            if progressiondict[chord] >= 2:
                while chord in progressiondict.keys():
                    chord = chords[random.randrange(0, len(chords))]
            progressiondict[chord] = progressiondict.get(chord) + 1
        #Appends chord onto progression_num list
        progression_num.append(chord)
        #Uses the "chords" list as an index for the "chord_modes" list and checks whether the given chord
        #should be a major, minor, or diminished chord, and appends it appropriately.
        for chosen in progression_num:
            if chord_modes[chords.index(chosen)] == "Major":
                progression.append(key[chosen - (12 - key_index)])
            elif chord_modes[chords.index(chosen)] == "Minor":
                progression.append("{}m".format(key[chosen - (12 - key_index)]))
            elif chord_modes[chords.index(chosen)] == "Dim":
                progression.append("{}dim".format(key[chosen - (12 - key_index)]))
    keymodeprogression = {"key": song_key, "mode": song_mode, "prog": progression}
    return keymodeprogression

def formatting(inputtxt):
    lyrics = lyricgenerator(inputtxt)
    items = chordgenerator()
    song_key = items.get("key")
    song_mode = items.get("mode")
    progression = items.get("prog")
    #Converts the "progression" and "newlyric" lists into strings
    prog_format = " ".join(progression)
    preformat = " ".join(lyrics)
    #Formats the generated lyric, with the key and chord progression, and adds it to the "bunch" str.
    formatted = "lyric in key: {} {}\nChord progression: {}\n{}\n".format(song_key, song_mode, prog_format, preformat)
    print(formatted)



formatting("input.txt")