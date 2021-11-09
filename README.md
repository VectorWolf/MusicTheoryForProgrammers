# MusicTheoryForProgrammers
#### AKA Music theory for people who prefer numbers to letters
#### AKA Music theory for people who are disappointed with the inconsistency of current notation
#### AKA Music theory exclusively for me myself and no other human being

# What is a note?
To be super general, a note itself is nothing but a sound-wave with a distinct frequency. 1337Hz for example, that's a note. But what usually is meant when most musical persons talk about notes is a note in the western 12-tone-equal-temperament-system. Virtually all pop music, from classic till today is written in it (or slightest variations of it). This system builds on the repetition of 12 reoccurring notes.

How this works? It's relatively easy, you start at a frequency, lets say 440Hz, that's our zero'th note and by doubling it to 880Hz you get the 12th note. The notes in-between are a bit more difficult to calculate, since we can't just interpolate linearly but have to "follow the curvature" of the 2^x function. This means to get the next note, you have to multiply with the 12th root of two which is roughly 1.05946... . Here's an example starting from 440Hz with rounding applied.

|Step     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |
|---------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|Factor   | 1.0 |1.059|1.122|1.189|1.260|1.335|1.414|1.498|1.584|1.682|1.782|1.888| 2.0 |
|Frequency| 440 |466.2|493.9|523.3|554.4|587.3|622.3|659.3|698.5|740.0|784.0|830.6| 880 |

The cool thing is you can choose any step count and any factor to get another n-tone equal temperament system. 24th root of three sounds pretty cool for example. But you can also choose to interpolate differently or instead of using a formula, choosing each tone individually. There is no real right and wrong, use what sounds well and have fun!

How do we know at what frequency we should start? Well actually there is no reason to favor any frequency over any other. Most commonly used is 440Hz with steps above and below, but the selection is arbitrary. The chosen pitch is then called "concert pitch".

A small note, if you're "sub-stepping" between the notes there is a unit called cents. A note +100 cents gets you the next note, a note +50 gets you a note right in-between which is outside the system (has no own name).

How does this twelve tone system overall sound? Well, the doubling of the frequency (commonly called octave) sounds like just the same note but higher (or lower if halved) and is the main building block of the notation system.

The notation system, which is used to most commonly write and talk about notes is, in my opinion, one big hysterical raisin and pretty bad to understand, like most natural languages honestly. It's C D E F G A B.

