from improvement import Improvement
from genre import Genre
class GenreBrpFantasy(Genre):
    """
    Incorporate the BRP Fantasy professions and races, as a demonstration. Incorporates the information from brp_professions_fantasy and brp_races_fantasy.
    """
    def __init__(self):
        self.name = "BRP Fantasy"
        self.game = "Brp"
        self.professions = [
            {
                "name" : "Warrior",
                "description" : "",
                "base_skill_scores" :
                {
                    'First Melee Weapon': 50,
                    'Second Melee Weapon': 40,
                    'Missile Weapon': 40,
                    'Brawl': 30,
                    'Throw': 30,
                    'Grapple': 30,
                    'Parry': 30,
                    'Shield': 30,
                    'Stealth': 30,
                    'Ride': 30
                }
            },
            {
                "name" : "Rogue",
                "description" : "",
                "base_skill_scores" :
                {
                    'Stealth': 30,
                    'Hide': 50,
                    'Fine Manipulation': 50,
                    'Dodge': 50,
                    'Fast Talk': 50,
                    'Appraise': 50,
                    'Listen': 50,
                    'Spot': 50,
                    'Brawl': 50,
                    'Melee Weapon': 30
                }
            },
            {
                "name" : "Wizard",
                "description" : "",
                "base_skill_scores" :
                {
                    'Knowledge (Occult)': 20,
                    'Perform (Rituals)': 50,
                    'Language (Other)': 40,
                    'Craft (Any)': 30,
                    'Knowledge 1': 30,
                    'Knowledge 2': 30,
                    'Insight': 30,
                    'Persuade': 30,
                    'Research': 30,
                    'Literacy': 30
                }
            },
            {
                "name" : "Priest",
                "description" : "",
                "base_skill_scores" :
                {
                    'Knowledge (Religion)': 30,
                    'Perform (Rituals)': 50,
                    'Perform (Oratory)': 30,
                    'Insight': 40,
                    'Research': 40,
                    'Knowledge (History)': 40,
                    'Persuade': 40,
                    'Teach': 40,
                    'Fast Talk': 40,
                    'Literacy': 50
                }
            },
            {
                "name" : "Explorer",
                "description" : "",
                "base_skill_scores" :
                {
                    'Track': 30,
                    'Hide': 50,
                    'Spot': 30,
                    'Listen': 40,
                    'Climb': 40,
                    'Navigate': 40,
                    'Stealth': 40,
                    'Missile Weapon': 40,
                    'Melee Weapon': 40,
                    'Knowledge (Region)': 50
                }
            },
            {
                "name" : "Noble",
                "description" : "",
                "base_skill_scores" :
                {
                    'Status': 30,
                    'Etiquette': 50,
                    'Knowledge (Region)': 30,
                    'Literacy': 40,
                    'Melee Weapon': 40,
                    'Language (Other)': 40,
                    'Bargain': 40,
                    'Ride': 40,
                    'Insight': 40,
                    'Craft (Any)': 50
                }
            },
            {
                "name" : "Assassin",
                "description" : "",
                "base_skill_scores" :
                {
                    'Stealth': 30,
                    'Hide': 50,
                    'Dodge': 30,
                    'Listen': 40,
                    'Spot': 40,
                    'Missile Weapon': 40,
                    'Melee Weapon': 40,
                    'Disguise': 40,
                    'Knowledge (Poisons)': 40,
                    'Track': 50
                }
            },
            {
                "name" : "Beggar",
                "description" : "",
                "base_skill_scores" :
                {
                    'Bargain': 30,
                    'Fast Talk': 50,
                    'Hide': 30,
                    'Insight': 40,
                    'Knowledge (Local Area)': 40,
                    'Listen': 40,
                    'Persuade': 40,
                    'Sleight of Hand': 40,
                    'Spot': 40,
                    'Stealth': 50
                }
            },
            {
                "name" : "Artisan",
                "description" : "",
                "base_skill_scores" :
                {
                    'Craft (1)': 30,
                    'Craft (2)': 50,
                    'Repair (Mechanical)': 30,
                    'Appraise': 40,
                    'Art (Any)': 40,
                    'Bargain': 40,
                    'Spot': 40,
                    'Research': 40,
                    'Status': 40,
                    'Fine Manipulation': 50
                }
            },
            {
                "name" : "Merchant",
                "description" : "",
                "base_skill_scores" :
                {
                    'Bargain': 30,
                    'Appraise': 50,
                    'Fast Talk': 30,
                    'Knowledge (Accounting)': 40,
                    'Knowledge (Business)': 40,
                    'Persuade': 40,
                    'Research': 40,
                    'Status': 40,
                    'Insight': 40,
                    'Literacy': 50
                }
            },
            {
                "name" : "Shaman",
                "description" : "",
                "base_skill_scores" :
                {
                    'Perform (Rituals)': 30,
                    'Knowledge (Occult)': 50,
                    'First Aid': 30,
                    'Art (Any)': 40,
                    'Knowledge (Folklore)': 40,
                    'Insight': 40,
                    'Language (Own)': 40,
                    'Listen': 40,
                    'Craft (Any)': 40,
                    'Science (Natural History)': 50
                }
            },
            {
                "name" : "Hunter",
                "description" : "",
                "base_skill_scores" :
                {
                    'Track': 30,
                    'Hide': 50,
                    'Spot': 30,
                    'Listen': 40,
                    'Climb': 40,
                    'Navigate': 40,
                    'Stealth': 40,
                    'Missile Weapon': 40,
                    'Melee Weapon': 40,
                    'Knowledge (Region)': 50
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
            },
            {
                "name" : "Elf",
                "stats" : {
                    'STR': '2d6+2',
                    'CON': '3d6',
                    'SIZ': '2d4+4',
                    'INT': '3d6+6',
                    'POW': '2d6+6',
                    'DEX': '3d6+3',
                    'APP': '3d6',
                    'EDU': '3d6'
                },
                "skills" : Improvement({})
            },
{
                "name" : "Dwarf",
                "stats" : {
                    'STR': '4d6',
                    'CON': '1d6+12',
                    'SIZ': '1d4+4',
                    'INT': '2d6+6',
                    'POW': '3d6',
                    'DEX': '3d6',
                    'APP': '3d6',
                    'EDU': '3d6'
                },
                "skills" : Improvement({})
            },
{
                "name" : "Orc",
                "stats" : {
                    'STR': '4d6',
                    'CON': '3d6',
                    'SIZ': '2d6+2',
                    'INT': '3d6',
                    'POW': '2d6+3',
                    'DEX': '4d6',
                    'APP': '2d6',
                    'EDU': '2d6'
                },
                "skills" : Improvement({})
            },
{
                "name" : "Goblin",
                "stats" : {
                    'STR': '2d6',
                    'CON': '3d6',
                    'SIZ': '2d6',
                    'INT': '3d6',
                    'POW': '2d6+3',
                    'DEX': '4d6',
                    'APP': '2d6',
                    'EDU': '2d6'
                },
                "skills" : Improvement({})
            },
{
                "name" : "Halfling",
                "stats" : {
                    'STR': '2d6',
                    'CON': '2d6+12',
                    'SIZ': '1d3+3',
                    'INT': '3d6',
                    'POW': '2d6+3',
                    'DEX': '2d6+10',
                    'APP': '2d6',
                    'EDU': '3d6'
                },
                "skills" : Improvement({})
            }
        ]
