import MiniProject01.ScoreManager as ScoreManager
import MiniProject01.GameManager as GameManager

def Run():
    ScoreManager.LoadScoresFromFiles()
    
    (_name, _score) = GameManager.PlayGameLoop()
    ScoreManager.UpdateUserScore(_name, _score)
    ScoreManager.ShowLeaderboard()