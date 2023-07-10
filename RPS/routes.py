import random

from flask import Flask, render_template, url_for, request, redirect, session
from random import choice


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'c7e5fb3c42586286931c3e6f348a8709356b1015c8c4cd32b575316db902'
    return app

game_result = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}


app = create_app()


@app.get('/')
def home():
    if session.get('nickname'):
        return redirect(url_for('game'))
    return render_template('/rps/index.html')

@app.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'GET' and not session.get('nickname'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        session['nickname'] = request.form.get('nickname')
        session['score'] = 0
    context = {}
    if request.args.get('choice'):
        pc_choice, _ = random.choice(list(game_result.items()))
        user_choice = request.args.get('choice')
        context.update({'pc_choice': pc_choice})
        context.update({'user_choice': user_choice})
        if game_result[user_choice] == pc_choice:
            # User won
            context.update({'winner': 'user'})
            session['score'] += 1
        elif user_choice == pc_choice:
            # No winners
            context.update({'winner': 'nobody'})
        else:
            # PC won
            context.update({'winner': 'pc'})
            if session['score'] > 0:
                session['score'] -= 1
    return render_template('/rps/game.html', context=context)

@app.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))