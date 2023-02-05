import datetime as dt

from marshmallow import Schema, fields


class Transaction:
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type
        self.date = dt.datetime.now()

    def __repr__(self):
        return f'Transaction({self.description}, {self.amount}, {self.type})'


class TransactionSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    type = fields.Str()
    created_at = fields.DateTime()
