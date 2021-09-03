from QRalgorithm import *

from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os



def get_file_path():
    file_path.set(filedialog.askopenfilename(title="Select A File", filetypes=[("excel file", "*.xlsx")]))
    text_box['state'] = 'normal'
    text_box.insert(INSERT, ' '.join(['File path: ', file_path.get(), '\n']))  # INSERT keyword is important
    text_box['state'] = 'disabled'
    flg.set(1)


def clear_text():
    text_box['state'] = 'normal'
    text_box.delete(1.0, END)
    text_box['state'] = 'disabled'
    # check meaning


def option_activation():
    status = 'normal' if options_flg.get() == 1 else 'disabled'  # get() not get
    check_button1['state'] = status
    check_button2['state'] = status
    check_button3['state'] = status
    check_button4['state'] = status
    check_button5['state'] = status


def check():
    text_box['state'] = 'normal'
    text_box.insert(INSERT, percent.get())
    text_box['state'] = 'disabled'


def number_of_components(eig_vectors, arr, var_ratio):
    sum, i = 0, 0
    while sum < percent.get() and i < arr.shape[1]:
        sum += var_ratio[i]
        i += 1
    transformation_matrix = eig_vectors[:, 0:i]
    result = matrix_multiplication(arr, transformation_matrix)  # on standardized data
    return result, i


def execute():
    arr = pd.read_excel(file_path.get()).to_numpy(dtype=float)
    # arr = np.random.RandomState(54).rand(10, 3)
    np.set_printoptions(3)
    # nptabulate = lambda a: tabulate(arr, tablefmt='psql')

    mean = mean_data(arr)
    s_deviation = standard_deviation(arr, mean)
    scaling(arr, s_deviation, mean)
    if standardize_flg.get():
        text_box['state'] = 'normal'
        format(arr, 'STANDARDIZED DATA')
        text_box.insert(INSERT, '\n\n')
        text_box['state'] = 'disabled'

    mean = mean_data(arr)  # as mean of data changes
    cov_mat = covariance_matrix(arr, mean)
    if cov_flg.get():
        text_box['state'] = 'normal'
        format(cov_mat, 'COVARIANCE MATRIX')
        text_box.insert(INSERT, '\n\n')
        text_box['state'] = 'disabled'

    A = QR_method(cov_mat)
    var_ratio = variance_ratio(A)
    if qr_flg.get():
        text_box['state'] = 'normal'
        format(A, 'EIGEN VALUES')
        text_box.insert(INSERT, '\n\n')
        text_box['state'] = 'disabled'

    eigvectors = eigen_vectors(cov_mat, A)
    if gauss_flg.get():
        text_box['state'] = 'normal'
        format(eigvectors, 'EIGEN VECTORS')
        text_box.insert(INSERT, '\n\n')
        text_box['state'] = 'disabled'

    if varratio_flg.get():
        text_box['state'] = 'normal'
        text_box.insert(INSERT, '\t')
        text_box.insert(INSERT, 'VARIANCE RATIO')
        text_box.insert(INSERT, '\n\n')
        for j in var_ratio:
            text_box.insert(INSERT, round(j, 4))
            text_box.insert(INSERT, '\t\t')
        text_box.insert(INSERT, '\n\n')
        text_box['state'] = 'disabled'

    result, number = number_of_components(eigvectors, arr, var_ratio)
    text_box['state'] = 'normal'
    text_box.insert(INSERT, '\n\n')
    format(result, 'RESULTANT DATA')
    text_box.insert(INSERT, 'Number of components used: ')
    text_box.insert(INSERT, number)
    text_box.insert(INSERT, '\n')
    text_box['state'] = 'disabled'

    global transformed_data, eigen_vector_data, eigen_value_data, var_ratio_data
    transformed_data = result.copy()
    eigen_vector_data = eigvectors.copy()
    eigen_value_data = A.copy()
    var_ratio_data =  var_ratio.copy()


def format(A, title):  # only for 2d arrays
    text_box.insert(INSERT, '\t')
    text_box.insert(INSERT, title)
    text_box.insert(INSERT, '\n\n')
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            temp = np.around(A[i][j], 5)
            text_box.insert(INSERT, temp)
            text_box.insert(INSERT, '\t\t')  # tab works for alignment
        text_box.insert(INSERT, '\n')


def save():
    global transformed_data, eigen_vector_data, eigen_value_data, var_ratio_data
    transformed_data = pd.DataFrame(transformed_data)
    eigen_vector_data = pd.DataFrame(eigen_vector_data)
    eigen_value_data = pd.DataFrame(eigen_value_data)
    var_ratio_data = pd.DataFrame(var_ratio_data)
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    with pd.ExcelWriter(export_file_path) as writer:  # not working if stored in variable; have to use for multisheet
        transformed_data.to_excel(writer, sheet_name='Result', index=False, header=False)
        eigen_value_data.to_excel(writer, sheet_name='Eigen Value', index=False, header=False)
        eigen_vector_data.to_excel(writer, sheet_name='Eigen Vectors', index=False, header=False)
        var_ratio_data.to_excel(writer, sheet_name='Variance Distribution', index=False, header=False)
    os.startfile(export_file_path)