But wait, there are five notes missing? Yes, this is because all notes are expressed relative to the C-Major scale (we get to scales later), and the missing notes in-between are called sharp(#) or flat(b) depending on if you're going up or down in pitch. Also you have to memorize that there are no steps between B and C and between E and F. 

What makes this even more awful is that you can accumulate as many # or b signs behind a note which makes reading more difficult (C## = D). I personally find this favoring of C-Major a bit silly and off-putting especially for beginners so I vow for the so called "Integer Scale" which is more commonly used by mathematicians and looks in this case just like an ordinary Base 12 Number going from 0 to 9 to B to 0 again (Which is super easy if you're used to hex).

|Step     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Common   |B# / C |C# / Db|  D  |D# / Eb|E / Fb |E# / F |F# / Gb|  G  |G# / Ab|  A  |A# / Bb|  B  |B# / C |
|Integer  |    0  |    1  |  2  |    3  |    4  |    5  |    6  |  7  |    8  |  9  |    A  |  B  |    0  |

This notation will get us the relative pitch pretty easily, but we need another number to indicate at what tonal "height" the played note is. The "normal" notation goes like A¹=55Hz, A²=110Hz, A³=220Hz for all notes. Again going with base 12 it's really easy, just add a number to the left to get a two digit number. 49 = 440Hz, 39 = 220Hz, 29 = 110Hz, 19 = 55Hz, 09 = 27.5Hz, 00 = 16.35Hz . Now we also know, a one digit note is always a relative note which may be played at any desired tonal height, a two digit note usually means an absolute note which is at only one distinct pitch.

# What is a scale?

With scales it's the same as with notes. The general description is being just a an ordered set of notes. To narrow it down scales usually.. :
1. Sound somewhat interesting or musically useful
2. Go from low to high (and sometimes to low again)
3. Span only relative notes and may be played at any starting note
4. End an octave higher than they started
5. Consist of mostly 2-note, 1-note and more seldom 3-note steps
6. Usually have 7 steps (not including the octave), sometimes 5 (called pentatonic), rarely else

Some useful notations of scales include writing down the step size between each note, or the step size from the base note. As an example let's look at the most common used scales, the major scale (which most people describe as "happy")

|Major|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|2|1|2|2|2|1|
|Relative|2|4|5|7|9|B|10|

and the (natural) minor scale (which most people describe as "sad")

|Minor|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|1|2|2|1|2|2|
|Relative|2|3|5|7|8|A|10|

When you look closely at the "between" steps of major and minor you can see that the scheme is actually the same, just starting at two steps further and wrapping around. This way you can alter any scale that goes from base to octave and make as many variants or modes as many steps the scale has. Using this technique we can generate the so called "(gregorian) modes" which all have their musical use and sound distinct from each other. These are all modes sorted from "happy" to "sad" or "light" to "dark"

|Lydian|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|2|2|1|2|2|1|
|Relative|2|4|6|7|9|B|10|

|Ionian/Major|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|2|1|2|2|2|1|
|Relative|2|4|5|7|9|B|10|

|Mixolydian|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|2|1|2|2|1|2|
|Relative|2|4|5|7|9|A|10|

|Dorian|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|1|2|2|2|1|2|
|Relative|2|3|5|7|9|A|10|

|Aeolian/Minor|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|2|1|2|2|1|2|2|
|Relative|2|3|5|7|8|A|10|

|Phrygian|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|1|2|2|2|1|2|2|
|Relative|1|3|5|7|8|A|10|

|Locrian|1|2|3|4|5|6|0|
|-|-|-|-|-|-|-|-|
|Between|1|2|2|1|2|2|2|
|Relative|1|3|5|6|8|A|10|

Now what is this all for you may ask? Well in music it can be quite difficult for a piece to sound coherent. Most musicians try to avoid notes which are "clashing" with each other. When you restrict the used notes of a musical piece to mostly those of a chosen scale you can achieve that more easily.

If you're interested in what other scales there are you can browse through this great site! https://ianring.com/musictheory/scales/

# What is a chord?

Now a chord is nothing but a set of notes played together at the same time. These are grouped by the amount of note played simultaneously. A three note chord is called a triad and these ones are the most common ones. If you only play two notes most people call it "power chord" (only god knows why). If you play more than three notes people usually can get really creative with chord naming so I'll spare you that.

The root note, which is usually the lowest note of the chord, gives the chord its name. You can construct a chord similarly to a scale by starting at the root note and adding steps. There are four common triads.

|Major|0|1|2|
|-|-|-|-|
|Between|0|4|3|
|Relative|0|4|7|

|Minor|0|1|2|
|-|-|-|-|
|Between|0|3|4|
|Relative|0|3|7|

|Diminished|0|1|2|
|-|-|-|-|
|Between|0|3|3|
|Relative|0|3|6|

|Augmented|0|1|2|
|-|-|-|-|
|Between|0|4|4|
|Relative|0|4|8|

So for example; If you wanted to play an E Augmented chord which is a 4 in integer notation. You would play the notes 4, 8, 0 .

(There is a relly cool and compact notation i came up with to convert something like a Cmaj7#11 or Fmaj7b5/E chord to something wich isn't only compact but more intuitively playable because it follows a system which expresses added notes more equally. But i need latex for that to display both subscript and superscript symbols. I'll add it soon. Trust me, it's super cool.)

Additionaly there are so called inversions of chords. You construct them by shifting the lowest note up an octave so that the lowest note is no longer the root. The first inversion is if you do this once, the second inversion if done twice, so the third note would be the lowest in this case. With the upper example starting with E2 it would result in

|Root Position|24|28|30|
|-|-|-|-|
|1. Inversion|28|30|34|
|2. Inversion|30|34|38|

Notation of chords with more than three notes (in traditional notation) usually is a bit hard to read, i refer to wikipedia for that... https://en.wikipedia.org/wiki/Chord_(music)#Notation_in_popular_music

# Stuff i want to say but doesn't fit anywhere

I made a little python script into which you can feed an arbitrary scale (and a root note) and it generates not only the scale or all possible modes of that but also can generate all possibly fitting chords. I found it very useful but it's not that easy to use. I'll work on that if I got time and motivation :-D

