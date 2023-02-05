from marshmallow import post_load

from cashman.model.transaction import Transaction, TransactionSchema
from cashman.model.transaction_type import TransactionType


class Income(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, amount, TransactionType.INCOME)

    def __repr__(self):
        return f'Income({self.description}, {self.amount})'


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)
