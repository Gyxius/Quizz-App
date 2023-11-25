import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import *

"""
For better tests
https://realpython.com/python-testing/
"""
def test_quizz_apps():
    print("Testing quizz class")
    quiz = QuizzApp()
    data = pd.read_csv('data/data.csv')
    data['user_answer'] = 'test'
    assert quiz.data.shape == data.shape # Should be True
    return quiz

def test_pages(root):
    print("Testing Pages Object")
    page = Pages(root)
    print("Testing OpenPage")
    page.openpage()
    print("Testing HomePage")
    page.homepage()
    print("Testing Topic setting")
    page.set_topic("professional")
    print("Testing quizz method")
    page.quizz()
    print("Testing Ending Page")
    page.end_page()
    print("Testing Question Page")
    page.question_page(1)

if __name__ == "__main__":
    quiz = test_quizz_apps()
    test_pages(quiz)
    print("Everything passed")