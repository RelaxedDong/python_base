from Father import Father
from Mather import Mother
class Son(Mother,Father):
    def __init__(self,money,facevalue,uid):
        Mother.__init__(self,facevalue)

        Father.__init__(self,money)
        self.uid = uid

