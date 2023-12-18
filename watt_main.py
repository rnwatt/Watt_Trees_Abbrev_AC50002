# References - ChatGPT
import re  # Importing the regular expression module to clean words

def formatLine(lineClean):
    # Keep only letters and remove other characters
    cleanWords = re.sub(r'[^a-zA-Z]', '', lineClean)
    return cleanWords.upper()  # Convert the cleaned words to uppercase

def readFile(filePath):
    try:
        with open(filePath, 'r') as file:  # Open the file in read mode
            lines = file.readlines()  # Read each line from file
            return lines
    except FileNotFoundError:
        print("File not found. Please provide the correct file path.")  # If file is not found
        return []

def createAbbr(line):
    phrase = formatLine(line)  # Clean the words in the line
    dictAbbr = {}  # Initialize an empty dictionary to store abbreviations

    if len(phrase) >= 3:  # Check if length of the phrase is greater or equal to 3 so an abbreviation can be made
        abbreviations = set()  # Initialize an empty set to store abbreviations for uniqueness
        first_letter = phrase[0]  # Get the first letter of the phrase

        # Create abbreviations by using the first letter and then switching through different letters throughout the word
        for i in range(1, len(phrase) - 1):
            for j in range(i + 1, len(phrase)):
                abbreviation = first_letter + phrase[i] + phrase[j]
                abbreviations.add(abbreviation)  # Add the generated abbreviation to the set

        # Filter and store three letter abbreviations
        threeLetterAbbr = []
        for abbr in abbreviations:
            if len(abbr) == 3:
                threeLetterAbbr.append(abbr)

        # Store the list of 3-letter abbreviations for the line in the dictionary
        dictAbbr[line.strip()] = threeLetterAbbr

    return dictAbbr  # Return the dictionary containing abbreviations for the line

#GPT prompt used here
def calculateScore(abbreviation, fileLine):
    # Get the first and last letters of the phrase
    firstLetter = fileLine[0]
    lastLetter = fileLine[-1]


    score = 0

    # Loop through each letter in the abbreviation
    for i, letter in enumerate(abbreviation):
        # Check if the letter is at index 0 (first position) and matches the first letter of the phrase
        if i == 0 and letter == firstLetter:
            score += 0  # If the condition is met, add 0 to the score (no points)

        # Check if the letter is at index 2 (third position) and matches the last letter of the phrase
        elif i == 2 and letter == lastLetter:
            # If the last letter is 'E', add 20 to the score; otherwise, add 5
            if letter == 'E':
                score += 20
            else:
                score += 5

        else:
            # If the letter doesn't meet the above conditions, assign point values based on position and letter
            positionValues = {'2': 1, '3': 2}  # Define position-based values
            letterScores = {'Q': 1, 'Z': 1, 'J': 3, 'X': 3, 'K': 6, 'F': 7, 'H': 7, 'V': 7, 'W': 7, 'Y': 7,
                             'B': 8, 'C': 8, 'M': 8, 'P': 8, 'D': 9, 'G': 9, 'L': 15, 'N': 15, 'R': 15, 'S': 15,
                             'T': 15, 'O': 20, 'U': 20, 'A': 25, 'I': 25, 'E': 35}  # Define letter-based values

            # Get the position value for the current letter in the abbreviation
            positionValue = positionValues.get(str(i + 1), 3)

            # Get the letter score based on the letter in the abbreviation
            letterScore = letterScores.get(letter, 0)

            # Add the position value and letter score to the total score
            score += positionValue + letterScore

    return score  # Return the final calculated score


def removeDupes(listAbbr):
    # Extract all abbreviations from the list of phrases and their abbreviations
    allAbbr = [abbr for _, abbr_list in listAbbr for abbr in abbr_list]

    # Find duplicates by creating a set of abbreviations occurring more than once
    duplicates = {abbr for abbr in allAbbr if allAbbr.count(abbr) > 1}

    # Remove duplicates from the abbreviations list for each phrase
    for idx, (phrase, abbreviationList) in enumerate(listAbbr):
        # Remove duplicates from the current phrase's abbreviation list
        listAbbr[idx] = (phrase, [abbr for abbr in abbreviationList if abbr not in duplicates])

    return listAbbr  # Return the list with duplicates removed

#ChatGPT
def smallestScore(abbrList, output_file):
    with open(output_file, 'w') as file:
        # Iterate through each phrase and its abbreviation list
        for fileLine, abbr_list in abbrList:
            if abbr_list: # Check if the abbreviation list is not empty
            # Find the abbreviation with the smallest score for the current phrase
                min_score_abbr = min(abbr_list, key=lambda x: calculateScore(x, fileLine))
                print(f"{fileLine}\n{min_score_abbr}")  # Display the phrase and its smallest score abbreviation
                file.write(f"{fileLine}\n{min_score_abbr}")
            else:
                print(f"{fileLine}: \n")  # Display the phrase indicating no abbreviation available
                file.write(f"{fileLine}:\n")
def main():
    while True:
        print("1. Input a text file")
        print("2. Test calculate_score")
        print("3. End")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Please provide the file name: ")
            file_path = f'{file_name}'

            lines = readFile(file_path)

            # Generating abbreviations for each line in the file
            listAbbr = []
            for line in lines:
                abbreviations = createAbbr(line)
                if abbreviations:
                    listAbbr.append((line.strip(), abbreviations[line.strip()]))

            # Remove duplicates across phrases
            listAbbr = removeDupes(listAbbr)

            # Displaying the abbreviation with the smallest score
            smallestScore(listAbbr, 'watt_trees_abbrevs.txt')


        elif choice == '2':

            print("Abbreviation Score")
            print("VIM in Vim")
            print(calculateScore("VIM", "Vim"))
            print("STR in Stormtrooper")
            print(calculateScore("STR", "Stormtrooper"))
            print("ABC in Alphabetical")
            print(calculateScore("ABC", "Alphabetical"))
            print("SDM in Spider-man")
            print(calculateScore("SDM", "Spider-man"))
            print("TWE in The World's End")
            print(calculateScore("TWE", "The World's End"))
            print("ALD in Alder")
            print(calculateScore("ALD", "Alder"))

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()

