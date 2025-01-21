class sanket:
    sid: int
    ssub: str

    def s_getdata(self):
        self.sid = input("Enter Sanket's ID:")
        self.ssub = input("Enter Sanket's Subject:")


class nirav:
    nid: int
    nsub: str

    def n_getdata(self):
        self.nid = input("Enter Nirav's ID:")
        self.nsub = input("Enter Nirav's Subject:")


class ashok:
    aid: int
    asub: str

    def a_getdata(self):
        self.aid = input("Enter Ashok's ID:")
        self.asub = input("Enter Ashok's Subject:")


class tops(sanket, nirav, ashok):
    def prindata(self):
        print("---------Sanket's Data--------")
        print("Sanket's ID:", self.sid)
        print("Sanket's Subject:", self.ssub)
        print("---------Nirav's Data--------")
        print("Nirav's ID:", self.nid)
        print("Nirav's Subject:", self.nsub)
        print("---------Ashok's Data--------")
        print("Ashok's ID:", self.aid)
        print("Ashok's Subject:", self.asub)


tp = tops()
tp.s_getdata()
tp.n_getdata()
tp.a_getdata()
tp.prindata()
