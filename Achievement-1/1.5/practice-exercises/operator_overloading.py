class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __sub__(self, obj):
        # covnerting height into inches
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = obj.feet * 12 + obj.inches

        total_height_inches = height_A_inches - height_B_inches
        output_feet = total_height_inches // 12

        output_inches = total_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)

    def __gt__(self, obj):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = obj.feet * 12 + obj.inches
        return height_A_inches > height_B_inches

    def __ge__(self, obj):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = obj.feet * 12 + obj.inches
        return height_A_inches >= height_B_inches

    def __ne__(self, obj):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = obj.feet * 12 + obj.inches
        return height_A_inches != height_B_inches


Paul_height = Height(5, 10)
Philippe_height = Height(3, 9)

height_sub = Paul_height - Philippe_height

print("Total height: ", height_sub)

print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))
