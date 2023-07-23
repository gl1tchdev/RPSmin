from flask import Blueprint, render_template, url_for, request, redirect, session
from random import choice


RPS = Blueprint('rps', __name__, template_folder='templates', static_folder='static', static_url_path='/RPS')


game_result = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
game_messages = {
    'win': [
        'Good!',
        'Congratulations',
        'So lucky',
        'Well played'
    ],
    'lose': [
        'Oops!',
        ':(',
        'Never give up',
        'Nice try',
        'GG'
    ],
    'draw': ['No winners', 'Porridge mala']
}



@RPS.get('/')
def home():
    if session.get('nickname'):
        return redirect(url_for('rps.game'))
    return render_template('rps/home.html', title='Home')

@RPS.route('/game', methods=['POST', 'GET'])
def game():
    if request.method == 'GET' and not session.get('nickname'):
        return redirect(url_for('rps.home'))
    if request.method == 'POST':
        session['nickname'] = request.form.get('nickname')
        session['score'] = 0
    context = {}
    if request.args.get('choice'):
        pc_choice, _ = choice(list(game_result.items()))
        user_choice = request.args.get('choice')
        if user_choice not in game_result.keys():
            return render_template('/rps/game.html', context=context)
        context.update({'pc_choice': pc_choice})
        context.update({'user_choice': user_choice})
        if game_result[user_choice] == pc_choice:
            # User won
            context.update({'winner': 'user'})
            session['score'] += 1
            context.update({'message': choice(game_messages['win'])})
        elif user_choice == pc_choice:
            # No winners
            context.update({'message': choice(game_messages['draw'])})
        else:
            # PC won
            context.update({'winner': 'pc'})
            context.update({'message': choice(game_messages['lose'])})
            if session['score'] > 0:
                session['score'] -= 1
    return render_template('/rps/game.html', context=context)

@RPS.get('/logout')
def logout():
    session.clear()
    return redirect(url_for('rps.home'))