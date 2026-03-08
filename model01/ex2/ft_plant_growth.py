class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def blueprinter(self):
        print(f"{self.name}: {self.height}cm , {self.age} days old")
    
    def grow(self):
        self.height += 6
    
    def age_up(self):
        self.age += 6
    
    def get_info(self):
        self.blueprinter()

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    print("=== Day 7 ===")
    rose.grow()
    rose.age_up()
    rose.get_info()
    print("Growth this week: +6cm")
    rose.grow()
    rose.age_up()
    rose.get_info()