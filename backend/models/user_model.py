class User:
    """
    Represents the 'users' table in PostgreSQL

    Table: users

    Columns:
    --------
    id: int (Primary Key)
    name: str
    email: str (Unique)
    password: str (hashed)
    vehicle_id: str
    phone_number: str
    address: str
    car_brand: str
    car_model: str
    created_at: timestamp

    Example:
    --------
    {
        "id": 1,
        "name": "Vipul",
        "email": "vipul@example.com",
        "car_brand": "Honda",
        "car_model": "City"
    }
    """

    def __init__(self, id, name, email, password=None,
                 vehicle_id=None, phone_number=None,
                 address=None, car_brand=None, car_model=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.vehicle_id = vehicle_id
        self.phone_number = phone_number
        self.address = address
        self.car_brand = car_brand
        self.car_model = car_model

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "car_brand": self.car_brand,
            "car_model": self.car_model
        }