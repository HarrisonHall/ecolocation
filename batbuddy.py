import datetime

class BatBuddy(Bat):
    LIFE_DEC = 20
    TIME_INC_SEC = datetime.timedelta(seconds=86400)

    def __init__(self, lf):
        self.life = lf;
        self.exp = 0;
        self.level = 1;
        self.starttime = datetime.datetime.now()

    def update_life(self):
        diff = datetime.datetime.now() - self.starttime
        self.life -= int(diff.total_seconds() / TIME_INC_SEC.total_seconds()) * LIFE_DEC
