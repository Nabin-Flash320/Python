
import tkinter as tk

class CalculatorApp():
    
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.frame.pack()
        self.num_var = tk.StringVar()
        self.buttonsAndEntries()
        self.operation = ''

    
    def buttonsAndEntries(self):
        self.entry = tk.Entry(self.frame, bg='powder blue', insertwidth=4, justify='right', bd=10, textvariable=self.num_var, state=tk.DISABLED).grid(columnspan=4)
        #First Row.
        self.one   = tk.Button(self.frame, text='1', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('1')).grid(row=1, column=0) 
        self.two   = tk.Button(self.frame, text='2', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('2')).grid(row=1, column=1) 
        self.three = tk.Button(self.frame, text='3', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('3')).grid(row=1, column=2)
        self.add   = tk.Button(self.frame, text='+', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('+')).grid(row=1, column=3)
        #Second Row.
        self.four  = tk.Button(self.frame, text='4', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('4')).grid(row=2, column=0) 
        self.five  = tk.Button(self.frame, text='5', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('5')).grid(row=2, column=1) 
        self.six   = tk.Button(self.frame, text='6', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('6')).grid(row=2, column=2) 
        self.sub   = tk.Button(self.frame, text='-', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('-')).grid(row=2, column=3)
        #Third Row.
        self.seven = tk.Button(self.frame, text='7', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('7')).grid(row=3, column=0) 
        self.eight = tk.Button(self.frame, text='8', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('8')).grid(row=3, column=1) 
        self.nine  = tk.Button(self.frame, text='9', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('9')).grid(row=3, column=2)  
        self.mul   = tk.Button(self.frame, text='*', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('*')).grid(row=3, column=3)
        #Fourth Row
        self.zero  = tk.Button(self.frame, text='0', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('0')).grid(row=4, column=0)       
        self.clear = tk.Button(self.frame, text='C', bg='light green', bd=10, padx=15, pady=15, command=self.clearCallBack).grid(row=4, column=1)
        self.equal = tk.Button(self.frame, text='=', bg='light green', bd=10, padx=15, pady=15, command=self.evaluateOperation).grid(row=4, column=2)
        self.div   = tk.Button(self.frame, text='/', bg='light green', bd=10, padx=15, pady=15, command=lambda:self.callBackFunction('/')).grid(row=4, column=3) 
        
        
    def callBackFunction(self, operation):
        self.operation += operation
        self.num_var.set(self.operation)
    
    def clearCallBack(self):
        self.operation = ''
        self.num_var.set(self.operation)
    
    def evaluateOperation(self):
        self.operation = str(eval(self.operation))
        self.num_var.set(self.operation)
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title="Calculator"
    CalculatorApp(root)
    root.mainloop()
