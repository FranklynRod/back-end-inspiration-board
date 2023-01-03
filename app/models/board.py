from app import db


class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)

    def to_dict(self):
        result_dict = {}
        result_dict["board_id"] = self.board_id
        result_dict["name"] = self.name
        result_dict["owner"] = self.owner


    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            owner = data_dict["owner"]
        )