def help():
    messagebox.showinfo('Help', '  1.Select excel file containing data.\n\n  2.Click on execute'
                                '\n\n  3.Save results at desired location')


def author():
    messagebox.showinfo('Developer',
                        '    Mohammad Daanish Shaikh   \n\n    Roll no. 5  \n\n    Branch - ENTC   Div - C')


Height = 400
Width = 925
main = Tk()
main.title('')
main.geometry('1000x600')
main.resizable(0, 0)
main.title('Software Development Project')

file_path = StringVar(main)  # cannot declare before main window declaration
flg = IntVar(main, value=0)
options_flg = IntVar(main, value=0)
standardize_flg = IntVar(main, value=1)
cov_flg = IntVar(main, value=1)
qr_flg = IntVar(main, value=1)
gauss_flg = IntVar(main, value=1)
varratio_flg = IntVar(main, value=1)
percent = IntVar(main, value=100)

transformed_data = pd.DataFrame()
eigen_vector_data = pd.DataFrame()
eigen_value_data = pd.DataFrame()
var_ratio_data = pd.DataFrame()

canvas = Canvas(main, bg='#000000', height=Height, width=Width, scrollregion=(0, 0, 2000, 2000))
canvas.place(relwidth=1, relheight=1)

side_frame = ttk.Frame(main, padding='2 2 2 2')
side_frame.place(relheight=0.9, relwidth=0.2, relx=0.03, rely=0.05)

# for adding color
# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
# s.configure('TFrame', background='#252626')
# s.configure('TCombobox', foreground='#252626')
s.configure('.', font=('Corbel', 10, 'bold'), foreground='maroon')  # Root style, changes options of all widgets

# frame used to make title overlap mini windows and prevent them from covering it
title = Label(canvas, text='Principal Component Analysis', font=('Bahnschrift semilight', 24), bg='red', relief='flat',
              fg='black',
              justify=CENTER)
title.place(relx=0.38, rely= 0.05, relwidth=0.45, relheight=0.08)

text_box = Text(main, font='Bahnschrift 13', wrap=NONE, spacing3=10, bd=5, padx=15, pady=10,
                tabs='1.5c')  # wrapping makes width constant
text_box.place(relx=0.25, rely=0.15, relwidth=0.725, relheight=0.8)

yscroll = ttk.Scrollbar(text_box)
# Parent of any widget has to be defined before hand
yscroll.pack(fill=Y, side=RIGHT)
# Using pack() is the most straightforward  approach for scrollbars
text_box.configure(yscrollcommand=yscroll.set)
# Configure has been used here as before scroll was not defined hence throwing error
yscroll.config(command=text_box.yview)

xscroll = ttk.Scrollbar(text_box)
xscroll.pack(fill=X, side=BOTTOM)
text_box.configure(xscrollcommand=xscroll.set)
xscroll.config(command=text_box.xview, orient=HORIZONTAL)

button_excel = ttk.Button(side_frame, text='Excel File', command=get_file_path)
button_excel.place(relx=0.25, rely=0.05, relheight=0.05, relwidth=0.5)

button_execute = ttk.Button(side_frame, text='EXECUTE', command=execute)
button_execute.place(relx=0.25, rely=0.15, relheight=0.05, relwidth=0.5)

button_clear = ttk.Button(side_frame, text='CLEAR', command=clear_text)  # first enable to delete
button_clear.place(relx=0.25, rely=0.25, relheight=0.05, relwidth=0.5)

button_save = ttk.Button(side_frame, text='SAVE', command=save)  # first enable to delete
button_save.place(relx=0.25, rely=0.35, relheight=0.05, relwidth=0.5)

radio_button1 = ttk.Radiobutton(side_frame, text='Simplified', value=0, variable=options_flg, command=option_activation)
radio_button2 = ttk.Radiobutton(side_frame, text='Advanced', value=1, variable=options_flg, command=option_activation)
radio_button1.place(relx=0.18, rely=0.49)
radio_button2.place(relx=0.18, rely=0.54)

check_button1 = ttk.Checkbutton(side_frame, text='Standardize data', variable=standardize_flg)  # default is 0-1
check_button2 = ttk.Checkbutton(side_frame, text='Covariance Matrix', variable=cov_flg)
check_button3 = ttk.Checkbutton(side_frame, text='Eigen Value', variable=qr_flg)
check_button4 = ttk.Checkbutton(side_frame, text='Eigen Vector', variable=gauss_flg)
check_button5 = ttk.Checkbutton(side_frame, text='Variance Ratio', variable=varratio_flg)
check_button1.place(relx=0.2, rely=0.60)
check_button2.place(relx=0.2, rely=0.64)
check_button3.place(relx=0.2, rely=0.68)
check_button4.place(relx=0.2, rely=0.72)
check_button5.place(relx=0.2, rely=0.76)
option_activation()

scale = Scale(side_frame, resolution=0.1, to=100, variable=percent, orient=HORIZONTAL)
scale.place(relx=0.17, rely=0.85, relwidth=0.7)

menu = Menu(main)
About = Menu(menu, tearoff=0)
About.add_command(label='Help', command=help)
About.add_separator()
About.add_command(label='Author', command=author)
menu.add_cascade(label='Information', menu=About)
main.config(menu=menu)

main.mainloop()
