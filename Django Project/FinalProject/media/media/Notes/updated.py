import datetime
import csv

# List to store meetings
meetings = []

# Function to display the menu
def display_menu():
    print("\nMeeting Scheduler")
    print("1. Add a new meeting")
    print("2. View all meetings")
    print("3. Edit a meeting")
    print("4. Delete a meeting")
    print("5. Search for a meeting")
    print("6. View meetings by date")
    print("7. View meetings in a time range")
    print("8. Set a reminder for a meeting")
    print("9. View upcoming meetings")
    print("10. View meetings by upcoming reminder")
    print("11. Exit")

# Helper function to display a meeting's details
def display_meeting(meeting):
    print(f"{meeting['title']} - {meeting['description']} on {meeting['datetime'].strftime('%Y-%m-%d %H:%M')}")
    if meeting.get('reminder'):
        print(f"Reminder set for {meeting['reminder'].strftime('%Y-%m-%d %H:%M')}")

# Function to add a new meeting
def add_meeting():
    title = input("Enter meeting title: ")
    description = input("Enter meeting description: ")
    date_str = input("Enter meeting date (YYYY-MM-DD): ")
    time_str = input("Enter meeting time (HH:MM): ")

    try:
        meeting_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        meetings.append({'title': title, 'description': description, 'datetime': meeting_datetime, 'reminder': None})
        print("Meeting added successfully.")
        
        # Automatically export meetings to CSV after adding a new meeting
        export_to_csv()
    except ValueError:
        print("Invalid date or time format.")

# Function to view all meetings
def view_meetings():
    if not meetings:
        print("No meetings scheduled.")
    else:
        for idx, meeting in enumerate(meetings, 1):
            print(f"{idx}. ", end="")  # Print meeting number
            display_meeting(meeting)

# Function to edit an existing meeting
def edit_meeting():
    if not meetings:
        print("No meetings to edit.")
        return
    view_meetings()
    try:
        idx = int(input("Enter the number of the meeting to edit: ")) - 1
        if idx < 0 or idx >= len(meetings):
            print("Invalid choice.")
            return
        title = input("Enter new title: ")
        description = input("Enter new description: ")
        date_str = input("Enter new date (YYYY-MM-DD): ")
        time_str = input("Enter new time (HH:MM): ")
        meeting_datetime = datetime.datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        meetings[idx].update({'title': title, 'description': description, 'datetime': meeting_datetime})
        print("Meeting updated successfully.")
    except ValueError:
        print("Invalid input.")

# Function to delete a meeting
def delete_meeting():
    if not meetings:
        print("No meetings to delete.")
        return
    view_meetings()
    try:
        idx = int(input("Enter the number of the meeting to delete: ")) - 1
        if idx < 0 or idx >= len(meetings):
            print("Invalid choice.")
            return
        del meetings[idx]
        print("Meeting deleted successfully.")
    except ValueError:
        print("Invalid input.")

# Function to search for a meeting
def search_meeting():
    if not meetings:
        print("No meetings to search.")
        return
    search_term = input("Enter a search term (title or description): ").lower()
    found = [meeting for meeting in meetings if search_term in meeting['title'].lower() or search_term in meeting['description'].lower()]
    if found:
        for meeting in found:
            display_meeting(meeting)
    else:
        print("No meetings found.")

# Function to view meetings by a specific date
def view_meetings_by_date():
    if not meetings:
        print("No meetings to display.")
        return
    date_str = input("Enter the date (YYYY-MM-DD): ")
    try:
        filter_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        for meeting in meetings:
            if meeting['datetime'].date() == filter_date:
                display_meeting(meeting)
    except ValueError:
        print("Invalid date format.")

# Function to view meetings in a time range
def view_meetings_in_range():
    if not meetings:
        print("No meetings to display.")
        return
    start_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
    end_str = input("Enter end time (YYYY-MM-DD HH:MM): ")
    try:
        start_time = datetime.datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end_time = datetime.datetime.strptime(end_str, "%Y-%m-%d %H:%M")
        for meeting in meetings:
            if start_time <= meeting['datetime'] <= end_time:
                display_meeting(meeting)
    except ValueError:
        print("Invalid time format.")

# Function to set a reminder for a meeting
def set_reminder():
    if not meetings:
        print("No meetings to set a reminder for.")
        return
    view_meetings()
    try:
        idx = int(input("Enter the number of the meeting to set a reminder for: ")) - 1
        if idx < 0 or idx >= len(meetings):
            print("Invalid choice.")
            return
        reminder_minutes = int(input("Enter reminder time (in minutes before the meeting): "))
        reminder_time = meetings[idx]['datetime'] - datetime.timedelta(minutes=reminder_minutes)
        meetings[idx]['reminder'] = reminder_time
        print(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M')}")
    except ValueError:
        print("Invalid input.")

# Function to view upcoming meetings
def view_upcoming_meetings():
    if not meetings:
        print("No meetings scheduled.")
        return
    now = datetime.datetime.now()
    upcoming = [meeting for meeting in meetings if meeting['datetime'] > now]
    if upcoming:
        for meeting in upcoming:
            display_meeting(meeting)
    else:
        print("No upcoming meetings.")

# Function to view meetings by upcoming reminder
def view_meetings_by_reminder():
    if not meetings:
        print("No meetings scheduled.")
        return
    now = datetime.datetime.now()
    upcoming_reminders = [meeting for meeting in meetings if meeting['reminder'] and meeting['reminder'] > now]
    if upcoming_reminders:
        for meeting in upcoming_reminders:
            display_meeting(meeting)
    else:
        print("No upcoming reminders.")

# Function to export meetings to CSV
def export_to_csv():
    if not meetings:
        print("No meetings to export.")
        return
    with open('meetings.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Description", "Date", "Time", "Reminder"])
        for meeting in meetings:
            reminder = meeting['reminder'].strftime('%Y-%m-%d %H:%M') if meeting['reminder'] else ""
            writer.writerow([meeting['title'], meeting['description'], meeting['datetime'].strftime('%Y-%m-%d'), meeting['datetime'].strftime('%H:%M'), reminder])
    print("Meetings exported to meetings.csv successfully.")

def load_meetings_from_csv():
    try:
        with open('meetings.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                meeting_datetime = datetime.datetime.strptime(f"{row['Date']} {row['Time']}", "%Y-%m-%d %H:%M")
                reminder_time = datetime.datetime.strptime(row['Reminder'], "%Y-%m-%d %H:%M") if row['Reminder'] else None
                meetings.append({
                    'title': row['Title'],
                    'description': row['Description'],
                    'datetime': meeting_datetime,
                    'reminder': reminder_time
                })
    except FileNotFoundError:
        pass


# Main function to run the program
def main():
    load_meetings_from_csv()
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ")
        if choice == "1":
            add_meeting()
        elif choice == "2":
            view_meetings()
        elif choice == "3":
            edit_meeting()
        elif choice == "4":
            delete_meeting()
        elif choice == "5":
            search_meeting()
        elif choice == "6":
            view_meetings_by_date()
        elif choice == "7":
            view_meetings_in_range()
        elif choice == "8":
            set_reminder()
        elif choice == "9":
            view_upcoming_meetings()
        elif choice == "10":
            view_meetings_by_reminder()
        elif choice == "11":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
