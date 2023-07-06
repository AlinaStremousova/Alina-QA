class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Alina"
        self.second_name = "Stremousova"

    def remove(self):
        self.name = ""
        self.second_name = ""

    def test_change_name():
        user = User()
        user.create()

        assert user.name == "Alina"
        user.remove()

    def test_change_second_name():
        user = User()
        user.create()

        assert user.second_name == "Stremousova"
        user.remove()
        