# Watt_Trees_Abbrev_AC50002
References:
ChatGPT
Prompts:
How to make a score system with criteria for each letter - used in calculate score function
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
How to find out the smallest score for each abbreviation - Used in smallest score function
for fileLine, abbr_list in abbrList:
            if abbr_list: # Check if the abbreviation list is not empty
            # Find the abbreviation with the smallest score for the current phrase
                min_score_abbr = min(abbr_list, key=lambda x: calculateScore(x, fileLine))
                print(f"{fileLine}\n{min_score_abbr}")  # Display the phrase and its smallest score abbreviation
                file.write(f"{fileLine}\n{min_score_abbr}")
            else:
                print(f"{fileLine}: \n")  # Display the phrase indicating no abbreviation available
                file.write(f"{fileLine}:\n")
What to do to find out letters for three-letter abbreviations in a list. - Used in create abbreviation function for the nested loop
for i in range(1, len(phrase) - 1):
            for j in range(i + 1, len(phrase)):
                abbreviation = first_letter + phrase[i] + phrase[j]
                abbreviations.add(abbreviation)
