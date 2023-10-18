from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def message_board():
    messages = []  # 메시지를 저장할 리스트

    if request.method == 'POST':
        message = request.form['message']  # 사용자로부터 메시지 입력 받기
        messages.append(message)  # 메시지를 리스트에 추가

    return render_template('message_board.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)