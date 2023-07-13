class Question():
    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer
    def __repr__(self) -> str:
        return f"{self.text} : {self.answer}"