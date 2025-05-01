import numpy as np
import tabulate
import matplotlib.pyplot as plt

dict = {
"latex_key" : ["latextable", "latex", "table", "tabulate", "latextablecerator",
                "latextableformat", "tabular"],
"plot_key" : ["plot", "graphs", "solutionplot", "odesolution", "plotting"]
}

def help(kw = ""):
    if((kw.lower()).replace(" ", "") in dict["latex_key"]):
        Notes = '''
        Function Name: latexit

        Inputs: cols: # of columns of the table
                headers: list of header names
                *args : all columns as lists (in the same order as headers)

                (optional)
                style:
                  (Default) style = 1: prints latex table with column lines
                            style = 0: prints latex table without column lines


        Outputs: Tabulates given values and prints it in latex table format.
        '''
        print(Notes)

    if((kw.lower()).replace(" ", "") in dict["plot_key"]):
        Notes = '''
        Function Name: plotit

        Inputs: t: the time axis (time array, or x-values array)
                labels: Array of labels of the plots
                *args: all the arrays (to be plotted) in the same order as headers

        Outputs: Plots all the given arrays against the x-values array
                 Prints latex code for including the generated plot
        '''
        print(Notes)

    return 0






#------------------------------------------------------------
#creating latex tables in python!


def latexit(cols, headers, *args, style = 1):
    if(style == 0):
        latexit1(cols, headers, *args)
    if(style == 1):
        latexit2(cols, headers, *args)



def latexit1(cols, headers, *args):
    N = len(args[0])-1
    table = np.zeros((N+1, cols))
    for i in range(N+1):
        temp = []
        for j in range(len(args)):
            temp.append(args[j][i])
        table[i] = temp
    print(tabulate.tabulate(table, \
        headers = headers,  \
        floatfmt=".8f", tablefmt="latex"))

#--------------------------------------------------------------

def latexit2(cols, headers, *args):
    col_str = "c|"
    print("\\begin{center}")
    print("\\begin{tabular}{|%s|%s}"%(col_str, col_str*(cols-1))    )
    print("\\hline")
    string = ""
    for i in range(len(headers)):
        if(i != len(headers) - 1):
            string += "%s   &  "%headers[i]
        else:
            string += "%s \\\ "%headers[i]
    print(string)
    print("\\hline")
    print("\\hline")
    N = len(args[0])-1
    table = np.zeros((N+1, cols))
    for i in range(N+1):
        temp = []
        for j in range(len(args)):
            temp.append(args[j][i])
        table[i] = temp
    for m in range(len(table)):
        string = ""
        for n in range(len(table[m])):
            if(n != len(table[m]) - 1):
                string += "%s   &  "%table[m][n]
            else:
                string += "%s \\\ \\hline"%table[m][n]
        print(string)
    print("\\hline")
    print("\\end{tabular}")
    print("\\end{center}")


def plotit(name, t, label, *args):
    for i in range(len(args)):
        plt.plot(t, args[i], label = label[i])
    plt.legend()
    plt.show()
    print('''
    \\begin{figure}[h]
	\\centering
	\\includegraphics[scale = 0.75]{%s.png}
	\\caption{Plot of the solution}
    \\end{figure}'''%name)
