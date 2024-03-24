import pandas as pd

#Soal 1

class MarketingDataETL():
    def extract(self):
        self.data = pd.read_csv("marketing_data.csv", sep=';')
        print("Data sebelum transform:")
        print(self.data)
        return self.data

    def transform(self):
        if 'purchase_date' in self.data.columns:
            self.data['purchase_date'] = pd.to_datetime(self.data['purchase_date'], errors='coerce')
            self.data = self.data.dropna(subset=['purchase_date'])
            print("Data setelah transform:")
            print(self.data)
            return self.data

    def store(self):
        if hasattr(self, 'data'):
            self.data.to_csv('marketing_data_processed.csv', index=False)
            print("Data stored successfully as CSV.")
        else:
            print("Tidak ada data untuk disimpan.")

data = MarketingDataETL()
data_before_transform = data.extract()
data_after_transform = data.transform()
data.store()

#Soal 2

import numpy as np
class TargetedMarketingETL(MarketingDataETL):
    def __init__(self, file_path):
        super().__init__()

    def segment_customers(self):
        if self.data is not None:
            conditions = [
                (self.data['amount_spent'] < 100),
                (self.data['amount_spent'] >= 100) & (self.data['amount_spent'] < 200),
                (self.data['amount_spent'] >= 200)
            ]
            choices = ['Low Spending', 'Medium Spending', 'High Spending']
            self.data['spending_segment'] = pd.Series(np.select(conditions, choices), index=self.data.index)
            print("Segmentasi berdasarkan pengeluaran customer:")
            print(self.data)
        else:
            print("No data to segment. Please extract data first.")

    def transform(self):
        super().transform()
        self.segment_customers()

    def store_segmented_data(self, output_file_path):
        if self.data is not None:
            try:
                self.data.to_excel(output_file_path, index=False)
                print(f"Data yang sudah di-segmentasi berhasil disimpan ke {output_file_path}")
            except Exception as e:
                print(f"Gagal menyimpan data: {e}")
        else:
            print("No data to store. Please extract and transform data first.")

# Contoh penggunaan
targeted_etl = TargetedMarketingETL("marketing_data.csv")
targeted_etl.extract()
targeted_etl.transform()
targeted_etl.store_segmented_data("segmented_data.xlsx")