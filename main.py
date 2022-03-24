from flask import Flask, render_template
import glob
import random


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
    can_play = check_data()
    if can_play:
        button_type = "\"button red\""
        play_disabled = ""
    else:
        button_type = "\"button gray\""
        play_disabled = "disabled"
    return render_template("index.html", button_type=button_type, play_disabled=play_disabled)


@sudoku_web.route("/sudoku.html")
def sudoku():
    dataSudoku = GetRandomData()

    tabSudoku = "<table cellpadding='0' cellspacing='0' border='1'>"
    for i in range(0, 9):
        tabSudoku += "<tr>"
        for j in range(0, 9):
            cellNum = dataSudoku[i*9+j]
            zeroState = rightState = bottomState = False
            if cellNum == "0":
                cellNum = ""
                zeroState = True
            cellDiv = f"<div class='input_cell' id='input_cell_{i}{j}' contenteditable='{zeroState}' style='max-width:10mm max-height:10mm'>{cellNum}</div>"

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
    return render_template("sudoku.html", placeContent=tabSudoku)



@sudoku_web.route("/sudoku_result.html",methods=["post"])
def result():
    pass


@sudoku_web.route("/inputsudo.html")
def input_sudo():
    dataSudoku = ["0" for i in range(81)]

    tabSudoku = "<table cellpadding='0' cellspacing='0' border='1'>"
    for i in range(0, 9):
        tabSudoku += "<tr>"
        for j in range(0, 9):
            cellNum = dataSudoku[i*9+j]
            zeroState = rightState = bottomState = False
            if cellNum == "0":
                cellNum = ""
                zeroState = True
            cellDiv = f"<div class='input_cell' id='input_cell_{i}{j}' contenteditable='{zeroState}' style='max-width:10mm max-height:10mm'>{cellNum}</div>"

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
    return render_template("input_sudo.html", placeContent=tabSudoku)


if __name__ == "__main__":
    sudoku_web.run(host="0.0.0.0", port=80, debug=True)
