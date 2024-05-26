class Engine:

    def __init__(self, power, volume):
        self.__power = power
        self.__volume = volume

    # def set_power(self, power):
    #     self.__power = power

    def get_power(self):
        return self.__power
    
    # def set_volume(self, volume):
    #     self.__volume = volume

    def get_volume(self):
        return self.__volume
    
    power = property(get_power)
    volume = property(get_volume)

class SerialCar:

    min_power = 50

    def __init__(self, make, model, engine, min_power=False):
        self.__make = make
        self.__model = model
        self.__engine = engine
        if min_power:
            self.min_power = min_power

    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def set_engine(self, engine):
        if engine.power >= self.min_power:
            self.__engine = engine
        else:
            raise ValueError("The engine is not powerful enough")
        
    def get_engine(self):
        return self.__engine
    
    make = property(get_make)
    model = property(get_model)
    engine = property(get_engine, set_engine)


en = Engine(133, 4)

sc = SerialCar("vw", "golf", en)
print(sc.engine.power)

new_en = Engine(145, 6)
sc.engine = new_en
print(sc.engine.power)


class SuperCar:

    def __init__(self, make, model, power, volume):
        self.__make = make
        self.__model = model
        self.__engine = Engine(power, volume)
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
        
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume

    make = property(get_make)
    model = property(get_model)
    power = property(get_power)
    volume = property(get_volume)


sup_c = SuperCar("ferrari", "la ferrari", 200, 12)
print(sup_c.power)


class SuperCar:


    class __SuperEngine:

        def __init__(self, power, volume):
            self.__power = power
            self.__volume = volume

        def get_power(self):
            return self.__power

        def get_volume(self):
            return self.__volume
        
        power = property(get_power)
        volume = property(get_volume)

    def __init__(self, make, model, power, volume):
        self.__make = make
        self.__model = model
        self.__engine = self.__SuperEngine(power, volume)
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
        
    def get_power(self):
        return self.__engine.power
    
    def get_volume(self):
        return self.__engine.volume

    make = property(get_make)
    model = property(get_model)
    power = property(get_power)
    volume = property(get_volume)