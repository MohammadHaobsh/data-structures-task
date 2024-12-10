import csv

def read_csv(file_path):
    """Reads a CSV file and returns a list of dictionaries with song data."""
    try:
        songs = []
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure duration is stored as a float for filtering purposes
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
    return [song for song in songs if song['genre'].lower() == genre.lower()]

def filter_by_duration(songs, min_duration, max_duration):
    """Filters songs by duration range."""
    return [
        song for song in songs
        if min_duration <= song['duration'] <= max_duration
    ]

def filter_by_title(songs, title_keyword):
    """Filters songs by title containing a keyword."""
    title_keyword = title_keyword.lower()
    return [song for song in songs if title_keyword in song['title'].lower()]

def filter_by_artist(songs, artist_keyword):
    """Filters songs by artist containing a keyword."""
    artist_keyword = artist_keyword.lower()
    return [song for song in songs if artist_keyword in song['artist'].lower()]

def display_songs(songs):
    """Displays the list of songs."""
    if not songs:
        print("No songs found.")
    else:
        print(f"{'Title':<30} {'Artist':<20} {'Genre':<15} {'Duration':<10}")
        print('-' * 75)
        for song in songs:
            print(f"{song['title']:<30} {song['artist']:<20} {song['genre']:<15} {song['duration']:<10.2f}")

def get_valid_choice(prompt, valid_choices):
    """Gets a valid choice from the user."""
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_choices:
                return choice
            else:
                print(f"Invalid choice. Please choose from {valid_choices}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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

        choice = get_valid_choice("Enter your choice (1-6): ", range(1, 7))

        if choice == 1:
            genre = input("Enter genre to filter by: ").strip()
            filtered_songs = filter_by_genre(songs, genre)
            display_songs(filtered_songs)
        elif choice == 2:
            while True:
                try:
                    min_duration = float(input("Enter minimum duration (in minutes): "))
                    max_duration = float(input("Enter maximum duration (in minutes): "))
                    if min_duration > max_duration:
                        print("Minimum duration cannot be greater than maximum duration. Please try again.")
                        continue
                    filtered_songs = filter_by_duration(songs, min_duration, max_duration)
                    display_songs(filtered_songs)
                    break
                except ValueError:
                    print("Invalid input. Please enter valid numbers for duration.")
        elif choice == 3:
            title_keyword = input("Enter keyword to search in title: ").strip()
            filtered_songs = filter_by_title(songs, title_keyword)
            display_songs(filtered_songs)
        elif choice == 4:
            artist_keyword = input("Enter keyword to search in artist: ").strip()
            filtered_songs = filter_by_artist(songs, artist_keyword)
            display_songs(filtered_songs)
        elif choice == 5:
            display_songs(songs)
        elif choice == 6:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
