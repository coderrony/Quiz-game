

class QuestionMode:
    def __init__(self, text, correct_n) -> None:
        self.text = text
        self.correct_n = correct_n

    def __repr__(self) -> str:
        return f"{self.text}  {self.correct_n}"
