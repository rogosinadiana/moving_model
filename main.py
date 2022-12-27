import random
class area:
    @staticmethod
    def create_area(field_size):
        matrix = [['.' for X in range(field_size)] for Y in range(field_size)]
        return matrix
class coordinate:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
class character:
    @staticmethod
    def move(move,coordinates):
        if move=='up':
            coordinates.Y-=1
        elif move=='down':
            coordinates.Y+=1
        elif move=='left':
            coordinates.X-=1
        elif move=='right':
            coordinates.X+=1
        else:
            exit()
        return coordinates
class controller:
    @staticmethod
    def locate(field_size,coordinates):
        matrix=area.create_area(field_size)
        matrix[coordinates.Y][coordinates.X]='1'
        return matrix
    @staticmethod
    def display(field_size,coordinates):
        matrix=controller.locate(coordinates,field_size)
        for Y in range(len(matrix)):
            for X in range(len(matrix)):
                print(matrix[Y][X],end=' ')
            print()
        print()
    @staticmethod
    def check_bounds(coordinates,field_size):
        if coordinates.Y<0:
            coordinates.Y=0
        if coordinates.Y==field_size:
            coordinates.Y=field_size-1
        if coordinates.X<0:
            coordinates.X=0
        if coordinates.X==field_size:
            coordinates.X=field_size-1
        return coordinates
def main():
    field_size = int(input('ВВЕДИТЕ РАЗМЕР ПОЛЯ:'))
    Y0=random.randint(0,field_size-1)
    X0=random.randint(0,field_size-1)
    coordinates=coordinate(X0,Y0)
    while True:
        controller.display(coordinates,field_size)
        move=input('ВВЕДИТЕ НАПРАВЛЕНИЕ ИЛИ НАЖМИТЕ ЛЮБУЮ КЛАВИШУ ДЛЯ ЗАВЕРШЕНИЯ:')
        character.move(move,coordinates)
        controller.check_bounds(coordinates,field_size)
main()