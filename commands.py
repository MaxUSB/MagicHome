import tkinter as tk
import time
from subprocess import call, Popen, PIPE

# widgets var
root = None
# frame1 = None
switch_button = None
# frame2 = None
preset_button1 = None
preset_button2 = None
preset_button3 = None
# frame3 = None
red_scale = None
green_scale = None
blue_scale = None
set_button = None


def main():
    global root, frame1, switch_button, frame2, preset_button1, preset_button2, preset_button3, frame3, red_scale, green_scale, blue_scale, set_button

    # main window
    install_library()
    root = tk.Tk()
    root.geometry('300x500')
    root.title('Magic Home')
    # root.resizable(False, False)

    # widgets
    # frame1 = tk.Frame(root)
    switch_button = tk.Button(root, text='switch button', width='30', font='helvetica 40')
    # frame2 = tk.Frame(root)
    preset_button1 = tk.Button(root, text='-', font='helvetica 40', fg='#34ebd5', command=preset_1)
    preset_button2 = tk.Button(root, text='-', font='helvetica 40', fg='#ff8533', command=preset_2)
    preset_button3 = tk.Button(root, text='-', font='helvetica 40', fg='#ff0000', command=preset_3)
    # frame3 = tk.Frame(root)
    red_scale = tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=255, tickinterval=50, resolution=5)
    green_scale = tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=255, tickinterval=50, resolution=5)
    blue_scale = tk.Scale(root, orient=tk.HORIZONTAL, from_=0, to=255, tickinterval=50, resolution=5)
    switch_button = tk.Button(root, text='Set Color', width='30', font='helvetica 40', command=set_color)
    update_widgets()
    tk.mainloop()


def set_color():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-c', f'{red_scale.get()},{green_scale.get()},{blue_scale.get()}'], stdout=PIPE)


def preset_1():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-c', '"#34ebd5"'], stdout=PIPE)


def preset_2():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-c', '"#ff8533"'], stdout=PIPE)


def preset_3():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-c', '"#ff0000"'], stdout=PIPE)


def turn_on():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-1'], stdout=PIPE)
    update_widgets(True)


def turn_off():
    Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-0'], stdout=PIPE)
    update_widgets(True)


def is_on():
    p = Popen(['python3', '-m', 'flux_led', '192.168.0.231', '-i'], stdout=PIPE)
    output = str(p.communicate())
    if output.find('ON') != -1:
        return True
    return False


def update_widgets(sleep=False):
    global switch_button, set_button
    if sleep:
        time.sleep(0.5)
    if is_on():
        switch_button['command'] = turn_off
        switch_button['text'] = 'Turn OFF'
        switch_button['fg'] = 'red'
    else:
        switch_button['command'] = turn_on
        switch_button['text'] = 'Turn ON'
        switch_button['fg'] = 'green'
    # frame1.pack(side='top')
    switch_button.grid(row=0, column=0, columnspan=3)
    # frame2.pack(side='top')
    preset_button1.grid(row=1, column=0)
    preset_button2.grid(row=1, column=1)
    preset_button3.grid(row=1, column=2)
    # frame3.pack(side='top')
    red_scale.grid(row=2, column=0, columnspan=3)
    green_scale.grid(row=3, column=0, columnspan=3)
    blue_scale.grid(row=4, column=0, columnspan=3)
    # set_button.pack(side='top')


def install_library():
    p = Popen(['pip3', 'show', 'flux_led'], stdout=PIPE)
    if str(p.communicate()).find('not found') != -1:
        call('pip3 install flux_led')


if __name__ == '__main__':
    main()
