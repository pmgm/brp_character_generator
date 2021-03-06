#
# Import IO as workaround for "file" not existing in Python3
#
from io import FileIO as file

#
# Import Kivy Modules
#
import kivy
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ListProperty

#
# Import ReportLab Modules
#
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm, mm, inch, pica
from reportlab.platypus import Paragraph
from reportlab.lib.utils import simpleSplit

#
# Import PyPDF2 Modules
#
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

#
# Import custom modules
#
from brp_stats import *
#from brp_skills import *
from brp_professions_fantasy import *
from brp_professions_scifi import *
from brp_professions_cyber import *
from brp_professions_wildwest import *
from brp_professions_horror import *
from brp_races_fantasy import *
from brp_races_scifi import *
from brp_races_cyber import *
from brp_races_wildwest import *
from brp_races_horror import *
from dice_roller import *

#
# Import KV file
#

Builder.load_file("gui_brp_scroll.kv")

class WelcomeScreen(Screen):
    pass

class SelectSystem(Screen):

    game = StringProperty()
    ruleset = StringProperty()

    def brp_system(self,*args):
        game = 'Basic Roleplaying'
        sm.get_screen("character_sheet").printrules(game)

    def mw_system(self,*args):
        game='Magic World'
        sm.get_screen("character_sheet").printrules(game)

    def mi_system(self,*args):
        game='Mythras Imperative'
        sm.get_screen("character_sheet").printrules(game)

    def coc_system(self,*args):
        game='Call of Cthulhu'
        sm.get_screen("character_sheet").printrules(game)

class SelectGenre(Screen):

    genre = StringProperty()

    def choose_race_screen(self):
        race_display = self.genre
        if race_display == 'fantasy':
            sm.get_screen("character_sheet").printgenre('Fantasy')
            sm.current = 'race_fantasy'
        if race_display == 'scifi':
            sm.get_screen("character_sheet").printgenre('Scifi')
            sm.current = 'race_scifi'
        if race_display == 'cyberpunk':
            sm.get_screen("character_sheet").printgenre('Cyberpunk')
            sm.current = 'race_cyberpunk'
        if race_display == 'wildwest':
            sm.get_screen("character_sheet").printgenre('Wildwest')
            sm.current = 'race_wildwest'
        if race_display == 'horror':
            sm.get_screen("character_sheet").printgenre('Horror')
            sm.current = 'race_horror'

class SelectRaceFantasy(Screen):

    def fantasy_human(self,a,b):
        if b==True:
            race="Human"
            statblock = fantasy_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def fantasy_elf(self,a,b):
        if b==True:
            race="Elf"
            statblock = fantasy_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def fantasy_dwarf(self,a,b):
        if b==True:
            race="Dwarf"
            statblock = fantasy_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def fantasy_orc(self,a,b):
        if b==True:
            race="Orc"
            statblock = fantasy_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def fantasy_goblin(self,a,b):
        if b==True:
            race="Goblin"
            statblock = fantasy_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def fantasy_halfling(self,a,b):
        if b==True:
            race="Halfling"
            statblock = fantasy_halfling_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

class SelectRaceSciFi(Screen):

    def scifi_human(self,a,b):
        if b==True:
            race="Human"
            statblock = scifi_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_eldar(self,a,b):
        if b==True:
            race="Eldar"
            statblock = scifi_eldar_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_squat(self,a,b):
        if b==True:
            race="Squat"
            statblock = scifi_squat_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_ork(self,a,b):
        if b==True:
            race="Ork"
            statblock = scifi_ork_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_gretchin(self,a,b):
        if b==True:
            race="Gretchin"
            statblock = scifi_gretchin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_wookiee(self,a,b):
        if b==True:
            race="Wookiee"
            statblock = scifi_wookiee_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_grey(self,a,b):
        if b==True:
            race="Grey"
            statblock = scifi_grey_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_gungan(self,a,b):
        if b==True:
            race="Gungan"
            statblock = scifi_gungan_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def scifi_zabrak(self,a,b):
        if b==True:
            race="Zabrak"
            statblock = scifi_zabrak_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

