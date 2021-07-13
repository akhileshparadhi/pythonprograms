class vehicle:
    def __init__(self,company,model_name,color,engine_power):
        self.company=company
        self.color=color
        self.engine_power=engine_power
        self.model_name=model_name

    def __str__(self):
        return f"This car of {self.company} with model no. {self.model_name} has {self.color} with {self.engine_power} power"


class car1(vehicle):
    def __init__(self, company, model_name, color, engine_power):
        super().__init__(company, model_name, color, engine_power)
        


newcar=car1("bmw","42fs0","red","7554cc")

print(newcar)
    
