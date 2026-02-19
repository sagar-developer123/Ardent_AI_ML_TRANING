# ============================================================
#  Advanced Calculator — Python (User Input / Type Casting)
#  Features: +  -  *  /  %  | Mean  Median  Mode  Average
# ============================================================

def get_number(prompt):
    """Safely get a float from the user (type casting from str → float)."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Invalid input. Please enter a numeric value.\n")


def get_numbers_list():
    """Get a comma-separated list of numbers from the user."""
    while True:
        raw = input("  Enter numbers separated by commas: ")
        try:
            numbers = [float(x.strip()) for x in raw.split(",") if x.strip()]
            if not numbers:
                raise ValueError
            return numbers
        except ValueError:
            print("  ⚠  Invalid input. Example: 4, 8, 15, 16, 23, 42\n")


# ── Arithmetic Operations ──────────────────────────────────

def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def percentage(a, b):
    """What is a% of b?"""
    if b == 0:
        return "Error: Base value is zero"
    return (a / 100) * b


# ── Statistics ─────────────────────────────────────────────

def mean(numbers):
    return sum(numbers) / len(numbers)

# average is the same as mean
def average(numbers):
    return mean(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def mode(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_freq = max(frequency.values())

    if max_freq == 1:
        return "No mode (all values appear once)"

    modes = [k for k, v in frequency.items() if v == max_freq]
    return modes if len(modes) > 1 else modes[0]


# ── Display Helpers ────────────────────────────────────────

def fmt(value):
    """Format a number: show int if whole, else float."""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return round(value, 6) if isinstance(value, float) else value

def print_header():
    print("\n" + "=" * 50)
    print("        🧮  ADVANCED PYTHON CALCULATOR")
    print("=" * 50)

def print_menu():
    print("""
  ── ARITHMETIC ─────────────────────────
   1.  Addition         ( A + B )
   2.  Subtraction      ( A - B )
   3.  Multiplication   ( A × B )
   4.  Division         ( A ÷ B )
   5.  Percentage       ( A% of B )

  ── STATISTICS (list of numbers) ────────
   6.  Mean
   7.  Median
   8.  Mode
   9.  Average
  10.  All Statistics at once

  ── OTHER ───────────────────────────────
   0.  Exit
""")

def print_result(label, value):
    print(f"\n  ✅  {label} = {fmt(value)}\n")


# ── Main Program ───────────────────────────────────────────

def main():
    print_header()

    while True:
        print_menu()
        choice = input("  Select an option (0-10): ").strip()

        # ── Arithmetic ──────────────────────────────────
        if choice in ("1", "2", "3", "4", "5"):
            a = get_number("  Enter first number  (A): ")
            b = get_number("  Enter second number (B): ")

            if   choice == "1": print_result(f"{fmt(a)} + {fmt(b)}",        add(a, b))
            elif choice == "2": print_result(f"{fmt(a)} - {fmt(b)}",        subtract(a, b))
            elif choice == "3": print_result(f"{fmt(a)} × {fmt(b)}",        multiply(a, b))
            elif choice == "4": print_result(f"{fmt(a)} ÷ {fmt(b)}",        divide(a, b))
            elif choice == "5": print_result(f"{fmt(a)}% of {fmt(b)}",      percentage(a, b))

        # ── Statistics ──────────────────────────────────
        elif choice in ("6", "7", "8", "9", "10"):
            print()
            nums = get_numbers_list()

            if choice == "6":
                print_result("Mean",   mean(nums))

            elif choice == "7":
                print_result("Median", median(nums))

            elif choice == "8":
                result = mode(nums)
                if isinstance(result, list):
                    print(f"\n  ✅  Mode = {[fmt(m) for m in result]}  (multiple modes)\n")
                else:
                    print(f"\n  ✅  Mode = {fmt(result) if isinstance(result, (int, float)) else result}\n")

            elif choice == "9":
                print_result("Average", average(nums))

            elif choice == "10":
                m = mode(nums)
                mode_display = (
                    [fmt(x) for x in m] if isinstance(m, list)
                    else (fmt(m) if isinstance(m, (int, float)) else m)
                )
                print(f"""
  📊  Statistics for: {[fmt(n) for n in nums]}
  ─────────────────────────────────────
   Count   : {len(nums)}
   Sum     : {fmt(sum(nums))}
   Mean    : {fmt(mean(nums))}
   Average : {fmt(average(nums))}
   Median  : {fmt(median(nums))}
   Mode    : {mode_display}
   Min     : {fmt(min(nums))}
   Max     : {fmt(max(nums))}
   Range   : {fmt(max(nums) - min(nums))}
""")

        # ── Exit ────────────────────────────────────────
        elif choice == "0":
            print("\n  👋  Goodbye!\n")
            break

        else:
            print("\n  ⚠  Invalid option. Please choose 0–10.\n")


if __name__ == "__main__":
    main()