class SelectRaceWildWest(Screen):

    def wildwest_human(self,a,b):
        if b==True:
            race="Human"
            statblock = wildwest_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def wildwest_amerindian(self,a,b):
        if b==True:
            race="American Indian"
            statblock = wildwest_amerindian_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def wildwest_brawn(self,a,b):
        if b==True:
            race="Brawn Over Brains"
            statblock = wildwest_brawn_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def wildwest_brains(self,a,b):
        if b==True:
            race="Brains Over Brawn"
            statblock = wildwest_brains_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def wildwest_lowlife(self,a,b):
        if b==True:
            race="Lowlife Scum"
            statblock = wildwest_lowlife_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)


class SelectRaceHorror(Screen):

    def horror_human(self,a,b):
        if b==True:
            race="Horror Human"
            statblock = horror_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def horror_ghoul(self,a,b):
        if b==True:
            race="Ghoul"
            statblock = horror_ghoul_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def horror_vampire(self,a,b):
        if b==True:
            race="Vampire"
            statblock = horror_vampire_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def horror_brawn(self,a,b):
        if b==True:
            race="Brawn Over Brains"
            statblock = horror_brawn_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def horror_brains(self,a,b):
        if b==True:
            race="Brains Over Brawn"
            statblock = horror_brains_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def horror_lowlife(self,a,b):
        if b==True:
            race="Lowlife Scum"
            statblock = horror_lowlife_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)


class SelectRaceCyberpunk(Screen):

    def cyber_human(self,a,b):
        if b==True:
            race="Cyber Human"
            statblock = cyber_human_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def cyber_elf(self,a,b):
        if b==True:
            race="Cyber Elf"
            statblock = cyber_elf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def cyber_dwarf(self,a,b):
        if b==True:
            race="Cyber Dwarf"
            statblock = cyber_dwarf_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def cyber_orc(self,a,b):
        if b==True:
            race="Cyber Orc"
            statblock = cyber_orc_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)

    def cyber_goblin(self,a,b):
        if b==True:
            race="Cyber Goblin"
            statblock = cyber_goblin_stats()
            characteristic_rolls = rolls(statblock)
            skill_category_modifiers = scm(statblock)
            skill_category_bonuses = scb(statblock)
            sm.get_screen("character_sheet").printcharacter(statblock,characteristic_rolls,skill_category_modifiers,skill_category_bonuses)
            sm.get_screen("character_sheet").printrace(race)



