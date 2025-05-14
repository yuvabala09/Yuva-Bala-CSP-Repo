import random
import datetime

# ------------------------ Requirement #3 - Part i -----------------------------
# ❗This shows how data is stored in a list (managing complexity)
MOOD_COLOR_MAP = {
    "happy": ["#FFD700", "#FFFACD", "#FFE135", "#FFDD44"],
    "calm": ["#A3D5D3", "#E0F7FA", "#C2E9FB", "#B2DFDB"],
    "sad": ["#5D737E", "#6C757D", "#708090", "#34495E"],
    "angry": ["#FF6F61", "#D7263D", "#C72C48", "#E63946"],
    "energetic": ["#FF9F1C", "#FFBF00", "#F77F00", "#FF6B6B"],
    "creative": ["#9B5DE5", "#F15BB5", "#00BBF9", "#00F5D4"],
    "lonely": ["#3D3B8E", "#2C2C54", "#3A0CA3", "#1D1E2C"],
    "romantic": ["#FFC0CB", "#FF69B4", "#DB7093", "#FFB6C1"]
}

HEX_TO_TERMINAL = {
    "#FFD700": 226, "#FFFACD": 229, "#FFE135": 220, "#FFDD44": 214,
    "#A3D5D3": 159, "#E0F7FA": 195, "#C2E9FB": 153, "#B2DFDB": 122,
    "#5D737E": 67, "#6C757D": 244, "#708090": 103, "#34495E": 60,
    "#FF6F61": 203, "#D7263D": 160, "#C72C48": 161, "#E63946": 196,
    "#FF9F1C": 214, "#FFBF00": 220, "#F77F00": 202, "#FF6B6B": 203,
    "#9B5DE5": 135, "#F15BB5": 200, "#00BBF9": 45, "#00F5D4": 50,
    "#3D3B8E": 61, "#2C2C54": 60, "#3A0CA3": 56, "#1D1E2C": 235,
    "#FFC0CB": 218, "#FF69B4": 205, "#DB7093": 168, "#FFB6C1": 217
}

# ------------------ Requirement #1: Student-Developed Procedure ------------------
# This function defines a named procedure using parameters that affect output.
# It uses sequencing (steps), selection (if), and iteration (for).
def generate_palette(mood_keywords: list) -> list:
    """Generate a color palette based on selected mood keywords."""
    palette = []
    for mood in mood_keywords:  # <-- iteration
        if mood in MOOD_COLOR_MAP:  # <-- selection
            palette.extend(random.sample(MOOD_COLOR_MAP[mood], 2))  # <-- sequencing
    return palette[:6]  # Max 6 colors in palette

# ---------------- Requirement #2: Calling the Student Procedure ------------------
# This is where the above procedure is called inside the main logic.
def create_mood_board():
    print("\n💭 Enter 1 to 3 moods (comma-separated) like: happy, sad, calm")
    mood_input = input("> ").lower()
    keywords = [word.strip() for word in mood_input.split(",") if word.strip() in MOOD_COLOR_MAP]
    
    if not keywords:
        print("⚠️  Invalid moods. Please try again.")
        return

    # 🔁 Call the procedure with keywords as argument
    palette = generate_palette(keywords)

    print("\n🎨 Your Mood Board:")
    display_color_blocks(palette)

    save_option = input("\n💾 Save this board to a file? (y/n) ").lower()
    if save_option == "y":
        save_palette(palette)

# ---------------- Requirement #3 - Part ii -----------------------------
# ❗ This shows how the stored list is accessed and used to display data
def display_color_blocks(palette: list):
    """Display colored blocks in terminal using hex codes."""
    for hex_color in palette:
        color_code = HEX_TO_TERMINAL.get(hex_color, 255)
        print(f"\033[48;5;{color_code}m    {hex_color}    \033[0m")

def save_palette(palette: list):
    """Save mood board to a file with timestamp."""
    filename = f"mood_board_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as file:
        for color in palette:
            file.write(f"{color}\n")
    print(f"✅ Saved to {filename}")

# ---------------- Menu and Program Runner ------------------
def menu():
    while True:
        print("\n🌀 Mood Visualizer")
        print("1. Create Mood Board")
        print("2. Exit")
        choice = input("> ")
        if choice == "1":
            create_mood_board()
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
