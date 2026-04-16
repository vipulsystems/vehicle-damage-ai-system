class DamageReport:
    """
    Represents the 'damage_reports' table

    Table: damage_reports

    Columns:
    --------
    id: int (Primary Key)
    user_id: int (FK → users.id)
    image_path: str
    detected_parts: JSONB
    total_cost: float
    created_at: timestamp

    Example:
    --------
    {
        "id": 1,
        "user_id": 1,
        "image_path": "uploads/abc.jpg",
        "detected_parts": {
            "Bumper": 2,
            "Door": 1
        },
        "total_cost": 12000
    }
    """

    def __init__(self, id, user_id, image_path, detected_parts, total_cost, created_at=None):
        self.id = id
        self.user_id = user_id
        self.image_path = image_path
        self.detected_parts = detected_parts
        self.total_cost = total_cost
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "image_path": self.image_path,
            "detected_parts": self.detected_parts,
            "total_cost": self.total_cost,
            "created_at": str(self.created_at) if self.created_at else None
        }