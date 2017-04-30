# Rifle, Firearm, Shotgun, Handgun, Gun
class Firearms:
    state_data = [['Alabama', 0],
                  ['Alaska', 0],
                  ['Arizona', 0],
                  ['Arkansas', 0],
                  ['California', 0],
                  ['Colorado', 0],
                  ['Connecticut', 0],
                  ['Delaware', 0],
                  ['Florida', 0],
                  ['Georgia', 0],
                  ['Hawaii', 0],
                  ['Idaho', 0],
                  ['Illinois', 0],
                  ['Indiana', 0],
                  ['Iowa', 0],
                  ['Kansas', 0],
                  ['Kentucky', 0],
                  ['Louisiana', 0],
                  ['Maine', 0],
                  ['Maryland', 0],
                  ['Massachusetts', 0],
                  ['Michigan', 0],
                  ['Minnesota', 0],
                  ['Mississippi', 0],
                  ['Missouri', 0],
                  ['Montana', 0],
                  ['Nebraska', 0],
                  ['Nevada', 0],
                  ['New Hampshire', 0],
                  ['New Jersey', 0],
                  ['New Mexico', 0],
                  ['New York', 0],
                  ['North Carolina', 0],
                  ['North Dakota', 0],
                  ['Ohio', 0],
                  ['Oklahoma', 0],
                  ['Oregon', 0],
                  ['Pennsylvania', 0],
                  ['Rhodes Island', 0],
                  ['South Carolina', 0],
                  ['South Dakota', 0],
                  ['Tennessee', 0],
                  ['Texas', 0],
                  ['Utah', 0],
                  ['Vermont', 0],
                  ['Virginia', 0],
                  ['Washington', 0],
                  ['West Virginia', 0],
                  ['Wisconsin', 0],
                  ['Wyoming', 0]
                  ]

    def __init__(self, homicide_data):
        for homicide in homicide_data:
            self.state = homicide.state
            self.add_firearm_count(homicide.Weapon)
        self.state_data = sorted(self.state_data, key=lambda x: x[1], reverse=True)
        print(self.state_data)

    def add_firearm_count(self, weapon):
        if weapon in ['Rifle', 'Firearm', 'Shotgun', 'Handgun', 'Gun']:
            if self.state == 'District of Columbia':
                for sublist in self.state_data:
                    if sublist[0] == 'Washington':
                        sublist[1] += 1
                return
            for sublist in self.state_data:
                if sublist[0] == self.state:
                    sublist[1] += 1
