# 🧮 Advanced Python Calculator

A terminal-based calculator built in Python with user input, type casting, arithmetic operations, and statistical functions — no external libraries required.

---

## Features

| Category | Operations |
|---|---|
| **Arithmetic** | Addition, Subtraction, Multiplication, Division |
| **Percentage** | Calculate X% of Y |
| **Statistics** | Mean, Median, Mode, Average |
| **Extras** | Full stats summary, input validation, zero-division guard |

---

## Getting Started

### Requirements
- Python 3.x
- No external libraries needed (uses only built-ins)

### Run

```bash
python calculator.py
```

---

## Usage

When you run the script, a menu appears with **10 options**:

```
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
```

### Arithmetic Example

```
Select an option: 4
Enter first number  (A): 100
Enter second number (B): 4

  ✅  100 ÷ 4 = 25
```

### Statistics Example

```
Select an option: 10
Enter numbers separated by commas: 4, 8, 8, 15, 16, 23

📊  Statistics for: [4, 8, 8, 15, 16, 23]
─────────────────────────────────────
 Count   : 6
 Sum     : 74
 Mean    : 12.333333
 Average : 12.333333
 Median  : 11.5
 Mode    : 8
 Min     : 4
 Max     : 23
 Range   : 19
```

---

## How It Works

### Type Casting
All user input is received as a `str` and explicitly cast to `float` using `float(input(...))`. Invalid entries are caught with `try/except` and prompt the user to re-enter.

```python
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
```

### Statistics Logic
- **Mean / Average** — sum of all values divided by count
- **Median** — middle value of a sorted list; average of two middle values for even-length lists
- **Mode** — most frequently occurring value(s); returns "No mode" if all values are unique

### Input Guards
- Division by zero returns a friendly error message instead of crashing
- Percentage base-zero is also caught
- Empty or non-numeric list entries are rejected with a re-prompt

---

## File Structure

```
calculator.py   # Main script — all logic in one file
README.md       # This file
```

---

## License

MIT — free to use, modify, and distribute.