class SelectProfessionFantasy(Screen):

    def warrior(self,*args):
        prof = 'Warrior'
        skills_list = fantasy_warrior_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def rogue(self,*args):
        prof = 'Rogue'
        skills_list = fantasy_rogue_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def wizard(self,*args):
        prof = 'Wizard'
        skills_list = fantasy_wizard_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def priest(self,*args):
        prof = 'Priest'
        skills_list = fantasy_priest_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def explorer(self,*args):
        prof = 'Explorer'
        skills_list = fantasy_explorer_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def noble(self,*args):
        prof = 'Noble'
        skills_list = fantasy_noble_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def assassin(self,*args):
        prof = 'Assassin'
        skills_list = fantasy_assassin_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def beggar(self,*args):
        prof = 'Beggar'
        skills_list = fantasy_beggar_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def artisan(self,*args):
        prof = 'Artisan'
        skills_list = fantasy_artisan_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def merchant(self,*args):
        prof = 'Merchant'
        skills_list = fantasy_merchant_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def shaman(self,*args):
        prof = 'Shaman'
        skills_list = fantasy_shaman_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def hunter(self,*args):
        prof = 'Hunter'
        skills_list = fantasy_hunter_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionSciFi(Screen):

    def warrior(self,*args):
        prof = 'Warrior'
        skills_list = scifi_warrior_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def psyker(self,*args):
        prof = 'Psyker'
        skills_list = scifi_psyker_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def jedi(self,*args):
        prof = 'Jedi'
        skills_list = scifi_jedi_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def rogue(self,*args):
        prof = 'Rogue'
        skills_list = scifi_rogue_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def smuggler(self,*args):
        prof = 'Smuggler'
        skills_list = scifi_smuggler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def noble(self,*args):
        prof = 'Noble'
        skills_list = scifi_noble_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def technician(self,*args):
        prof = 'Technician'
        skills_list = scifi_technician_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def agent(self,*args):
        prof = 'Agent'
        skills_list = scifi_agent_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def gambler(self,*args):
        prof = 'Gambler'
        skills_list = scifi_gambler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def trader(self,*args):
        prof = 'Trader'
        skills_list = scifi_trader_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionCyberpunk(Screen):

    def solo(self,*args):
        prof = 'Solo'
        skills_list = cyber_solo_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def fixer(self,*args):
        prof = 'Fixer'
        skills_list = cyber_fixer_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def rocker(self,*args):
        prof = 'Rocker'
        skills_list = cyber_rocker_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def techie(self,*args):
        prof = 'Techie'
        skills_list = cyber_techie_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def corporate(self,*args):
        prof = 'Corporate'
        skills_list = cyber_corporate_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def cop(self,*args):
        prof = 'Cop'
        skills_list = cyber_cop_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def nomad(self,*args):
        prof = 'Nomad'
        skills_list = cyber_nomad_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def medtech(self,*args):
        prof = 'Medtech'
        skills_list = cyber_medtech_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def netrunner(self,*args):
        prof = 'Netrunner'
        skills_list = cyber_netrunner_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def media(self,*args):
        prof = 'Media'
        skills_list = cyber_media_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionWildWest(Screen):

    def soldier(self,*args):
        prof = 'Soldier'
        skills_list = wildwest_soldier_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def occultist(self,*args):
        prof = 'Occultist'
        skills_list = wildwest_occultist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def preacher(self,*args):
        prof = 'Preacher'
        skills_list = wildwest_preacher_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def criminal(self,*args):
        prof = 'Criminal'
        skills_list = wildwest_criminal_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def madscientist(self,*args):
        prof = 'Mad Scientist'
        skills_list = wildwest_madscientist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def gambler(self,*args):
        prof = 'Gambler'
        skills_list = wildwest_gambler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def sheriff(self,*args):
        prof = 'Sheriff'
        skills_list = wildwest_sheriff_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def doctor(self,*args):
        prof = 'Doctor'
        skills_list = wildwest_doctor_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def tribesman(self,*args):
        prof = 'Tribesman'
        skills_list = wildwest_tribesman_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class SelectProfessionHorror(Screen):

    def mercenary(self,*args):
        prof = 'Mercenary'
        skills_list = horror_mercenary_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def occultist(self,*args):
        prof = 'Occultist'
        skills_list = horror_occultist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def priest(self,*args):
        prof = 'Priest'
        skills_list = horror_priest_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def criminal(self,*args):
        prof = 'Criminal'
        skills_list = horror_criminal_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def journalist(self,*args):
        prof = 'Journalist'
        skills_list = horror_journalist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def spy(self,*args):
        prof = 'Spy'
        skills_list = horror_spy_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def scientist(self,*args):
        prof = 'Scientist'
        skills_list = horror_scientist_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def gambler(self,*args):
        prof = 'Gambler'
        skills_list = horror_gambler_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def detective(self,*args):
        prof = 'Detective'
        skills_list = horror_detective_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

    def doctor(self,*args):
        prof = 'Doctor'
        skills_list = horror_doctor_skillset()
        sm.get_screen("character_sheet").printprofession(prof)
        sm.get_screen("character_sheet").printskills(skills_list)

