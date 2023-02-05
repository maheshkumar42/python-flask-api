from marshmallow import post_load

from cashman.model.transaction import Transaction, TransactionSchema
from cashman.model.transaction_type import TransactionType


class Expense(Transaction):
    def __init__(self, description, amount):
        super().__init__(description, -abs(amount), TransactionType.EXPENSE)

    def __repr__(self):
        return f'Expense({self.description}, {self.amount})'


class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self, data, **kwargs):
        return Expense(**data)
