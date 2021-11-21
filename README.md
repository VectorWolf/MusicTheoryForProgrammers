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

# What is an interval?

The space between two played notes is called an interval. For example we already know that if two notes are 12 steps or semitones apart it's called an octave. The really interesting part about intervals is how they sound together. Frequencies with simple rations to each other usually sound nice together. But there are also other things to factor in. The distance to the base note for example. A somewhat bad sounding interval usually is way more bearable if played an octave higher. Also the so called overtones an instrument produces are a huge factor and can totally mess up the perceived consonance or dissonance of the intervals.

To estimate how consonant or dissonnant a chord will sound it can be useful to "rank" the intervals in "niceness". That'll make it possible to asess the overall niceness of any chord we construct. (It is said that the inverse of a note is functionally equivalent, but this also inverts the interval. To make things easier and way more practical the inverse of an interval will always have the same niceness. This makes the inversions of a chord theoratically just as nice as the base chord.)

|Step     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Trad. Name|Perfect Unison|Minor second|Major second|Minor third|Major third|Perfect fourth|Tritone|Perfect Fifth|Minor Sixth|Major sixth|Minor Seventh|Major Seventh|Perfect Octave|
|Niceness | +3  | -2  | -1  |  0  |  +1 |  +2 | -1  |  +2 |  +1 |  0  |  -1 |  -2 |  +3 |

(I'm totally not sure on a good way to come up with a niceness that can be practically used. Currently a major/minor chord would be less nice than their sus counterpart which doesn't match up with the perceived consonance. Maybe better make the metric about dissonance? Gonna test this out with 0 at octave and 1 at 1 and 11 semitones.)

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

# Equations I guess?
<!--- Generated with https://www.codecogs.com/latex/eqneditor.php -->

Here you can see an alternative method for displaying all common types of triads in integer notation. The + in superscript means "Add the root plus this step as an additional note", the minus sign works analogous. You may add seperators between the notes for readability. Instead of using a valid base 12 root you may write X as a placeholder or a numeral followed by a dot and a d (1.d or 4.d) for indicating a scale degree.

The subscript "#,%,d,a,s2,s5" symbols are nothing but mere macros as you may know from programming.

In addition to plus and minus there is also the o, which stands for "omit". So a 5#/o+7 wouldn't be 5|9|0 but only 5|9.

You can also specify a chord at a specific tonal height by using a two digit number as the root.

You can also express inversions by appending +1, +2, -1 or -2 to the subscript. This means you can only invert the root and the notes expressed by the subscript macro. This means for tetrads, pentads or more you have to either adjust the superscript accordingly to match the inversion or define a macro for these chords locally.

