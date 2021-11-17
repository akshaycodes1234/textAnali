from flask import Flask, render_template, request

app = Flask(__name__)

ans = ''

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/answer', methods = ['POST', 'GET'])
def ans():
    if request.method == 'POST':
        text_input = request.form.get('texInput')
        upcase = request.form.get('ucase', 'off')
        locase = request.form.get('lcase', 'off')
        ans = ''
        if upcase == 'uc':
            ans = text_input.upper()
            return render_template('answer.html', answer = ans)
        elif locase == 'lc':
            ans = text_input.lower()
            return render_template('lanswer.html', answerl = ans)
        else: 
            return 'Problem Problem beep beep beep'
    return 'PLEASE SELECT AN EXCERCISE'
    
if __name__ == '__main__':
    app.run()