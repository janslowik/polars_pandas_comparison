import csv
import random
import argparse
from faker import Faker
from faker.providers import credit_card, address

# Inicjalizacja Faker
fake = Faker()
fake.add_provider(credit_card)
fake.add_provider(address)

def generate_users(n_users):
    users = {}
    for user_id in range(1, n_users + 1):
        country = fake.country()
        users[user_id] = {
            "user_id": user_id,
            "home_country": country
        }
    return users

def load_or_generate_merchants(n_merchants):
    return [fake.company() for _ in range(n_merchants)]

def generate_transaction(user, fraud_probability, shared_merchants, reuse_ratio):
    is_fraud = random.random() < fraud_probability
    transaction_country = fake.country() if is_fraud else user['home_country']

    # Merchant: losowy z listy lub nowy
    if random.random() < reuse_ratio and shared_merchants:
        merchant = random.choice(shared_merchants)
    else:
        merchant = fake.company()

    return {
        "user_id": user["user_id"],
        "timestamp": fake.date_time_this_year().isoformat(),
        "amount": round(random.uniform(5.0, 5000.0), 2),
        "currency": "USD",
        "card_number": fake.credit_card_number(card_type=None),
        "merchant": merchant,
        "country": transaction_country,
        "is_fraud": is_fraud
    }

def estimate_row_size(shared_merchants, reuse_ratio):
    sample = generate_transaction(
        {"user_id": 1, "home_country": "United States"},
        fraud_probability=0.1,
        shared_merchants=shared_merchants,
        reuse_ratio=reuse_ratio
    )
    csv_line = ','.join(str(val) for val in sample.values()) + '\n'
    return len(csv_line)

def generate_data_streaming_csv(output_file, num_rows=None, est_size_gb=None,
                                fraud_probability=0.01, n_users=1000,
                                n_shared_merchants=100, reuse_ratio=0.8):

    shared_merchants = load_or_generate_merchants(n_shared_merchants)

    if est_size_gb is not None:
        row_size = estimate_row_size(shared_merchants, reuse_ratio)
        num_rows = int((est_size_gb * (1024 ** 3)) / row_size)
        print(f"[INFO] Szacunkowa liczba wierszy dla {est_size_gb} GB: {num_rows}")

    users = generate_users(n_users)

    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["user_id", "timestamp", "amount", "currency", "card_number", "merchant", "country", "is_fraud"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(num_rows):
            if i % 1000 == 0:
                percent = round(i*100/num_rows, 3)
                print(f"Generating row {percent}%")
            user = users[random.randint(1, n_users)]
            transaction = generate_transaction(user, fraud_probability, shared_merchants, reuse_ratio)
            writer.writerow(transaction)

    print(f"[INFO] Wygenerowano plik: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator danych transakcji kartowych.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--num_rows', type=int, help='Liczba wierszy do wygenerowania')
    group.add_argument('--est_size_gb', type=float, help='Estymowany rozmiar pliku CSV w GB')

    parser.add_argument('--output', type=str, default='transactions.csv', help='Ścieżka do pliku wyjściowego CSV')
    parser.add_argument('--fraud_prob', type=float, default=0.01, help='Prawdopodobieństwo fraudu (0.0 - 1.0)')
    parser.add_argument('--n_users', type=int, default=1000, help='Liczba unikalnych użytkowników')

    parser.add_argument('--n_merchants', type=int, default=100, help='Liczba wspólnych merchantów do powtarzania')
    parser.add_argument('--merchant_reuse_ratio', type=float, default=0.8, help='Ułamek transakcji korzystających z powtarzanych merchantów (0.0 - 1.0)')

    args = parser.parse_args()

    generate_data_streaming_csv(
        output_file=args.output,
        num_rows=args.num_rows,
        est_size_gb=args.est_size_gb,
        fraud_probability=args.fraud_prob,
        n_users=args.n_users,
        n_shared_merchants=args.n_merchants,
        reuse_ratio=args.merchant_reuse_ratio
    )