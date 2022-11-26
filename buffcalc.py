from tkinter import *
from tkinter import ttk

root = Tk()
root.title("bee tee dee six")
root.geometry("800x320")
# holy shit so bad lmfao
multiplier = {"damage": 0, "pierce": 0, "speed": 1}


def update(type, change):
    global multiplier
    ispercent = False
    totaldamage = 0
    stats = allvar[type][change].get().split()
    multiplier["damage"] += float(stats[0])
    if "%" in stats[1]:
        ispercent = True
        #multiplier["pierce"] += towerstat[1]["pierce"].get() * (
        #    float(stats[1][:-1]) / 100
        #)
    else:
        multiplier["pierce"] += float(stats[1])
    multiplier["speed"] *= float(stats[2])
    for i in range(1, 5):
        if toggle[str(i)].get() and towerstat[str(i)]['speed'] != 0.0:
            temp = towerstat[str(i)]
            output[str(i)]["damage"].config(
                text=f'{round(multiplier["damage"] + temp["damage"].get())}'
            )
            if ispercent:
                output[str(i)]["pierce"].config(
                    text=f'{round(multiplier["damage"] + temp["pierce"].get() * (float(stats[1][:-1])) / 100 + temp["damage"].get(), 4)}'
                )
            else:
                output[str(i)]["pierce"].config(
                    text=f'{round(multiplier["damage"] + temp["damage"].get(), 4)}'
                )
            # speed.config(text=f'{round(multiplier["speed"] * towerstat["speed"].get(), 4)}')
            output[str(i)]["speed"].config(
                text=f'{round((1 / temp["speed"].get()) / multiplier["speed"], 4)}'
            )
            output[str(i)]["singletarget"].config(
                text=round(
                    float(output[str(i)]["damage"]["text"])
                    * float(output[str(i)]["speed"]["text"])
                    * float(temp["j"].get()),
                    4,
                )
            )
            totaldamage += float(output[str(i)]["singletarget"]["text"])
    totaldps.config(text=round(totaldamage, 4))


# variables
towerstat = {
    "1": {
        "damage": DoubleVar(),
        "pierce": DoubleVar(),
        "speed": DoubleVar(),
        "j": DoubleVar(),
    },
    "2": {
        "damage": DoubleVar(),
        "pierce": DoubleVar(),
        "speed": DoubleVar(),
        "j": DoubleVar(),
    },
    "3": {
        "damage": DoubleVar(),
        "pierce": DoubleVar(),
        "speed": DoubleVar(),
        "j": DoubleVar(),
    },
    "4": {
        "damage": DoubleVar(),
        "pierce": DoubleVar(),
        "speed": DoubleVar(),
        "j": DoubleVar(),
    },
}
allvar = {
    "normalbuff": {
        "pbruh": StringVar(),
        "amd": StringVar(),
        "temple": StringVar(),
        "tsg": StringVar(),
        "drums": StringVar(),
        "homeland": StringVar(),
        "oc": StringVar(),
        "uboost": StringVar(),
        "mboost": StringVar(),
    },
    "towerbuff": {
        "flagshit": StringVar(),
        "shonob": StringVar(),
        "pooplust": StringVar(),
        "pmfc": StringVar(),
        "tt5": StringVar(),
    },
    "debuff": {
        "sbruh": StringVar(),
        "cripple": StringVar(),
        "embrit": StringVar(),
        "glorm": StringVar(),
    },
    "herobuff": {
        "gwen": StringVar(),
        "pat": StringVar(),
        "elizi": StringVar(),
        "brickell": StringVar(),
    },
}
for item in allvar:
    for iter in allvar[item]:
        allvar[item][iter].set("0 0 0")
