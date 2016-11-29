from Tkinter import *
import csv 

# based on code from http://stackoverflow.com/questions/8959815/restricting-the-value-in-tkinter-entry-widget

# wipe the floor
def wipe():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    e13.delete(0,END)
    e14.delete(0,END)
    e15.delete(0,END)
    e16.delete(0,END)

def validateName(text):
        if (isinstance(text, basestring)):
            try:
                return True
            except ValueError:
                return False
        else:
            return False

def validateScore(text, pre, insert):
    if (int(insert) == 0):
            return True
    if (text in '123-'):
        if(text == '-'):
            if (pre == ''):
                return True
            else:
                return False
        num = int(pre + text)
        if((num >= -3) and (num <= 3)):
            return True
    return False

        


#based on code from http://www.python-course.eu/tkinter_entry_widgets.php
def calc():
    artist = e1.get()
    title = e2.get()
    values = [float(e3.get()), float(e4.get()), float(e5.get()), float(e6.get()), float(e7.get()), float(e8.get()), float(e9.get()), float(e10.get()), float(e11.get()), float(e12.get()), float(e13.get()), float(e14.get()), float(e15.get()), float(e16.get())]

    # calculate ratings
    score_m = (values[0] * -0.02) + (values[1] * -0.16) + (values[2] * -0.05) + (values[3] * -0.43) + (values[4] * 0.05) + (values[5] * -0.38) + (values[6] * -0.11) + (values[7] * -0.47) + (values[8] * -0.18) + (values[9] * 0.09) + (values[10] * 0.18) + (values[11] * 0.56) + (values[12] * 0.57) + (values[13] * 0.32)
    score_u = (values[0] * -0.01) + (values[1] * 0.09) + (values[2] * 0.32) + (values[3] * 0.08) + (values[4] * 0.04) + (values[5] * -0.03) + (values[6] * 0.17) + (values[7] * 0.08) + (values[8] * 0.08) + (values[9] * -0.11) + (values[10] * -0.08) + (values[11] * -0.07) + (values[12] * -0.10) + (values[13] * -0.24)
    score_s = (values[0] * -0.08) + (values[1] * -0.42) + (values[2] * -0.66) + (values[3] * -0.07) + (values[4] * 0.30) + (values[5] * -0.27) + (values[6] * -0.53) + (values[7] * -0.22) + (values[8] * 0.34) + (values[9] * 0.55) + (values[10] * 0.58) + (values[11] * 0.32) + (values[12] * 0.23) + (values[13] * 0.01)
    score_i = (values[0] * 0.22) + (values[1] * 0.67) + (values[2] * 0.54) + (values[3] * 0.41) + (values[4] * 0.05) + (values[5] * 0.64) + (values[6] * 0.49) + (values[7] * 0.66) + (values[8] * 0.14) + (values[9] * -0.32) + (values[10] * -0.40) + (values[11] * -0.54) + (values[12] * -0.49) + (values[13] * -0.10)
    score_c = (values[0] * -0.07) + (values[1] * -0.31) + (values[2] * -0.25) + (values[3] * -0.22) + (values[4] * -0.31) + (values[5] * -0.26) + (values[6] * -0.11) + (values[7] * -0.48) + (values[8] * -0.41) + (values[9] * -0.10) + (values[10] * -0.15) + (values[11] * 0.15) + (values[12] * 0.18) + (values[13] * 0.15)

    # set up some stuff 
    scores = [score_m, score_u, score_s, score_i, score_c]
    score_high = max(scores)
    index_high = scores.index(score_high)

    #print to cmd
    print("Mellow:\t\t\t%f\nUrban:\t\t\t%f\nSophisticated:\t%f\nIntense:\t\t%f\nCampestral:\t\t%f\n" % (score_m, score_u, score_s, score_i, score_c))
    classes = ["Mellow", "Urban", "Sophisticated", "Intense", "Campestral"]
    print("\nWinning Category: %s\n" % classes[index_high])
  
    # append csv
    fields=[artist, title, score_m, score_u, score_s, score_i, score_c, classes[index_high]]
    filename = e17.get() + '.csv'
    
    with open(filename, 'a') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(fields)
                print("Appended to %s\n" % filename)

    # reset fields

#main
master = Tk()
master.wm_title("Music Rec IQP Classification")
Label(master, text="Artist").grid(row=0)
Label(master, text="Song Name").grid(row=1)
Label(master, text="Dense").grid(row=3)
Label(master, text="Distorted").grid(row=4)     
Label(master, text="Electric").grid(row=5)
Label(master, text="Fast").grid(row=6) 
Label(master, text="Instrumental").grid(row=7)
Label(master, text="Loud").grid(row=8) 
Label(master, text="Percussive").grid(row=9)

Label(master, text="Aggressive").grid(row=11) 
Label(master, text="Complex").grid(row=12)
Label(master, text="Inspiring").grid(row=13) 
Label(master, text="Intelligent").grid(row=14)
Label(master, text="Relaxing").grid(row=15) 
Label(master, text="Romantic").grid(row=16)
Label(master, text="Sad").grid(row=17) 
Label(master, text="User's Last Name").grid(row=19) 

vmn = (master.register(validateName), '%S')
vms = (master.register(validateScore), '%S', '%s', '%d')

e1 = Entry(master, validate = 'key', validatecommand = vmn)
e2 = Entry(master, validate = 'key', validatecommand = vmn)

e3 = Entry(master, validate = 'key', validatecommand = vms)
e4 = Entry(master, validate = 'key', validatecommand = vms)
e5 = Entry(master, validate = 'key', validatecommand = vms)
e6 = Entry(master, validate = 'key', validatecommand = vms)
e7 = Entry(master, validate = 'key', validatecommand = vms)
e8 = Entry(master, validate = 'key', validatecommand = vms)
e9 = Entry(master, validate = 'key', validatecommand = vms)
e10 = Entry(master, validate = 'key', validatecommand = vms)
e11 = Entry(master, validate = 'key', validatecommand = vms)
e12 = Entry(master, validate = 'key', validatecommand = vms)
e13 = Entry(master, validate = 'key', validatecommand = vms)
e14 = Entry(master, validate = 'key', validatecommand = vms)
e15 = Entry(master, validate = 'key', validatecommand = vms)
e16 = Entry(master, validate = 'key', validatecommand = vms)
e17 = Entry(master, validate = 'key', validatecommand = vmn)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='                                       ', state=DISABLED).grid(row=2, column=0, sticky=W, pady=4)
Button(master, text='                                       ', state=DISABLED).grid(row=2, column=1, sticky=W, pady=4)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
Button(master, text='                                       ', state=DISABLED).grid(row=10, column=0, sticky=W, pady=4)
Button(master, text='                                       ', state=DISABLED).grid(row=10, column=1, sticky=W, pady=4)
e10.grid(row=11, column=1)
e11.grid(row=12, column=1)
e12.grid(row=13, column=1)
e13.grid(row=14, column=1)
e14.grid(row=15, column=1)
e15.grid(row=16, column=1)
e16.grid(row=17, column=1)
Button(master, text='                                       ', state=DISABLED).grid(row=18, column=0, sticky=W, pady=4)
Button(master, text='                                       ', state=DISABLED).grid(row=18, column=1, sticky=W, pady=4)
e17.grid(row=19, column=1)

Button(master, text='Quit', command=master.quit).grid(row=20, column=0, sticky=W, pady=4)
Button(master, text='Calculate', command=calc).grid(row=20, column=1, sticky=W, pady=4)
Button(master, text='Wipe', command=wipe).grid(row=20, column=2, sticky=W, pady=4)

mainloop( )