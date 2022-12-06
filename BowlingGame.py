class BowlingGame:
    """
        BowlingGame is a game designed for high school age students. The game is a 10pin bowling game prototype that will be used to teach a variety of subjects. 
    """
    def __init__(self):
        """
            Constructor for BowlingGame, when a game is initalized it will construct an empty list that will be utilised throughout the project.
        """
        self.rolls=[]

    def roll(self,pins):
        """
            Rolls a ball and adds the value onto self.rolls. 
        """
        self.rolls.append(pins)

    def score(self):
        """
            Used to calculate the total score of rolls. 
            
            Returns the total result. 
        """
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if frameIndex in range(10):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
            rollIndex +=2
            return result

    def isStrike(self, rollIndex):
        """
            Used to figure out if a hit was a strike or not. 
        """
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        """
            Used to figure out if two balls were a spare.
        """
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    def strikeScore(self,rollIndex):
        """
            Calculates and returns the strike score. 
        """
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """
            Calculates and returns the spare score. 
        """
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """
            Calculates what the frame score is. 
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]