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
    return [song for song in songs if song['genre'].lower() == genre.lower()]

def filter_by_duration(songs, min_duration, max_duration):
    """Filters songs by duration range."""
    return [
        song for song in songs
        if min_duration <= song['duration'] <= max_duration
    ]

def display_songs(songs):
    """Displays the list of songs."""
    if not songs:
        print("No songs found.")
    else:
        print(f"{'Title':<30} {'Artist':<20} {'Genre':<15} {'Duration':<10}")
        print('-' * 75)
        for song in songs:
            print(f"{song['title']:<30} {song['artist']:<20} {song['genre']:<15} {song['duration']:<10.2f}")

def main():
    file_path = input("Enter the path to the CSV file: ")
    songs = read_csv(file_path)

    if not songs:
        return

    while True:
        print("\nFilter Options:")
        print("1. Filter by genre")
        print("2. Filter by duration")
        print("3. Display all songs")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            genre = input("Enter genre to filter by: ")
            filtered_songs = filter_by_genre(songs, genre)
            display_songs(filtered_songs)
        elif choice == 2:
            try:
                min_duration = float(input("Enter minimum duration (in minutes): "))
                max_duration = float(input("Enter maximum duration (in minutes): "))
                filtered_songs = filter_by_duration(songs, min_duration, max_duration)
                display_songs(filtered_songs)
            except ValueError:
                print("Invalid input. Please enter valid numbers for duration.")
        elif choice == 3:
            display_songs(songs)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
