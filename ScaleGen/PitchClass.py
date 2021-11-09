import copy

class PitchClass:
    """
    Pitch Class representation inside 12 note equal temperament
    """
    # Set to true for a more civilized output :-D
    DUODEC = False
    NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    
    def __init__(self, interval_structure):
        """
        Initialize pitch class by given interval structure
        """
        self.intervals = interval_structure
        if sum(self.intervals) != 12:
            print("Interval sum isn't 12, revert to chromatic scale")
            self.intervals = [1,1,1,1,1,1,1,1,1,1,1,1]
        self.setup()
    
    def setup(self):
        """
        Sets up helper variables after change of interval structure
        """
        self._is_prime = None
        self.pitch = [0]
        last_val = 0
        for i in self.intervals:
            last_val += i
            self.pitch.append(last_val)
        self.pitch.pop()
        self.cardinality = len(self.pitch)
        self.enumerator = 0
        for p in self.pitch:
            self.enumerator += pow(2,p)
    
    def permute(self, steps = 1):
        """
        Shifts pitch class into next mode
        """
        for i in range(steps):
            self.intervals.append(self.intervals[0])
            self.intervals.pop(0)
        self.setup()
    
    def generate_all_modes(self):
        modes = []
        tmp = copy.deepcopy(self)
        for c in range(self.cardinality):
            modes.append(copy.deepcopy(tmp))
            tmp.permute()
        return modes
    
    def make_prime(self):
        """
        Converts pitch class into its prime form
        """
        tmp = min(self.generate_all_modes())
        self.__init__(tmp.intervals)
        
    def is_prime(self):
        if self._is_prime == None:
            tmp = copy.deepcopy(self)
            tmp.make_prime()
            if tmp == self:
                self._is_prime = True
            else:
                self._is_prime = False
        return self._is_prime
        
    def get_chords(self):
        chords = []
        tmp = PitchClass(self.intervals)
        for i in range(self.cardinality):
            chords.append(tmp.get_first_chord())
            tmp.permute()
        return chords
        
    def get_degree_pitch(self):
        degs = []
        tmp = PitchClass(self.intervals)
        for i in range(self.cardinality):
            degs.append(tmp.pitch)
            tmp.permute()
        return degs
        
    def print_chords(self):
        chords = self.get_chords()
        degs = self.get_degree_pitch()
        for i in range(self.cardinality):
            print(str(i+1) + ". Deg:\n" + str(degs[i]) + "\n" + str(chords[i]))
            print()
            
    def print_chords_of_scale(self, base):
        scale = self.get_scale(base)
        chords = self.get_chords()
        degs = self.get_degree_pitch()
        print("Scale:")
        print(scale)
        print()
        for i in range(self.cardinality):
            print(scale[i] + " :\n" + str(degs[i]) + "\n" + str(chords[i]))
            print()
    
    def get_scale(self, base):
        scale = []
        for p in self.pitch:
            tmp = base + p
            scale.append(self.to_duodec(tmp))
        return scale
    
    @classmethod
    def to_duodec(cls,n):
        n = n % 12
        if cls.DUODEC:
            if n == 10:
                return 'A'
            elif n == 11:
                return 'B'
            else:
                return str(n)
        else:
            return cls.NOTES[n]
        
    def get_first_chord(self):
        chords = []
        if 3 in self.pitch:
            if 6 in self.pitch:
                chords.append("Diminished")
                if 8 in self.pitch:
                    chords.append("(+8)")
        if 7 in self.pitch:
            if 2 in self.pitch:
                chords.append("Sus2")
            if 3 in self.pitch:
                chords.append("Minor")
            if 4 in self.pitch:
                chords.append("Major")
            if 5 in self.pitch:
                if self.DUODEC:
                    chords.append("Sus5")
                else:
                    chords.append("Sus4")
        if 4 in self.pitch:
            if 8 in self.pitch:
                chords.append("Augmented")
                if 2 in self.pitch:
                    chords.append("(+2)")
                if 6 in self.pitch:
                    chords.append("(+6)")
        if chords:
            if 9 in self.pitch:
                if self.DUODEC:
                    chords.append("(+9)")
                else:
                    chords.append("(Add6)")
            if 10 in self.pitch:
                if self.DUODEC:
                    chords.append("(+10)")
                else:
                    chords.append("(Add7)")
            if 11 in self.pitch:
                if self.DUODEC:
                    chords.append("(+11)")
                else:
                    chords.append("(AddMaj7)")
        return chords
            
    def __lt__(self, other):
        return self.enumerator < other.enumerator
    def __le__(self, other):
        return self.enumerator <= other.enumerator
    def __gt__(self, other):
        return self.enumerator > other.enumerator
    def __ge__(self, other):
        return self.enumerator >= other.enumerator
    def __eq__(self, other):
        return self.enumerator == other.enumerator
    def __ne__(self, other):
        return self.enumerator != other.enumerator
    def __str__(self):
        tmp = ""
        tmp += "Enumerator: " + str(self.enumerator) + "\n"
        tmp += "Cardinality: " + str(self.cardinality) + "\n"
        tmp += "Pitch Class: " + str(self.pitch) + "\n"
        tmp += "Intervals: " + str(self.intervals) + "\n"
        tmp += "Is prime: " + str(self.is_prime()) + "\n"
        return tmp
        
if __name__ == "__main__":
    # Insert arbitrary in between notes here
    r = [2,2,1,2,2,2,1] # Ionian / Major scale for example
    
    p = PitchClass(r)
    
    # Shows scale information
    print(p)
    
    # Use this to print chords in a root agnostic fashion
    #p.print_chords()
    
    # Use this to print chords in relation to root note
    p.print_chords_of_scale(4) # E note for example
    
    # Uncomment to generate all modes and print them
    #for m in p.generate_all_modes():
    #    print(m)
    
        