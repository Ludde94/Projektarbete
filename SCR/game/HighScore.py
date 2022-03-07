import dice
import player

class Highscore():
    score = dice.Dice
    rollsmade = score.get_rolls_made
    player= player.Player
    name = player.player
    
    
    def __init__(self):
        """object of class"""
        self.save_to_highscore
        self.highscores
        

    def highscores(self):
        with open('Highscores.txt', 'r') as Highscores_file:
            name = Highscores_file.readline().rstrip('\n')
            while name != '':
                count = int(Highscores_file.readline())
                print(f'{name} scored {count} points.')
                name = Highscores_file.readline().rstrip('\n')


    def save_to_highscore(self, rollsmade, name):
        with open('Highscores.txt', 'w') as Highscores_file:
            Highscores_file.write(f'{name} with {rollsmade} rolls')
            
            
    def sort_highscore(self):
        scores = []
        with open('Highscores.txt', 'r') as Highscores_file:
            for line in Highscores_file:
                name = Highscores_file.readline().rstrip('\n')
                score =  Highscores_file.readline().rstrip('\n')
                scores.append(int(score))
        scores.sort(reverse=True)
        print(f'{name} with {scores} rolls'[0:5])
            
            
                