class CharacterSheet(Screen):

    mysb = StringProperty()
    mycr = StringProperty()
    myscm = StringProperty()
    myscb = StringProperty()
    ruleset = StringProperty()
    race = StringProperty()
    genre = StringProperty()
    profession = StringProperty()
    skills = StringProperty()

    def print_stats(self,mystats):
        stat_string = ''
        statlist = [ 'STR' , 'CON' , 'SIZ' , 'INT' , 'POW' , 'DEX' , 'APP' , 'EDU' ]
        for stat in statlist:
            ss = str(mystats[stat])
            stat_string = stat_string + stat + " [" + ss + "] "
        return stat_string


    def print_rolls(self,myrolls):
        char_string = ''
        rolls_list = [ 'Effort' , 'Stamina' , 'Idea' , 'Luck' , 'Agility' , 'Charisma' , 'Know' ]
        for r in rolls_list:
            qq = str(myrolls[r])
            char_string = char_string + r + " " + qq + "% "
        return char_string

    def print_scm(self,myscm):
        scm_string = ''
        scm_list = [ 'Physical' , 'Communication' , 'Knowledge' , 'Manipulation' , 'Perception' ]
        for s in scm_list:
            tt = str(myscm[s])
            scm_string = scm_string + s + " " + tt + "% "
        return scm_string

    def print_scb(self,myscb):
        scb_string = ''
        scb_list = [ 'Combat' , 'Communication' , 'Manipulation' , 'Mental' , 'Perception', 'Physical' ]
        for s in scb_list:
            zz = str(myscb[s])
            scb_string = scb_string + s + " " + zz + "% "
        return scb_string

    def printrules(self,rs):
        ruleset = str(rs)
        self.ruleset = str(rs)
        sm.get_screen("character_save_as_pdf").print_rules_to_pdf(self.ruleset)
        return ruleset

    def printgenre(self,rg):
        genre = str(rg)
        self.genre = str(rg)
        sm.get_screen("character_save_as_pdf").print_genre_to_pdf(self.genre)
        return genre

    def printrace(self,rc):
        race = str(rc)
        self.race = str(rc)
        sm.get_screen("character_save_as_pdf").print_race_to_pdf(self.race)
        return race

    def printprofession(self,p):
        profession = str(p)
        self.profession = str(p)
        sm.get_screen("character_save_as_pdf").print_profession_to_pdf(self.profession)
        return profession

    def printskills(self,p):
        skills_string = ''
        skills = p
        self.skills = p
        sm.get_screen("character_save_as_pdf").print_skills_to_pdf(self.skills)
        return skills

    def printcharacter(self,my_sb,my_cr,my_scm,my_scb):
        self.mysb = self.print_stats(my_sb)
        self.mycr = self.print_rolls(my_cr)
        self.myscm = self.print_scm(my_scm)
        self.myscb = self.print_scb(my_scb)
        sm.get_screen("character_save_as_pdf").print_character_to_pdf(self.mysb,self.mycr,self.myscm,self.myscb)

