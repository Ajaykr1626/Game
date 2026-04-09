# Tiki Topple - Complete Hackathon Version

# Initial setup
stack = ["A", "B", "C", "D"]   # Top = index 0
positions = {t: 0 for t in stack}

players = 2
current_player = 1
turns = 0
MAX_TURNS = 20
MAX_POSITION = 5   # Track length


# ---------------- FUNCTIONS ----------------

def move_tokens(count):
    for i in range(count):
        token = stack[i]
        positions[token] += 1


def reorder_tokens(n):
    top_tokens = stack[:n]
    print("Top tokens:", top_tokens)

    new_order = input("Enter new order (space separated): ").split()

    if sorted(new_order) != sorted(top_tokens):
        print("❌ Invalid reorder!")
        return

    stack[:n] = new_order


def next_player(p):
    return (p % players) + 1


def display():
    print("\n--------------------------")
    print("Player:", current_player)
    print("Stack (Top → Bottom):", stack)
    print("Positions:", positions)
    print("--------------------------")


# ---------------- GAME LOOP ----------------

while turns < MAX_TURNS:

    # End condition 1
    if all(pos >= MAX_POSITION for pos in positions.values()):
        print("All tokens reached end!")
        break

    display()

    choice = input("1: Move | 2: Reorder → ")

    if choice == "1":
        try:
            count = int(input("Move how many (1-3): "))
            if 1 <= count <= 3:
                move_tokens(count)
            else:
                print("❌ Only 1–3 allowed")
                continue
        except:
            print("❌ Invalid input")
            continue

    elif choice == "2":
        try:
            n = int(input("Reorder how many (2-3): "))
            if 2 <= n <= 3:
                reorder_tokens(n)
            else:
                print("❌ Only 2–3 allowed")
                continue
        except:
            print("❌ Invalid input")
            continue

    else:
        print("❌ Wrong choice")
        continue

    # Next turn
    current_player = next_player(current_player)
    turns += 1


# ---------------- SCORING ----------------

print("\n===== GAME OVER =====")

# Sort tokens by position
sorted_tokens = sorted(positions.items(), key=lambda x: x[1], reverse=True)

points = {}
score = len(sorted_tokens)

for token, pos in sorted_tokens:
    points[token] = score
    score -= 1

print("\nFinal Positions:", positions)
print("Points:", points)

# Winner
winner_token = max(points, key=points.get)
print("🏆 Winning Token:", winner_token)