### Notation of common triads
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5C%5CD_%20%7BMaj%7D%20%3D%20D%7CF_%5C%23%7CA%20%3D%202%7C6%7C9%20%3D%202%5E%7B6%7C9%7D%20%3D%202%5E%7B&plus;4&plus;7%7D%20%3D%202_%7B%5C%23%7D%5C%5C%20E_%7BMin%7D%20%3D%20E%7CG%7CB%20%3D%204%7C7%7CB%20%3D%204%5E%7B7%7CB%7D%20%3D%204%5E%7B&plus;3&plus;7%7D%20%3D%204_%7B%5C%25%7D%5C%5C%20F_%7BDim%7D%20%3D%20F%7CG_%5C%23%7CB%20%3D%205%7C8%7CB%20%3D%205%5E%7B8%7CB%7D%20%3D%205%5E%7B&plus;3&plus;6%7D%20%3D%205_%7Bd%7D%5C%5C%20G_%7BAug%7D%20%3D%20G%7CC%7CE%20%3D%207%7C0%7C4%20%3D%207%5E%7B0%7C4%7D%20%3D%207%5E%7B&plus;4&plus;8%7D%20%3D%207_%7Ba%7D%5C%5C%20A_%7BSus2%7D%20%3D%20A%7CB%7CE%20%3D%209%7CB%7C4%20%3D%209%5E%7BB%7C4%7D%20%3D%209%5E%7B&plus;2&plus;7%7D%20%3D%209_%7Bs2%7D%5C%5C%20B_%7BSus4%7D%20%3D%20B%7CE%7CF_%5C%23%20%3D%20B%7C4%7C6%20%3D%20B%5E%7B4%7C6%7D%20%3D%20B%5E%7B&plus;5&plus;7%7D%20%3D%20B_%7Bs5%7D%5C%5C"> <img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5C%5C%5CRightarrow%20X%5E%7B&plus;4&plus;7%7D%20%3D%20X_%7B%5C%23%7D%5C%5C%20%5CRightarrow%20X%5E%7B&plus;3&plus;7%7D%20%3D%20X_%7B%5C%25%7D%5C%5C%20%5CRightarrow%20X%5E%7B&plus;3&plus;6%7D%20%3D%20X_%7Bd%7D%5C%5C%20%5CRightarrow%20X%5E%7B&plus;4&plus;8%7D%20%3D%20X_%7Ba%7D%5C%5C%20%5CRightarrow%20X%5E%7B&plus;2&plus;7%7D%20%3D%20X_%7Bs2%7D%5C%5C%20%5CRightarrow%20X%5E%7B&plus;5&plus;7%7D%20%3D%20X_%7Bs5%7D">
<!---
\\D_ {Maj} = D|F_\#|A = 2|6|9 = 2^{6|9} = 2^{+4+7} = 2_{\#}\\
E_{Min} = E|G|B = 4|7|B = 4^{7|B} = 4^{+3+7} = 4_{\%}\\
F_{Dim} = F|G_\#|B = 5|8|B = 5^{8|B} = 5^{+3+6} = 5_{d}\\
G_{Aug} = G|C|E = 7|0|4 = 7^{0|4} = 7^{+4+8} = 7_{a}\\
A_{Sus2} = A|B|E = 9|B|4 = 9^{B|4} = 9^{+2+7} = 9_{s2}\\
B_{Sus4} = B|E|F_\# = B|4|6 = B^{4|6} = B^{+5+7} = B_{s5}\\
-->

