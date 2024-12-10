import csv

def read_csv(file_path):
    """Reads a CSV file and returns a list of dictionaries with song data."""
    try:
        songs = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['duration'] = float(row['duration'])
                songs.append(row)
        return songs
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except ValueError as e:
        print(f"Error processing file: {e}")
        return []

def filter_by_genre(songs, genre):
    """Filters songs by genre."""
    genre = genre.lower()  
    return [song for song in songs if genre in song['genre'].lower()]

def filter_by_duration(songs, min_duration, max_duration):
    """Filters songs by duration range."""
    return [
        song for song in songs
        if min_duration <= song['duration'] <= max_duration
    ]

def filter_by_title(songs, title):
    """Filters songs by title containing a keyword."""
    title = title.lower()  
    return [song for song in songs if title in song['title'].lower()]

def filter_by_artist(songs, artist):
    """Filters songs by artist containing a keyword."""
    artist = artist.lower()  
    return [song for song in songs if artist in song['artist'].lower()]

def display_songs(songs):
    """Displays the list of songs."""
    if not songs:
        print("No songs found.")
    else:
        print(f"{'Title':<30} {'Artist':<20} {'Genre':<15} {'Duration':<10}")
        print('-' * 75)
        for song in songs:
            print(f"{song['title']:<30} {song['artist']:<20} {song['genre']:<15} {song['duration']:<10.2f}")

def get_valid_string_input(prompt, valid_values=None):
    """Gets a valid string input for genre, title, or artist."""
    while True:
        value = input(prompt).strip()
        if value == "*":  
            return "*"
        if not value: 
            print("Input cannot be empty. Please try again or enter '*' to return.")
            continue
        if valid_values:
            matches = [val for val in valid_values if value.lower() in val.lower()]
            if matches:
                return value
            else:
                print(f"Invalid input. '{value}' is not in the list. Please try again or enter '*' to return.")
        else:
            return value

def get_valid_duration_input():
    """Gets valid input for duration (min_duration, max_duration)."""
    while True:
        try:
            min_duration = float(input("Enter minimum duration (in minutes): "))
            max_duration = float(input("Enter maximum duration (in minutes): "))
            if min_duration > max_duration:
                print("Minimum duration cannot be greater than maximum duration. Please try again.")
                continue  
            return min_duration, max_duration
        except ValueError:
            print("Invalid input. Please enter valid numbers for duration.")

def main():
    file_path = input("Enter the path to the CSV file: ")
    songs = read_csv(file_path)

    if not songs:
        return

    while True:
        print("\nFilter Options:")
        print("1. Filter by genre")
        print("2. Filter by duration")
        print("3. Filter by title")
        print("4. Filter by artist")
        print("5. Display all songs")
        print("6. Exit")

        try:
            choice = input("Enter your choice (1-6): ") 
            if choice == "1":
                genre = get_valid_string_input("Enter genre to filter by: ", valid_values=[song['genre'] for song in songs])
                if genre == "*":
                    continue
                filtered_songs = filter_by_genre(songs, genre)
                display_songs(filtered_songs)
            elif choice == "2":
                min_duration, max_duration = get_valid_duration_input()
                filtered_songs = filter_by_duration(songs, min_duration, max_duration)
                display_songs(filtered_songs)
            elif choice == "3":
                title = get_valid_string_input("Enter keyword to search in title: ", valid_values=[song['title'] for song in songs])
                if title == "*":
                    continue
                filtered_songs = filter_by_title(songs, title)
                display_songs(filtered_songs)
            elif choice == "4":
                artist = get_valid_string_input("Enter keyword to search in artist: ", valid_values=[song['artist'] for song in songs])
                if artist == "*":
                    continue
                filtered_songs = filter_by_artist(songs, artist)
                display_songs(filtered_songs)
            elif choice == "5":
                display_songs(songs)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 6.")

if __name__ == "__main__":
    main()
