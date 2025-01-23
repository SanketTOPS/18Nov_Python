class master:
    def login(self, unm, pas):
        print("Username:", unm)
        print("Password:", pas)


class home(master):
    def login(self, unm, pas):
        return super().login(unm, pas)


class about(master):
    def login(self, unm, pas):
        return super().login(unm, pas)
