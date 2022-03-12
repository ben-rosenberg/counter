from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = 'counter_key'


'''
INDEX: Creates key-value pairs at 'visits' and 'real_visits' if not already
created. Increments both counters by 1, renders the template.
'''
@app.route('/')
def index() -> str:
    if not 'visits' in session:
        session['visits'] = 0
    if not 'real_visits' in session:
        session['real_visits'] = 0;
    session['visits'] += 1
    session['real_visits'] += 1
    return render_template('index.html',
        num_visits=str(session['visits']),
        num_real_visits=str(session['real_visits']))

''' DESTROY SESSION: Resets the pseuedo-counter when this URL is targeted '''
@app.route('/destroy_session')
def destroy_session():
    del session['visits']
    return redirect('/')

'''
PLUS 2: Adds 1 to the pseudo-counter when the +2 button is clicked.
I did += 1 rather than 2 because it will increment by 1 again when the index
page loads anyway. 
'''
@app.route('/plus2', methods=['POST'])
def increment_by_2():
    session['visits'] += 1
    return redirect('/')

'''
RESET: Called when the Reset button is clicked. Does not affect the 
"real" counter.
'''
@app.route('/reset_button', methods=['POST'])
def reset_button():
    return redirect('/destroy_session')

''' CUSTOM INCREMENT: Called when the form with the range slider is submitted. '''
@app.route('/custom_increment', methods=['POST'])
def custom_increment():
    form_value = request.form['custom_increment']
    session['visits'] += int(form_value) - 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)