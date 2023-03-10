from flask import Flask, render_template
from LoginForm import LF
from AuthForm import AuthF

app = Flask(__name__)
app.config['SECRET_KEY']= '420 everyday'

@app.route('/')
def main():
    return render_template('base1.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form =LF()
    if form.validate_on_submit():
        if form.password_again.data != form.password.data:
            return render_template('register.html', title='Registration', form=form,
                                    message='Password is incorrect!')
        
        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')

        return render_template('register.html', message='Registration successfull')
    return render_template('register.html', title='Registration', form=form)

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = AuthF()
    if form.validate_on_submit():
        with open('file.txt', 'r', encoding='utf-8') as file:
            data = ' '.join(file.readlines())
        if form.email.data not in data:
            return render_template('login.html', form=form, message='You are not registered')
        else:
            for i in data.split():
                if form.email.data in i:
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', form=form, message='Success')

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()

    # with open('file.txt', 'r', encoding='utf-8') as file:
    
    #     resultData = list()
    #     for line in file.readlines():
    #         resultData.append(tuple(line.split('\n')[0].split(';')))
    #     return render_template('base.html', data=resultData)

# @app.route('/about')
# def about():
#     return render_template('about.html')


# if __name__ == '__main__':
#     app.run()



# a - режим добавления
# w - режим на запись(очищает файл)
# r - режим считывания