class CharacterSaveAsPDF(Screen):
#   pass

    character_name = TextInput()

    def print_pdf(self,charname):
        character_file = charname + ".pdf"
        output = PdfFileWriter()
        input1 = PdfFileReader(file("page1.pdf", "rb"))
        input2 = PdfFileReader(file("page2.pdf", "rb"))
        input3 = PdfFileReader(file("page3.pdf", "rb"))
        input4 = PdfFileReader(file("page4.pdf", "rb"))
        input5 = PdfFileReader(file("page5.pdf", "rb"))
        input6 = PdfFileReader(file("page6.pdf", "rb"))
        input7 = PdfFileReader(file("page7.pdf", "rb"))
        page = input1.getPage(0)
        page.mergePage(input2.getPage(0))
        page.mergePage(input3.getPage(0))
        page.mergePage(input4.getPage(0))
        page.mergePage(input5.getPage(0))
        page.mergePage(input6.getPage(0))
        page.mergePage(input7.getPage(0))
        output.addPage(page)
        outputStream = file(character_file, "wb")
        output.write(outputStream)
        outputStream.close()

    def print_rules_to_pdf(self,rs):
        ruleset = str(rs)
        self.ruleset = str(rs)
        pdf = Canvas("page1.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawCentredString(A4[0]/2,800,"Character Sheet")
        pdf.setFont("Helvetica",12)
        pdf.drawCentredString(A4[0]/2,775,self.ruleset)
        pdf.showPage()
        pdf.save()

    def print_name_to_pdf(self,n):
        charname = str(n)
        self.charname = str(n)
        pdf = Canvas("page2.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawCentredString(A4[0]/2,750,"Name")
        pdf.setFont("Helvetica",12)
        pdf.drawCentredString(A4[0]/2,725,self.charname)
        pdf.showPage()
        pdf.save()
        CharacterSaveAsPDF.print_pdf(self,self.charname)

    def print_genre_to_pdf(self,g):
        genre = str(g)
        self.genre = str(g)
        pdf = Canvas("page3.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10,700,"Genre")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10,675, self.genre)
        pdf.showPage()
        pdf.save()

    def print_race_to_pdf(self,r):
        race = str(r)
        self.race = str(r)
        pdf = Canvas("page7.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10,650,"Race")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10,625, self.race)
        pdf.showPage()
        pdf.save()

    def print_profession_to_pdf(self,p):
        profession = str(p)
        self.profession = str(p)
        pdf = Canvas("page5.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10,600,"Profession")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10,575, self.profession)
        pdf.showPage()
        pdf.save()

    def print_character_to_pdf(self,sb,cr,scm,scb):
        self.statblock = str(sb)
        self.characteristic_rolls = str(cr)
        self.sc_modifiers = str(scm)
        self.sc_bonuses = str(scb)
        pdf = Canvas("page4.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10, 550, "Characteristics")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10, 525, self.statblock)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10, 500, "Characteristic Rolls")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10, 475, self.characteristic_rolls)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10, 450, "MW Skill Category Modifiers")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10, 425, self.sc_modifiers)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10, 400, "BRP Skill Category Bonuses")
        pdf.setFont("Helvetica",12)
        pdf.drawString(10, 375, self.sc_bonuses)
        pdf.showPage()
        pdf.save()

    def print_skills_to_pdf(self,p):
        skills = str(p)
        self.skills = str(p)
        pdf = Canvas("page6.pdf")
        pdf.setFillColorRGB(0,0,0)
        pdf.setFont("Helvetica-Bold",16)
        pdf.drawString(10,350,"Skills")
        pdf.setFont("Helvetica",12)
        y = 325
        L = simpleSplit(self.skills,"Helvetica",12,500)
        print(L)
        for t in L:
            print(t)
            pdf.drawString(10,y,t)
            y -= 20
#           pdf.drawString(10,325, self.skills)
        pdf.showPage()
        pdf.save()

    def character_pdf(self,a,charname):
        CharacterSaveAsPDF.print_name_to_pdf(self,charname)

sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(SelectSystem(name='system_type'))
sm.add_widget(SelectGenre(name='genre'))
sm.add_widget(SelectRaceFantasy(name='race_fantasy'))
sm.add_widget(SelectRaceSciFi(name='race_scifi'))
sm.add_widget(SelectRaceCyberpunk(name='race_cyberpunk'))
sm.add_widget(SelectRaceWildWest(name='race_wildwest'))
sm.add_widget(SelectRaceHorror(name='race_horror'))
sm.add_widget(SelectProfessionFantasy(name='profession_fantasy'))
sm.add_widget(SelectProfessionSciFi(name='profession_scifi'))
sm.add_widget(SelectProfessionCyberpunk(name='profession_cyberpunk'))
sm.add_widget(SelectProfessionWildWest(name='profession_wildwest'))
sm.add_widget(SelectProfessionHorror(name='profession_horror'))
sm.add_widget(CharacterSheet(name='character_sheet'))
sm.add_widget(CharacterSaveAsPDF(name='character_save_as_pdf'))

class GuiBrp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    GuiBrp().run()