# outputs
Label(root, text="damage: ", font=("Arial", 12)).grid(column=3, row=6)
Label(root, text="pierce: ", font=("Arial", 12)).grid(column=3, row=7)
# Label(root, text='speed: ', font=('Arial', 12)).grid(column=5, row=7)
Label(root, text="atk per s:", font=("Arial", 12)).grid(column=3, row=8)
Label(root, text="single target:", font=("Arial", 12)).grid(column=3, row=9)
totaldps = Label(root, text="None", font=("Arial", 12))
totaldps.grid(column=5, row=9)
output = {
    "1": {
        "damage": Label(root, text="None", font=("Arial", 12)),
        "pierce": Label(root, text="None", font=("Arial", 12)),
        "speed": Label(root, text="None", font=("Arial", 12)),
        "singletarget": Label(root, text="None", font=("Arial", 12)),
    },
    "2": {
        "damage": Label(root, text="None", font=("Arial", 12)),
        "pierce": Label(root, text="None", font=("Arial", 12)),
        "speed": Label(root, text="None", font=("Arial", 12)),
        "singletarget": Label(root, text="None", font=("Arial", 12)),
    },
    "3": {
        "damage": Label(root, text="None", font=("Arial", 12)),
        "pierce": Label(root, text="None", font=("Arial", 12)),
        "speed": Label(root, text="None", font=("Arial", 12)),
        "singletarget": Label(root, text="None", font=("Arial", 12)),
    },
    "4": {
        "damage": Label(root, text="None", font=("Arial", 12)),
        "pierce": Label(root, text="None", font=("Arial", 12)),
        "speed": Label(root, text="None", font=("Arial", 12)),
        "singletarget": Label(root, text="None", font=("Arial", 12)),
    },
}
for i in range(1, 5):
    for index, item in enumerate(output[str(i)]):
        output[str(i)][item].grid(column=i + 5, row=index + 6)
# label
Label(root, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|").grid(
    column=4, row=1, rowspan=9
)
Label(root, text="damage:", font=("Arial", 12)).grid(column=5, row=1)
Label(root, text="pierce:", font=("Arial", 12)).grid(column=5, row=2)
Label(root, text="speed:", font=("Arial", 12)).grid(column=5, row=3)
Label(root, text="# of proj:", font=("Arial", 12)).grid(column=5, row=4)
Label(root, text="total dps", font=("Arial", 12)).grid(column=5, row=6)
Label(root, text="|", font=("Arial", 12)).grid(column=5, row=7)
Label(root, text="v", font=("Arial", 12)).grid(column=5, row=8)
# enable calcs
toggle = {"1": BooleanVar(), "2": BooleanVar(), "3": BooleanVar(), "4": BooleanVar()}
Checkbutton(
    root,
    variable=toggle["1"],
    onvalue=True,
    offvalue=False,
).grid(column=6, row=5)
Checkbutton(
    root,
    variable=toggle["2"],
    onvalue=True,
    offvalue=False,
).grid(column=7, row=5)
Checkbutton(
    root,
    variable=toggle["3"],
    onvalue=True,
    offvalue=False,
).grid(column=8, row=5)
Checkbutton(
    root,
    variable=toggle["4"],
    onvalue=True,
    offvalue=False,
).grid(column=9, row=5)
# entry
entries = {
    "1": {
        'damage': Entry(
            root, width=10, textvariable=towerstat["1"]["damage"], font=("Arial", 12)
        ),
        'pierce': Entry(
            root, width=10, textvariable=towerstat["1"]["pierce"], font=("Arial", 12)
        ),
        'speed': Entry(root, width=10, textvariable=towerstat["1"]["speed"], font=("Arial", 12)),
        'j': Entry(root, width=10, textvariable=towerstat["1"]["j"], font=("Arial", 12)),
    },
    "2": {
        'damage': Entry(
            root, width=10, textvariable=towerstat["2"]["damage"], font=("Arial", 12)
        ),
        'pierce': Entry(
            root, width=10, textvariable=towerstat["2"]["pierce"], font=("Arial", 12)
        ),
        'speed': Entry(root, width=10, textvariable=towerstat["2"]["speed"], font=("Arial", 12)),
        'j': Entry(root, width=10, textvariable=towerstat["2"]["j"], font=("Arial", 12)),
    },
    "3": {
        'damage': Entry(
            root, width=10, textvariable=towerstat["3"]["damage"], font=("Arial", 12)
        ),
        'pierce': Entry(
            root, width=10, textvariable=towerstat["3"]["pierce"], font=("Arial", 12)
        ),
        'speed': Entry(root, width=10, textvariable=towerstat["3"]["speed"], font=("Arial", 12)),
        'j': Entry(root, width=10, textvariable=towerstat["3"]["j"], font=("Arial", 12)),
    },
    "4": {
        'damage': Entry(
            root, width=10, textvariable=towerstat["4"]["damage"], font=("Arial", 12)
        ),
        'pierce': Entry(
            root, width=10, textvariable=towerstat["4"]["pierce"], font=("Arial", 12)
        ),
        'speed': Entry(root, width=10, textvariable=towerstat["4"]["speed"], font=("Arial", 12)),
        'j': Entry(root, width=10, textvariable=towerstat["4"]["j"], font=("Arial", 12)),
    },
}
for i in range(1, 5):
    for index, item in enumerate(entries[str(i)]):
        entries[str(i)][item].grid(column=i + 5, row=index + 1)
