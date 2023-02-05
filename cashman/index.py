from flask import Flask, jsonify, request
from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Income('pizza', 50),
    Income('Rock Concert', 100)
]


@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = list(filter(lambda t: t.type ==
                   TransactionType.INCOME, transactions))
    return jsonify(schema.dump(incomes))


@app.route('/incomes', methods=['POST'])
def add_income():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return '', 204


@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = list(filter(lambda t: t.type ==
                    TransactionType.EXPENSE, transactions))
    return jsonify(schema.dump(expenses))


@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 204


if __name__ == '__main__':
    app.run()
