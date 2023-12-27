class Square:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.piece = None
        if ((x-y) % 2 == 0):
            self.color = 'w'
        else:
            self.color = 'b'
    
    def isEmpty(self):
        """Returns True if square is empty, False otherwise"""
        return self.piece == None
    
    def getPiece(self):
        """Returns the piece at the square, or None if the square is empty"""
        return self.piece
    
