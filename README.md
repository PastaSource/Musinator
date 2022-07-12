# Musinator
Generates random lyrics from a given TXT file, and a chord progression in a randomly chosen key.

Musinator's generation is almost completely random, there is however some code to stop things like single character word repetition.


## How it works
Create a TXT file called `input.txt` and fill it with whatever words you want Musinator to use to generate its lyrics. Run the code in a Terminal application (Powershell for example), and it will output a string of 10 words randomly chosen from you `input.txt`, a key accompanied with a mode, and a four chord progression.

## Example
`input.txt` is a plain text document containing David Bowie lyrics.

`lyric in key: F# Major
Chord progression: D#m C# F# Fdim
in been the a joined hangs takes seems strangest nightmare`

`lyric in key: C# Minor
Chord progression: F#m A B G#m
senseless to the closed rosy but of teatime round forgot`

## Todo
* Allow user to specify chord occurrence frequency, and length of generated progression
* Allow user to specify the length of generated lyrics
* Allow user to specify amount of generations to create
* Allow for saving of generations to a TXT file
* Implement less common modes
