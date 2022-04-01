from flask import Flask, request, render_template
import glob
import random
import sudoku


def check_data():
    with open("data\\sudoku.data") as f:
        lines = f.readlines()
    if len(lines) <= 0:
        return False
    return True


def GetRandomData():
    with open("data\\sudoku.data") as f:
        lines = f.readlines()
    return lines[random.randint(0, len(lines)-1)]


sudoku_web = Flask(__name__)


@sudoku_web.route("/")
def index():
    print("开始---request.headers:\n\n", request.headers, "结束---request.headers\n")

    can_play = check_data()
    if can_play:
        button_type = "\"button red\""
        play_disabled = ""
    else:
        button_type = "\"button gray\""
        play_disabled = "disabled"
    return render_template("index.html", button_type=button_type, play_disabled=play_disabled)


@sudoku_web.route("/sudoku.html")
def sudoku_play():
    return sudoku_web.send_static_file("sudoku.html")


@sudoku_web.route("/sudoku_result.html", methods=["post"])
def result():
    pass


@sudoku_web.route("/inputsudo.html")
def input_sudo():
    return sudoku_web.send_static_file("input_sudo.html")


@sudoku_web.route("/get_data", methods=("GET",))
def get_data():
    dataSudoku = GetRandomData()
    difficulty = sudoku.difficulty(dataSudoku)
    tabSudoku = "<table cellpadding='0' cellspacing='0' border='1'>"
    for i in range(0, 9):
        tabSudoku += "<tr>"
        for j in range(0, 9):
            cellNum = dataSudoku[i*9+j]
            zeroState = rightState = bottomState = False
            if cellNum == "0":
                cellNum = ""
                zeroState = True
            cellDiv = f"<div class='input_cell' id='input_cell_{i}{j}' contenteditable='{zeroState}' style='max-width:10mm;max-height:10mm;overflow:hidden'>{cellNum}</div>"

            if j % 3 == 2 and j != 8:
                rightState = True
            if i % 3 == 2 and i != 8:
                bottomState = True

            classValue = ""
            if zeroState == True:
                classValue += " zeroCell"
            if rightState == True:
                classValue += " rightBolder"
            if bottomState == True:
                classValue += " bottomBolder"
            classValue = classValue.strip()
            tdType = "<td>"
            if len(classValue) != 0:
                tdType = f"<td class='{classValue}'>"
            tabSudoku += f"{tdType}{cellDiv}</td>"
        tabSudoku += "</tr>"
    tabSudoku += "</table>"
    return str(difficulty)+' '+tabSudoku


@sudoku_web.route("/save_data", methods=("POST",))
def save_data():
    dataSudoku = request.form["data"]
    dataSudoku = dataSudoku.split(",")
    data = ""
    for c in dataSudoku:
        data += c
    with open("data\\sudoku.data", "a", encoding="utf-8") as f:
        f.write(data+"\n")

    return "Save Success!"


@sudoku_web.route("/finish_game",methods=("POST",))
def finish_game():
    dataSudoku = request.form["data"]
    dataSudoku = dataSudoku.split(",")
    data = [int(s) for s in dataSudoku]
    if sudoku.check(data):
        return "Success!"
    return "Fail!"


@sudoku_web.route("/winning.html")
def winning():
    return sudoku_web.send_static_file("winning.html")


if __name__ == "__main__":
    sudoku_web.run(host="0.0.0.0", port=80, debug=True)
