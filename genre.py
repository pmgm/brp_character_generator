from improvement import Improvement
class Genre():
    """ 
A class which defines and refines a GameSystem object to work with a particular genre. It does this by storing and providing:
+ a list of supressed skills, those from the parent system which are not used
+ a list of modified skills, new skills or those with changed defaults for the genre
+ a list of available Professions and their skills
+ a list of available Races or Cultural backgrounds, with their Attributes or skills
These last two lists can also be used by the kivy (or other) presentation system to provide available options.

The parent class should probably not be instantiated; subclass for each specific genre.
    """
    def __init__(self):
        self.name = 'Default'
        self.game = 'Brp'
        self.supressed_skills = []
        self.adjusted_skills = {} # "skill_name" : "base_score"
        # list of profession names can make screens 
        self.professions = [
            {
                "name" : "Default",
                "description" : "Standard profession",
                "base_skill_scores" :
                # skills should be available in the parent game
                # these are just an example
                {
                    'Stealth': 0,
                    'Hide': 0,
                    'Fine Manipulation': 0,
                    'Dodge': 0,
                    'Fast Talk': 0,
                    'Appraise': 0,
                    'Listen': 0,
                    'Spot': 0,
                    'Brawl': 0,
                    'Melee Weapon': 0
                }
            }
        ]
        self.races = [
            {
                "name" : "Human",
                "stats" : {
                    'STR': '3d6',
                    'CON': '3d6',
                    'SIZ': '2d6+6',
                    'INT': '2d6+6',
                    'POW': '3d6',
                    'DEX': '3d6',
                    'APP': '3d6',
                    'EDU': '3d6'
                },
                "skills" : Improvement({})
            }
        ]
    