# checkboxes
# ordered in [damage, pierce, speed]
Checkbutton(
    root,
    text="pbruh no amd",
    variable=allvar["normalbuff"]["pbruh"],
    onvalue="1 3 0.85",
    offvalue="-1 -3 1.1764705882352942",
    command=lambda: update("normalbuff", "pbruh"),
).grid(row=1, column=1, sticky=W)
Checkbutton(
    root,
    text="amd only",
    variable=allvar["normalbuff"]["amd"],
    onvalue="1 0 1",
    offvalue="-1 0 1",
    command=lambda: update("normalbuff", "amd"),
).grid(row=2, column=1, sticky=W)
Checkbutton(
    root,
    text="t4 temple only",
    variable=allvar["normalbuff"]["temple"],
    onvalue="2 3 0.81",
    offvalue="-2 -3 1.2345679012345678",
    command=lambda: update("normalbuff", "temple"),
).grid(row=3, column=1, sticky=W)
Checkbutton(
    root,
    text="t5 temple only",
    variable=allvar["normalbuff"]["tsg"],
    onvalue="2 3 0.81",
    offvalue="-2 -3 1.2345679012345678",
    command=lambda: update("normalbuff", "tsg"),
).grid(row=4, column=1, sticky=W)
Checkbutton(
    root,
    text="bongos",
    variable=allvar["normalbuff"]["drums"],
    onvalue="0 0 0.85",
    offvalue="0 0 1.1764705882352942",
    command=lambda: update("normalbuff", "drums"),
).grid(row=5, column=1, sticky=W)
Checkbutton(
    root,
    text="homeland",
    variable=allvar["normalbuff"]["homeland"],
    onvalue="0 100% 0.50",
    offvalue="0 -100% 2",
    command=lambda: update("normalbuff", "homeland"),
).grid(row=6, column=1, sticky=W)
Checkbutton(
    root,
    text="oc",
    variable=allvar["normalbuff"]["oc"],
    onvalue="0 0 0.60",
    offvalue="0 0 1.6666666666666667",
    command=lambda: update("normalbuff", "oc"),
).grid(row=7, column=1, sticky=W)
Checkbutton(
    root,
    text="10 ub stacks",
    variable=allvar["normalbuff"]["uboost"],
    onvalue="0 0 0.60",
    offvalue="0 0 1.6666666666666667",
    command=lambda: update("normalbuff", "uboost"),
).grid(row=8, column=1, sticky=W)
Checkbutton(
    root,
    text="mboost(power)",
    variable=allvar["normalbuff"]["mboost"],
    onvalue="0 0 0.50",
    offvalue="0 0 2",
    command=lambda: update("normalbuff", "mboost"),
).grid(row=9, column=1, sticky=W)
# -------------------------------------------------------------------------------------------------------------------------------
Checkbutton(
    root,
    text="flagcrap",
    variable=allvar["towerbuff"]["flagshit"],
    onvalue="0 0 0.85",
    offvalue="0 0 1.1764705882352942",
    command=lambda: update("towerbuff", "flagshit"),
).grid(row=1, column=2, sticky=W)
Checkbutton(
    root,
    text="20x shonob",
    variable=allvar["towerbuff"]["shonob"],
    onvalue="0 60% 0.1886933291627967",
    offvalue="0 -60% 5.299604413345433",
    command=lambda: update("towerbuff", "shonob"),
).grid(row=2, column=2, sticky=W)
Checkbutton(
    root,
    text="5x pooplust",
    variable=allvar["towerbuff"]["pooplust"],
    onvalue="0 75% 0.5714285714285714",
    offvalue="0 -75% 1.75",
    command=lambda: update("towerbuff", "pooplust"),
).grid(row=3, column=2, sticky=W)
Checkbutton(
    root,
    text="pmfc",
    variable=allvar["towerbuff"]["pmfc"],
    onvalue="1 3 0.0316",
    offvalue="-1 -3 31.645569620253163",
    command=lambda: update("towerbuff", "pmfc"),
).grid(row=4, column=2, sticky=W)
# -------------------------------------------------------------------------------------------------------------------------------
Checkbutton(
    root,
    text="sbruh",
    variable=allvar["debuff"]["sbruh"],
    onvalue="4 0 1",
    offvalue="-4 0 1",
    command=lambda: update("debuff", "sbruh"),
).grid(row=6, column=2, sticky=W)
Checkbutton(
    root,
    text="embrit",
    variable=allvar["debuff"]["embrit"],
    onvalue="1 0 1",
    offvalue="-1 0 1",
    command=lambda: update("debuff", "embrit"),
).grid(row=7, column=2, sticky=W)
Checkbutton(
    root,
    text="cripple",
    variable=allvar["debuff"]["cripple"],
    onvalue="5 0 1",
    offvalue="-5 0 1",
    command=lambda: update("debuff", "cripple"),
).grid(row=8, column=2, sticky=W)
Checkbutton(
    root,
    text="glorm",
    variable=allvar["debuff"]["glorm"],
    onvalue="2 0 1",
    offvalue="-2 0 1",
    command=lambda: update("debuff", "glorm"),
).grid(row=9, column=2, sticky=W)
# -------------------------------------------------------------------------------------------------------------------------------
Checkbutton(
    root,
    text="gwen",
    variable=allvar["herobuff"]["gwen"],
    onvalue="1 1 1",
    offvalue="-1 -1 1",
    command=lambda: update("herobuff", "gwen"),
).grid(row=1, column=3, sticky=W)
Checkbutton(
    root,
    text="pat",
    variable=allvar["herobuff"]["pat"],
    onvalue="3 0 1",
    offvalue="-3 0 1",
    command=lambda: update("herobuff", "pat"),
).grid(row=2, column=3, sticky=W)
Checkbutton(
    root,
    text="elizi",
    variable=allvar["herobuff"]["elizi"],
    onvalue="0 1 0.85",
    offvalue="0 -1 1.1764705882352942",
    command=lambda: update("herobuff", "elizi"),
).grid(row=3, column=3, sticky=W)
Checkbutton(
    root,
    text="brickell",
    variable=allvar["herobuff"]["brickell"],
    onvalue="0 0 0.5",
    offvalue="0 0 2",
    command=lambda: update("herobuff", "brickell"),
).grid(row=4, column=3, sticky=W)
# -------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
