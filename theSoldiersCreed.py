
def main():
    originalCreed = "I am an American Soldier\nI am a warrior and a member of a team\nI serve the people of the United States and live the Army Values\nI will always place the mission first\nI will never accept defeat\nI will never quit\nI will never leave a fallen comrade\nI am disciplined physically and mentally tough trained and proficient in my warrior tasks and drills\nI always maintain my arms my equipment and myself\nI am an expert and I am a professional\nI stand ready to deploy engage and destroy the enemies of the United States of America in close combat\nI am a guardian of freedom and the American way of life\nI am an American Soldier\n"
    creed = originalCreed.lower()
    correct = False
    nextLine = creed.split('\n')

    for line in nextLine:
        while correct == False:
            answer = input("Enter the next line of the Soldier's Creed: ")
            answer = answer.lower()
            if answer == line:
                correct = True
                print("Correct!")
            else:
                print("Incorrect. Try again.")
        correct = False

if __name__ == "__main__":
    main()