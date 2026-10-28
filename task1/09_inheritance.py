# Section 9: Inheritance

class MobilePhone:
    def __init__(self, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = "Touch Screen"
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_a_picture(self):
        print(f"Picture taken with {self.rear_camera} rear camera")

    def specs(self):
        print(f"Screen: {self.screen_type} | Network: {self.network_type} | "
              f"Dual SIM: {self.dual_sim} | Front: {self.front_camera} | "
              f"Rear: {self.rear_camera} | RAM: {self.ram} | Storage: {self.storage}")


class Apple(MobilePhone):
    def __init__(self, model, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Apple"
        self.model = model

    def use_facetime(self, number):
        print(f"{self.brand} {self.model}: FaceTime call to {number}")


class Samsung(MobilePhone):
    def __init__(self, model, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.brand = "Samsung"
        self.model = model

    def use_dex_mode(self):
        print(f"{self.brand} {self.model}: Samsung DeX mode activated")


iphone1 = Apple("iPhone 12", "5G", False, "12MP", "12MP", "4GB", "64GB")
iphone2 = Apple("iPhone SE", "4G", False, "8MP", "12MP", "3GB", "32GB")
samsung1 = Samsung("Galaxy S21", "5G", True, "16MP", "48MP", "4GB", "64GB")
samsung2 = Samsung("Galaxy M12", "4G", True, "8MP", "32MP", "3GB", "32GB")

for phone in [iphone1, iphone2, samsung1, samsung2]:
    print(f"--- {phone.brand} {phone.model} ---")
    phone.specs()
    phone.make_call("9876543210")
    phone.receive_call("9123456780")
    phone.take_a_picture()
    print()

iphone1.use_facetime("9998887776")
samsung1.use_dex_mode()