<!---
\\\Rightarrow X^{+4+7} = X_{\#}\\
\Rightarrow X^{+3+7} = X_{\%}\\
\Rightarrow X^{+3+6} = X_{d}\\
\Rightarrow X^{+4+8} = X_{a}\\
\Rightarrow X^{+2+7} = X_{s2}\\
\Rightarrow X^{+5+7} = X_{s5}
-->

### Chords at specific tonal height
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20G_3%5C%23_%7BMinor%7D%20%3D%2038%7C3B%7C43%20%3D%2038%5E%7B3B%7C43%7D%20%3D%2038%5E%7B&plus;3&plus;7%7D%20%3D%2038_%7B%5C%25%7D">
<!---
G_3\#_{Minor} = 38|3B|43 = 38^{3B|43} = 38^{+3+7} = 38_{\%}
-->

### Omit sign
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20G5%20%3D%20G%7CC%20%3D%207%7C0%20%3D%207_%7B%5C%23%7D%5E%7Bo&plus;4%7D%20%3D%207_%7B%5C%23%7D%5E%7Bo4%7D%20%3D%207%5E%7B&plus;7%7D">
<!---
G5 = G|C = 7|0 = 7_{\#}^{o+4} = 7_{\#}^{o4} = 7^{+7}
-->
You may skip the sign after the "o" if the note isn't ambiguous (means there is no +x AND -x at the same time inside the macro of the subscript)

### Inversions
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5C%5C0%7C4%7C7%20%3D%200%5E%7B&plus;4&plus;7%7D%20%3D%200_%7B%5C%23%7D%5C%5C%204%7C7%7C0%20%3D%200%5E%7Bo0&plus;10%7D_%7B%5C%23%7D%20%3D%200_%7B%5C%23&plus;1%7D%20%3D%200_%7B%5C%23-2%7D%5C%5C%207%7C0%7C4%20%3D%200%5E%7Bo4&plus;14%7D_%7B%5C%23&plus;1%7D%20%3D%200_%7B%5C%23&plus;2%7D%20%3D%200_%7B%5C%23-1%7D%5C%5C%20%5C%5C%2024%7C27%7C30%20%3D%2020_%7B%5C%23&plus;1%7D%5Cneq20_%7B%5C%23-2%7D%20%3D%2013%7C17%7C20">
<!---
\\0|4|7 = 0^{+4+7} = 0_{\#}\\
4|7|0 = 0^{o0+10}_{\#} = 0_{\#+1} = 0_{\#-2}\\
7|0|4 = 0^{o4+14}_{\#+1} = 0_{\#+2} = 0_{\#-1}\\
\\
24|27|30 = 20_{\#+1}\neq20_{\#-2} = 13|17|20
-->
These equations only show an example and not directly the principle of "pushing the lowest note up an octave"/"dropping the highest note down an octave". But it should get the point across nevertheless

### Scale degrees
Lets take for context the scale 2741 (Ionian/Major). It has the intervals [2,2,1,2,2,2,1] and the notes of the scale relative to the root note are {0,2,4,5,7,9,B}
The common triads for each degree of the scale are:

<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5C%5C1.d_%7B%5C%23%7D%5C%5C%202.d_%7B%5C%25%7D%5C%5C%203.d_%7B%5C%25%7D%5C%5C%204.d_%7B%5C%23%7D%5C%5C%205.d_%7B%5C%23%7D%5C%5C%206.d_%7B%5C%25%7D%5C%5C%207.d_%7Bd%7D"> or <img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5Clarge%20%5C%5C&plus;0_%7B%5C%23%7D%5C%5C%20&plus;2_%7B%5C%25%7D%5C%5C%20&plus;4_%7B%5C%25%7D%5C%5C%20&plus;5_%7B%5C%23%7D%5C%5C%20&plus;7_%7B%5C%23%7D%5C%5C%20&plus;9_%7B%5C%25%7D%5C%5C%20&plus;B_%7Bd%7D"> in root relative notation.

Using this notation you know what chords to play at which degree. If you use the second notation the scale is even encoded into the chords and you only need to add each chord onto the root note (modulo 12) to get all matching chords for the scale/mode.

<!---
\\1.d_{\#}\\
2.d_{\%}\\
3.d_{\%}\\
4.d_{\#}\\
5.d_{\#}\\
6.d_{\%}\\
7.d_{d}

\\+0_{\#}\\
+2_{\%}\\
+4_{\%}\\
+5_{\#}\\
+7_{\#}\\
+9_{\%}\\
+B_{d}
-->

### Common Tetrads, Pentads, Hexads and so on...
Just a collection of the stuff I can dig up on wikipedia of what to seem somewhat common and useful chords. I'll always take the 0 chord as reference.
#### Seventh Chords
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5C%5CDiminishedSeventh%20%3D%20Cdim%5E7%20%3D%20C%7CE_b%7CG_b%7CB_%7Bbb%7D%20%3D%200%7C3%7C6%7C9%20%3D%200_%7Bd%7D%5E%7B&plus;9%7D%5C%5C%20HalfDiminishedSeventh%20%3D%20Cm%5E%7B7b5%7D%20%3D%20C%7CE_b%7CG_b%7CB_b%20%3D%200%7C3%7C6%7CA%20%3D%200_%7Bd%7D%5E%7B&plus;A%7D%5C%5C%20MinorSeventh%20%3D%20Cm%5E%7B7%7D%20%3D%20C%7CE_b%7CG%7CB_b%20%3D%200%7C3%7C7%7CA%20%3D%200_%7B%25%7D%5E%7B&plus;A%7D%5C%5C%20MinorMajorSeventh%20%3D%20Cm%5E%7Bmaj7%7D%20%3D%20C%7CE_b%7CG%7CB%20%3D%200%7C3%7C7%7CB%20%3D%200_%7B%25%7D%5E%7B&plus;B%7D%5C%5C%20DominantSeventh%20%3D%20C%5E%7B7%7D%20%3D%20C%7CE%7CG%7CB_b%20%3D%200%7C4%7C7%7CA%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A%7D%5C%5C%20MajorSeventh%20%3D%20C%5E%7Bmaj7%7D%20%3D%20C%7CE%7CG%7CB%20%3D%200%7C4%7C7%7CB%20%3D%200_%7B%5C%23%7D%5E%7B&plus;B%7D%5C%5C%20AugmentedSeventh%20%3D%20Caug%5E%7B7%7D%20%3D%20C%7CE%7CG_%5C%23%7CB_b%20%3D%200%7C4%7C8%7CA%20%3D%200_%7Ba%7D%5E%7B&plus;A%7D%5C%5C%20AugmentedMajorSeventh%20%3D%20Caug%5E%7Bmaj7%7D%20%3D%20C%7CE%7CG_%5C%23%7CB%20%3D%200%7C4%7C8%7CB%20%3D%200_%7Ba%7D%5E%7B&plus;B%7D">
<!---
\\DiminishedSeventh = Cdim^7 = C|E_b|G_b|B_{bb} = 0|3|6|9 = 0_{d}^{+9}\\
HalfDiminishedSeventh = Cm^{7b5} = C|E_b|G_b|B_b = 0|3|6|A = 0_{d}^{+A}\\
MinorSeventh = Cm^{7} = C|E_b|G|B_b = 0|3|7|A = 0_{%}^{+A}\\
MinorMajorSeventh = Cm^{maj7} = C|E_b|G|B = 0|3|7|B = 0_{%}^{+B}\\
DominantSeventh = C^{7} = C|E|G|B_b = 0|4|7|A = 0_{\#}^{+A}\\
MajorSeventh = C^{maj7} = C|E|G|B = 0|4|7|B = 0_{\#}^{+B}\\
AugmentedSeventh = Caug^{7} = C|E|G_\#|B_b = 0|4|8|A = 0_{a}^{+A}\\
AugmentedMajorSeventh = Caug^{maj7} = C|E|G_\#|B = 0|4|8|B = 0_{a}^{+B}
-->

#### Extended Chords
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5C%5CDominantNinth%20%3D%20C%5E9%20%3D%20C%7CE%7CG%7CB_b%7CD%20%3D%200%7C3%7C6%7CA%7C2%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;12%7D%5C%5C%20DominantEleventh%20%3D%20C%5E%7B11%7D%20%3D%20C%7CE%7CG%7CB_b%7CD%7CF%20%3D%200%7C3%7C6%7CA%7C2%7C5%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;12&plus;15%7D%5C%5C%20DominantThirteenth%20%3D%20C%5E%7B13%7D%20%3D%20C%7CE%7CG%7CB_b%7CD%7CF%7CA%20%3D%200%7C3%7C6%7CA%7C2%7C5%7C9%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;12&plus;15&plus;19%7D">
<!---
\\DominantNinth = C^9 = C|E|G|B_b|D = 0|3|6|A|2 = 0_{\#}^{+A+12}\\
DominantEleventh = C^{11} = C|E|G|B_b|D|F = 0|3|6|A|2|5 = 0_{\#}^{+A+12+15}\\
DominantThirteenth = C^{13} = C|E|G|B_b|D|F|A = 0|3|6|A|2|5|9 = 0_{\#}^{+A+12+15+19}
-->

#### Altered chords
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5C%5CSeventhMinorNinth%20%3D%20C%5E%7B7b9%7D%20%3D%20C%7CE%7CG%7CB_b%7CD_b%20%3D%200%7C4%7C7%7CA%7C1%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;11%7D%5C%5C%20SeventhSharpNinth%20%3D%20C%5E%7B7%5C%239%7D%20%3D%20C%7CE%7CG%7CB_b%7CD_%5C%23%20%3D%200%7C4%7C7%7CA%7C3%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;13%7D%5C%5C%20SeventhAugmentedEleventh%20%3D%5C%5C%20C%5E%7B7%5C%2311%7D%20%3D%20C%7CE%7CG%7CB_b%7CD%7CF_%5C%23%20%3D%200%7C4%7C7%7CA%7C2%7C6%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;12&plus;16%7D%5C%5C%20SeventhDiminishedThirteenth%20%3D%5C%5C%20C%5E%7B7b13%7D%20%3D%20C%7CE%7CG%7CB_b%7CD%7CF%7CA_b%20%3D%200%7C4%7C7%7CA%7C2%7C5%7C8%20%3D%200_%7B%5C%23%7D%5E%7B&plus;A&plus;12&plus;15&plus;18%7D">
<!---
\\SeventhMinorNinth = C^{7b9} = C|E|G|B_b|D_b = 0|4|7|A|1 = 0_{\#}^{+A+11}\\
SeventhSharpNinth = C^{7\#9} = C|E|G|B_b|D_\# = 0|4|7|A|3 = 0_{\#}^{+A+13}\\
SeventhAugmentedEleventh =\\ C^{7\#11} = C|E|G|B_b|D|F_\# = 0|4|7|A|2|6 = 0_{\#}^{+A+12+16}\\
SeventhDiminishedThirteenth =\\ C^{7b13} = C|E|G|B_b|D|F|A_b = 0|4|7|A|2|5|8 = 0_{\#}^{+A+12+15+18}
-->

#### Added tone chords
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5C%5CAddNine%20%3D%20C%5E%7Badd9%7D%20%3D%20C%7CE%7CG%7CD%20%3D%200%7C4%7C7%7C2%20%3D%200_%7B%5C%23%7D%5E%7B&plus;12%7D%5C%5C%20AddFourth%20%3D%20C%5E%7Badd11%7D%20%3D%20C%7CE%7CG%7CF%20%3D%200%7C4%7C7%7C5%20%3D%200_%7B%5C%23%7D%5E%7B&plus;15%7D%5C%5C%20AddSixth%20%3D%20C%5E%7B6%7D%20%3D%20C%7CE%7CG%7CA%20%3D%200%7C4%7C7%7C9%20%3D%200_%7B%5C%23%7D%5E%7B&plus;9%7D%5C%5C%20SixNine%20%3D%20C%5E%7B6/9%7D%20%3D%20C%7CE%7CG%7CA%7CD%20%3D%200%7C4%7C7%7C9%7C2%20%3D%200_%7B%5C%23%7D%5E%7B&plus;9&plus;12%7D%5C%5C%20SevenSix%20%3D%20C%5E%7B7/6%7D%20%3D%20C%7CE%7CG%7CA%7CB_b%20%3D%200%7C4%7C7%7C9%7CA%20%3D%200_%7B%5C%23%7D%5E%7B&plus;9&plus;A%7D">
<!---
\\AddNine = C^{add9} = C|E|G|D = 0|4|7|2 = 0_{\#}^{+12}\\
AddFourth = C^{add11} = C|E|G|F = 0|4|7|5 = 0_{\#}^{+15}\\
AddSixth = C^{6} = C|E|G|A = 0|4|7|9 = 0_{\#}^{+9}\\
SixNine = C^{6/9} = C|E|G|A|D = 0|4|7|9|2 = 0_{\#}^{+9+12}\\
SevenSix = C^{7/6} = C|E|G|A|B_b = 0|4|7|9|A = 0_{\#}^{+9+A}
-->

#### Others
<img src="https://latex.codecogs.com/png.latex?%5Cdpi%7B150%7D%20%5Cbg_white%20%5C%5CPowerChord%20%3D%20C5%20%3D%20C%7CG%20%3D%200%7C7%20%3D%200%5E%7B&plus;7%7D%5C%5C%20SlashChord%20%3D%20C/D%20%3D%20D%7CC%7CE%7CG%20%3D%202%7C0%7C4%7C7%20%3D%200_%5C%23%5E%7B-10%7D%5C%5C%20SlashChord%20%3D%20C/G%20%3D%20G%7CC%7CE%20%3D%207%7C0%7C4%20%3D%200_%7B%5C%23-1%7D">
<!---
\\PowerChord = C5 = C|G = 0|7 = 0^{+7}\\
SlashChord = C/D = D|C|E|G = 2|0|4|7 = 0_\#^{-10}\\
SlashChord = C/G = G|C|E = 7|0|4 = 0_{\#-1}
-->

### Why use this?
Because it has one big strong point. If you learn the relatively easy principles how to build a chord with this system, you can read and write any possible chord existing inside the 12-tone equal temperament system. 

# Stuff i want to say but doesn't fit anywhere

I made a little python script into which you can feed an arbitrary scale (and a root note) and it generates not only the scale or all possible modes of that but also can generate all possibly fitting chords. I found it very useful but it's not that easy to use. I'll work on that if I got time and motivation :-D

