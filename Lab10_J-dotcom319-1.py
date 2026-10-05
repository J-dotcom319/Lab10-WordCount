"""
Lab 10: Word Count Analyzer
Author: Jeffrey Antwi
Purpose: Analyze text files and count word frequencies
Date: October 3, 2026"""

from pathlib import Path
import string


class WordAnalyzer:
    """A class to analyze word frequencies in a text file."""
    
    def __init__(self, filepath):
        """Initialize with filepath and empty frequencies dictionary."""
        self.__filepath = Path(filepath)
        self.__frequencies = {}
    
    def process_file(self):
        """Process the file and count word frequencies."""
        try:
            # Check if file exists
            if not self.__filepath.exists():
                print(f"Error: File '{self.__filepath}' not found.")
                return False
            
            # Open and read file
            with self.__filepath.open('r', encoding='utf-8') as file:
                for line in file:
                    # Remove punctuation
                    translator = str.maketrans('', '', string.punctuation)
                    clean_line = line.translate(translator)
                    
                    # Convert to lowercase
                    clean_line = clean_line.lower()
                    
                    # Split into words
                    words = clean_line.split()
                    
                    # Count frequencies
                    for word in words:
                        if word:  # Skip empty strings
                            self.__frequencies[word] = self.__frequencies.get(word, 0) + 1
            
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{self.__filepath}' not found.")
            return False
        except Exception as e:
            print(f"Error processing file: {e}")
            return False
    
    def print_report(self):
        """Print the word frequency report alphabetically."""
        if not self.__frequencies:
            print("No words to display.")
            return
        
        # Sort words alphabetically
        sorted_words = sorted(self.__frequencies.keys())
        
        print("\n--- Word Frequency Report ---")
        for word in sorted_words:
            print(f"{word} :: {self.__frequencies[word]}")
        print("-----------------------------\n")


def main():
    """Main function to run the word analyzer."""
    print("--- Word Analyzer ---")
    
    # Dictionary of files
    files = {
        "1": ("Treasure Island", "treasure_island.txt"),
        "2": ("A Princess of Mars", "princess_mars.txt"),
        "3": ("Tarzan of the Apes", "Tarzan.txt"),
        "4": ("The Count of Monte Cristo", "monte_cristo.txt")
    }
    
    while True:
        # Display menu
        print("\nPlease select a file to analyze:")
        for key, (name, _) in files.items():
            print(f"{key}. {name}")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Validate choice
        if choice == "5":
            print("Goodbye!")
            break
        
        if choice not in files:
            print("Invalid choice. Please select from 1-5.")
            input("Press Enter to return to the menu...")
            continue
        
        # Get filename
        name, filename = files[choice]
        print(f"\nProcessing '{filename}'...")
        
        # Create analyzer and process
        analyzer = WordAnalyzer(filename)
        success = analyzer.process_file()
        
        if success:
            analyzer.print_report()
        
        input("Press Enter to return to the menu...")


if __name__ == "__main__":
    main()