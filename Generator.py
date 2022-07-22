import random
from pathlib import Path
#Key and mode selector functions
def keyselector():
    song_key_int = random.randrange(0, len(key))
    song_key = key[song_key_int]
    key_index = key.index(song_key)
    keydict = {"key": song_key, "key_index": key_index}
    return keydict
def modeselector(complexity):
    if complexity == 1:
        mode = ["Major", "Minor", "Phrygian", "Locrian", "Dorian", "Lydian", "Mixolydian"]
    else:
        mode = ["Major", "Minor"]
    song_mode_int = random.randrange(0, len(mode))
    song_mode = mode[song_mode_int]
    return song_mode
#Import txt file
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
#Randomly picks words from imported TXT file
def lyricgenerator(inputtxt, upperrange):
    cleanedlyriclist = txtload(inputtxt)
    newlyric = []
    #Counts frequency of certain lengths of words generated
    fourorless = 0
    fiveormore = 0
    #Lyric generator
    for lyric in range(0,upperrange):
        #Picks a random int
        randomint = random.randrange(0, len(cleanedlyriclist))
        #Uses random int to select word at that position in cleaned lyric list
        new = cleanedlyriclist.pop(randomint)
        #Checks if chosen word is already in newlyric list
        if new in newlyric:
            #Generates a new int in an attempt to add a word not already in the list
            while new in newlyric:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
            #Avoids multiple single character words in succession
            while len(newlyric[len(newlyric) -1]) <= 1 and len(new) <= 1:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
        #Reduces frequency of low length words
        if fourorless < (upperrange // 2):
            if len(new) <= 4:
                fourorless += 1
        if fiveormore < (upperrange // 2):
            if len(new) >= 5:
                fiveormore += 1
        if fourorless >= (upperrange // 2) and len(new) <= 4:
            while len(new) <= 4:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
            fiveormore += 1
        if fiveormore >= (upperrange // 2) and len(new) >= 5:
            while len(new) >= 5:
                randomint = random.randrange(0, len(cleanedlyriclist))
                new = cleanedlyriclist.pop(randomint)
            fourorless += 1
        newlyric.append(new)
    return newlyric
#Generates a chord progression
def chordgenerator(upperrange, frequency, complexity):
    keydict = keyselector()
    song_key = keydict.get("key")
    key_index = keydict.get("key_index")
    song_mode = modeselector(complexity)
    progression = []
    progressiondict = {}
    progressionint = 1
    #Chord progression generator
    for randomchords in range(0,upperrange):
        progression_num = []
        #Chord numberings are their positions from the root key minus 1
        #Defines what makes up a Major/Ionian key and selects it
        if song_mode == "Major":
            chords = [0, 2, 4, 5, 7, 9, 11]
            chord_modes = ["Major", "Minor", "Minor", "Major", "Major", "Minor", "Dim"]
        #Defines what makes up a Dorian key and selects it
        if song_mode == "Dorian":
            chords = [0, 2, 3, 5, 7, 9, 10]
            chord_modes = ["Minor", "Minor", "Major", "Major", "Minor", "Dim", "Major"]
        #Defines what makes up a Phyrgian key and selects it
        if song_mode == "Phyrgian":
            chords = [0, 1, 3, 5, 7, 8, 10]
            chord_modes = ["Minor", "Major", "Major", "Minor", "Dim", "Major", "Minor"]
        #Defines what makes up a Lydian key and selects it
        if song_mode == "Lydian":
            chords = [0, 2, 4, 6, 7, 9, 11]
            chord_modes = ["Major", "Major", "Minor", "Dim", "Major", "Minor", "Minor"]
        #Defines what makes up a Mixolydian key and selects it
        if song_mode == "Mixolydian":
            chords = [0, 2, 4, 5, 7, 9, 10]
            chord_modes = ["Major", "Minor", "Dim", "Major", "Minor", "Minor", "Major"]
        #Defines what makes up a Minor/Aeolian key and selects it
        if song_mode == "Minor":
            chords = [0, 2, 3, 5, 7, 8, 10]
            chord_modes = ["Minor", "Dim", "Major", "Minor", "Minor", "Major", "Major"]
        #Defines what makes up a Locrian key and selects it
        if song_mode == "Locrian":
            chords = [0, 1, 3, 5, 6, 8, 10]
            chord_modes = ["Dim", "Major", "Minor", "Minor", "Major", "Major", "Minor"]

        #Picks a random number from the "chords" list
        chord = chords[random.randrange(0, len(chords))]
        #Tracks chord frequency in progressiondict dictionary and prevents chords repeating too often
        if chord not in progressiondict.keys():
            progressiondict[chord] = 1
            progression_num.append(chord)
        elif chord in progressiondict.keys():
            attempt = 0
            progressionint = progressiondict[chord]
            if progressiondict[chord] <= (frequency - 1):
                progressionint += 1
                progressiondict[chord] = progressionint
                progression_num.append(chord)
            elif progressiondict[chord] >= frequency:
                while chord in progressiondict.keys() and attempt <= 10:
                    chord = chords[random.randrange(0, len(chords))]
                    attempt += 1
                if attempt <= 10:
                    progressionint += 1
                    progressiondict[chord] = progressionint
                    progression_num.append(chord)
                else:
                    pass
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
#Key function that sends commands to other functions and returns a formatted string.
def formatting(inputtxt, lyricupperrange, chordupperrange, frequency, complexity):
    lyrics = lyricgenerator(inputtxt, lyricupperrange)
    items = chordgenerator(chordupperrange, frequency, complexity)
    song_key = items.get("key")
    song_mode = items.get("mode")
    progression = items.get("prog")
    #Converts the "progression" and "newlyric" lists into strings
    prog_format = " ".join(progression)
    preformat = " ".join(lyrics)
    #Formats the generated lyric, with the key and chord progression, and adds it to the "bunch" str.
    formatted = "lyric in key: {} {}\nChord progression: {}\n{}\n".format(song_key, song_mode, prog_format, preformat)
    return formatted
#Performs checks on user input
def numericcheck(amount):
    userinput = amount
    if not str(userinput).isnumeric():
        print("ERROR! Input must be numeric.")
        return False
    elif int(userinput) <= 0 or int(userinput) >= 100:
        print("ERROR! Input must be between 0 and 99.")
        return False
    return userinput
#Defines keys
key = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
#Stores generations in str variable.
generations = ""
#Allow the user to decide how many generations are to be made.
iterations = input("Please enter the amount of iterations to generate (1-99): ")
while numericcheck(iterations) is False:
    iterations = input("Please enter the amount of iterations to generate (1-99): ")
#Allow the user to choose how many words to generate in a lyric.
lyricupperrange = input("Please choose the amount of words per lyric (1-99): ")
while numericcheck(lyricupperrange) is False:
    lyricupperrange = input("Please choose the amount of words per lyric (1-99): ")
#Allow the user to choose how many chords are generated in a progression.
chordupperrange = input("Please choose the amount of chords per progression (1-99): ")
while numericcheck(chordupperrange) is False:
    chordupperrange = input("Please choose the amount of chords per progression (1-99): ")
#Allow the user to generate progressions with more uncommon modes.
complexity = input("Please enter 1 for uncommon modes (e.g. Locrian, Dorian, etc.): ")
while numericcheck(complexity) is False:
    complexity = input("Please enter 1 for uncommon modes (e.g. Locrian, Dorian, etc.): ")
#Allow the user to choose the frequency of how often a chord can appear in a progression.
frequency = input("Please choose how many times a chord can appear in a progression (1-99): ")
while numericcheck(frequency) is False:
    frequency = input("Please choose how many times a chord can appear in a progression (1-99): ")
#For loop using user input to determine amount of iterations to generate.
for iteration in range(int(iterations)):
    generations += formatting("input.txt", int(lyricupperrange), int(chordupperrange), int(frequency), int(complexity))
print(generations)