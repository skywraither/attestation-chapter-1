import json
import datetime

# Load existing notes from file
def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save notes to file
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

# Add a new note
def add_note():
    title = input("Enter the note title: ")
    body = input("Enter the note body: ")
    timestamp = datetime.datetime.now().isoformat()

    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes(notes)
    print("Note added successfully.")

# Display all notes
def display_notes():
    if not notes:
        print("No notes found.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Timestamp: {note['timestamp']}")
            print()

# Edit a note
def edit_note():
    note_id = int(input("Enter the ID of the note to edit: "))
    found_notes = [note for note in notes if note['id'] == note_id]

    if not found_notes:
        print("Note not found.")
    else:
        note = found_notes[0]
        print("Note found:")
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Timestamp: {note['timestamp']}")
        print()

        new_title = input("Enter the new title (leave blank to keep the same): ")
        new_body = input("Enter the new body (leave blank to keep the same): ")

        if new_title:
            note['title'] = new_title
        if new_body:
            note['body'] = new_body

        save_notes(notes)
        print("Note edited successfully.")

# Delete a note
def delete_note():
    note_id = int(input("Enter the ID of the note to delete: "))
    found_notes = [note for note in notes if note['id'] == note_id]

    if not found_notes:
        print("Note not found.")
    else:
        note = found_notes[0]
        notes.remove(note)
        save_notes(notes)
        print("Note deleted successfully.")

# Main program loop
notes = load_notes()

while True:
    print("\nMenu:")
    print("1. Add a note")
    print("2. Display all notes")
    print("3. Edit a note")
    print("4. Delete a note")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == '1':
        add_note()
    elif choice == '2':
        display_notes()
    elif choice == '3':
        edit_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")