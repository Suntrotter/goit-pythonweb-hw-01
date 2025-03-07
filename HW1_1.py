from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str):
        self.make: str = make
        self.model: str = model
        self.region_spec: str = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region_spec}): Двигун запущено.")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.region_spec}): Мотор заведено.")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Використання фабрики для США
us_factory = USVehicleFactory()
car1 = us_factory.create_car("Ford", "Mustang")
car1.start_engine()

motorcycle1 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
motorcycle1.start_engine()

# Використання фабрики для ЄС
eu_factory = EUVehicleFactory()
car2 = eu_factory.create_car("BMW", "3 Series")
car2.start_engine()

motorcycle2 = eu_factory.create_motorcycle("Ducati", "Panigale")
motorcycle2.start_engine()
