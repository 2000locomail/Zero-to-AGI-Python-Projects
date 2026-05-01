principal = float(input("Enter your Principal: "))
rate = float(input("Enter your Rate(in per): "))
time = float(input("Enter your Time (in years): "))
si = (principal*rate*time)/100
total_amo = principal+si
print(f"Simple Interest (SI): {si:.2f}")
print(f"Total Amount (P + SI): {total_amo:.2f}")