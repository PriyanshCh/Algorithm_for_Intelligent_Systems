class NQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        if target_row == self.size:
            self.show_full_board(positions)
            self.show_short_board(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, target_row, column):
        for i in range(target_row):
            if positions[i] == column or \
               positions[i] == column - (target_row - i) or \
               positions[i] == column + (target_row - i):
                return False
        return True

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q"
                else:
                    line += "."
            print(line)
        print("\n")

    def show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    NQueens(8)

if __name__ == "__main__":
    main()
