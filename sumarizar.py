import pandas as pd

# Read the CSV file
file_path = 'DetallePagos-Balanz-Bonos.csv'
df = pd.read_csv(file_path, parse_dates=['Fecha'], decimal=',')

# Convert 'Total' column to numeric, replacing ',' with '.'
df['Total'] = df['Total'].str.replace(',', '.').astype(float)

# Extract year from the 'Fecha' column
df['Year'] = df['Fecha'].dt.year

# Group by year and sum the 'Total' column
yearly_totals = df.groupby('Year')['Total'].sum().round(2)

# Print the results
print("Totals by year:")
for year, total in yearly_totals.items():
    print(f"{year}: ${total:,.2f}")

# Calculate and print the grand total
grand_total = yearly_totals.sum()
print(f"\nGrand Total: ${grand_total:,.2f}")
