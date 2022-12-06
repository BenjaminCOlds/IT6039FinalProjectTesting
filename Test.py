import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """
        TestBowlingGame is a class that is used to test the BowlingGame module.
    """

    def setUp(self):
        """
            This method sets up the BowlingGame to be used for testing purposes.
        """
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """
            This function is used to test the gutter game. It will roll 0's and assert whether the total score remains at 0. 
        """
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0

    def testAllOnes(self):
        """
            Throws 20 balls and checks to test if it only hit ones. 
        """
        self.rollMany(1, 20)

        assert self.game.score()==20
        
    def testOneSpare(self):
        """
            Tests for one spare.
        """
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)

        self.rollMany(0,17)

        assert self.game.score()==16

    def testOneStrike(self):
        """
            Tests to check whether strikes work. 
        """
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        
        self.rollMany(0,16)

        assert  self.game.score()==24

    def testPerfectGame(self):
        """
            Rolls many balls to test for a perfect game. 
        """
        self.rollMany(10,12)

        assert self.game.score()==300

    def testSecondSpare(self):
        """
            Rolls many balls and tests for spares. 
        """
        self.rollMany(5,21)

        assert self.game.score()==150

    def rollMany(self, pins,rolls):
        """
            Used as a helper function to roll mutliple balls.
        """
        for i in range(rolls):
            self.game.rolls(pins)

if __name__ == "__main__":
    unittest.main(verbosity=2)