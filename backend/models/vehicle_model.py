class VehiclePartPricing:
    """
    Represents the 'vehicle_parts_pricing' table

    Table: vehicle_parts_pricing

    Columns:
    --------
    id: int (Primary Key)
    brand: str
    model: str
    part: str
    price: float

    Example:
    --------
    {
        "brand": "Honda",
        "model": "City",
        "part": "Bumper",
        "price": 3000
    }
    """

    def __init__(self, id, brand, model, part, price):
        self.id = id
        self.brand = brand
        self.model = model
        self.part = part
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "part": self.part,
            "price": self.price
        }