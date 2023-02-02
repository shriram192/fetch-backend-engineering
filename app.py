import sys
import csv
from datetime import datetime


def customer_spend_points():
    points_total = int(sys.argv[1])
    print('Number of Points to Spend: ', points_total)

    with open('transactions.csv', 'r') as file:
        my_reader = csv.reader(file, delimiter=',')

        transactions = []
        for row in my_reader:
            transactions.append(row)
        transactions.pop(0)

        #print('Transactions: ',transactions)

        date_format = '%Y-%m-%dT%H:%M:%SZ'

        sorted_transactions = sorted(transactions, key=lambda x: datetime.strptime(x[2], date_format))
        print('Sorted Transactions: ', sorted_transactions)

        while points_total >= 0:
            oldest_transaction = sorted_transactions.pop(0)

            if (int(oldest_transaction[1]) == 0):
                sorted_transactions.append(oldest_transaction)
                continue;

            remaining = -1

            if points_total - int(oldest_transaction[1]) >= 0:
                points_total -= int(oldest_transaction[1])
                remaining = 0
            else:
                points_total -= int(oldest_transaction[1])
                remaining = abs(points_total)

            print('Total: ', points_total)
            print('Remaining: ',remaining)
            
            oldest_transaction[1] = str(remaining)
            sorted_transactions.append(oldest_transaction)

        vendor_points_remaining = {}

        for trans in sorted_transactions:
            if trans[0] in vendor_points_remaining:
                vendor_points_remaining[trans[0]] += int(trans[1])
            else:
                vendor_points_remaining[trans[0]] = int(trans[1])

        return vendor_points_remaining



if __name__ == '__main__':
    result = customer_spend_points()
    print(result)