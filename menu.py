import inquirer

questions = [
    inquirer.List('menu',
                  message="Choose from the menu below",
                  choices=['Play', 'Help', 'About', 'High Scores', 'Exit'],
                  )]

answers = inquirer.prompt(questions)
print(answers["menu"])
