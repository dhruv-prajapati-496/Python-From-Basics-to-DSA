# Encapsulation : Wrapping data and functions into a single unit(object).
class PhoneVolume:
    def __init__(self):
        self._volume = 50  # Protected attribute (0 to 100)

    def set_volume(self, new_volume):
        if 0 <= new_volume <= 100:
            self._volume = new_volume
        else:
            print("Volume must be between 0 and 100!")

    def get_volume(self):
        return self._volume


phone = PhoneVolume()
phone.set_volume(75)
print("Volume:", phone.get_volume())  # 75

phone.set_volume(150)               # Rejected because it's above 100
print("Volume:", phone.get_volume())  # Still 75

# Encapsulation simply means keeping data safe inside a class and changing it through methods that check rules first.