import os

FILE_NAME = "notes.txt"

# Create a note
def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")
    print("✅ Note added successfully!\n")

# View notes
def view_notes():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No notes found.\n")
        return
    
    with open(FILE_NAME, "r") as file:
        notes = file.readlines()
    
    if not notes:
        print("⚠️ No notes available.\n")
        return
    
    print("\n📒 Your Notes:")
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note.strip()}")
    print()

# Delete a note
def delete_note():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No notes to delete.\n")
        return
    
    with open(FILE_NAME, "r") as file:
        notes = file.readlines()
    
    view_notes()
    
    try:
        num = int(input("Enter note number to delete: "))
        if 1 <= num <= len(notes):
            notes.pop(num - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(notes)
            print("🗑️ Note deleted successfully!\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main menu
def menu():
    while True:
        print("==== Notes Saver CLI ====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Run the app
menu()