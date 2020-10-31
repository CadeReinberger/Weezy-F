import quizdb
import blueplatedb
import speaker
from qbutil import interleave
from configs import (between_question_time,
                     college_game_default_num_questions,
                     study_game_default_num_questions, 
                     bonus_game_default_num_questions,
                     cat_game_default_num_questions)
import time

def run_random_single_question():
    q = quizdb.get_random_question()
    speaker.speak_question(q)
    
class naqt_game:
    def __init__(self, qs):
        self.qs = qs
    
    def __str__(self):
        #this is just a diagnostic, so I'm not gonna make it good
        res = ''
        for i, q in enumerate(self.qs):
            res += '-' * 80 + '\n'
            res += 'QUESTION ' + str(i + 1) + '\n'
            res += '-' * 80 + '\n'
            res += 'Q: ' + q.q + '\n'
            res += '-' * 80 + '\n'
            res += 'A: ' + q.a + '\n'
            res += '-' * 80 + '\n\n\n'
        return res
    
    def playthrough(self):
        for q in self.qs:
            speaker.speak_question(q)
            time.sleep(between_question_time)
            
    def college_game(num_qs = college_game_default_num_questions):
        tossups = quizdb.get_random_tossups(num_qs)
        bonuses = quizdb.get_random_bonuses(3 * num_qs)
        return naqt_game(interleave([tossups, bonuses]))
    
    def study_game(num_qs = study_game_default_num_questions):
        tossups = quizdb.get_random_tossups(num_qs)
        facts_one = blueplatedb.get_random_facts(num_qs)
        bonuses = quizdb.get_random_bonuses(3 * num_qs)
        facts_two = blueplatedb.get_random_facts(num_qs)
        return naqt_game(interleave([tossups, facts_one, bonuses, facts_two]))
    
    def bonus_game(num_qs = bonus_game_default_num_questions):
        return naqt_game(quizdb.get_random_bonuses(num_qs))
    
    def cat_game(cat = None, num_qs = cat_game_default_num_questions):
        cats = [cat] if not cat is None else blueplatedb.cats
        qs = []
        for cat in cats:
            n =  num_qs//len(cats)
            qs.extend(blueplatedb.get_random_facts_by_cat(cat,n))
        return naqt_game(qs)
        
def run_college_game():
    naqt_game.college_game().playthrough()

def run_study_game():
    naqt_game.study_game().playthrough()     
    
def run_bonus_game():
    naqt_game.bonus_game().playthrough()
    
def run_cat_game():
    naqt_game.cat_game().playthrough()
    
naqt_game.college_game(100).playthrough()
        