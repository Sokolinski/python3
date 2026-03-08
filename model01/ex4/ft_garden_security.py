class secure_plant():
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        print(f"Plant created: {self._name}")
        self._height = 0
        self._age = 0
    
    def set_heigth(self, heigth_set: int):
        if heigth_set < 0:
            print(f"Invalid operation attempted: height {heigth_set}m [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = heigth_set
            print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age_set: int):
        if age_set < 0:
            print(f"Invalid operation attempted: age {age_set}m [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age_set
            print(f"Age updated: {age_set} days [OK]")

    def get_heigth(self):
        return self._height
    
    def get_age(self):
        return self._age
    
    def print_info(self):
        print(f"Current plant: {self._name} ({self.get_heigth()}cm,"
              f" {self.get_age()} days)")

def main():
    print("=== Garden Security System ===")
    rose = secure_plant("Rose", 0, 0)
    rose.set_heigth(25)
    rose.set_age(30)
    print()
    rose.set_heigth(-5)
    print()
    rose.print_info()

if __name__ == "__main__":
    main()