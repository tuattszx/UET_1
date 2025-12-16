# import thu vien
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data import StudentManager

class MainApp:
    def __init__(self, master):
        self.master = master
        self.studentManager = StudentManager()
        self.HEIGHT = 480
        self.WIDTH = 720
        self.FONT = ('Arial', 12, 'bold')
        self.COL = ["ID", "MSV" ,"Tên SV", "Lớp", "Điểm GT", "Điểm ĐSTT", "Điểm TDTT", "Điểm TTHCM"]
        self.COLWIDTH = {'ID': 20, 'Tên SV': 150, 'Lớp': 50, 'MSV': 65, 'Điểm GT': 65, 'Điểm ĐSTT': 65, 'Điểm TDTT': 65, 'Điểm TTHCM': 65} 
        self.fields = ["MSV", "Tên SV", "Lớp", "Điểm GT", "Điểm ĐSTT", "Điểm TDTT", "Điểm TTHCM"]
        self.root = master
        self.createWidgets()
        
        #entries
        self.addStudentEntries = {} 
        self.deleteStudentEntries = {}
        self.searchStudentEntries = {}
        self.updateStudentEntries = {}
        
        # khoi tao frame
        self.mainFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.addStudentFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.deleteStudentFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.searchStudentFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.updateStudentFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT)
        self.displayAllFrame = tk.Frame(self.root, bg='white', width=self.WIDTH, height=self.HEIGHT) 
        
        # cau hinh frame
        self.mainFrame.pack_propagate(False) 
        self.addStudentFrame.pack_propagate(False)
        self.deleteStudentFrame.pack_propagate(False)
        self.searchStudentFrame.pack_propagate(False)
        self.updateStudentFrame.pack_propagate(False)
        self.displayAllFrame.pack_propagate(False)
        
        # goi cac ham
        self.mainMenu()
        self.createAddStudentForm()
        self.createDeleteStudentForm()
        self.createSearchStudentForm()
        self.createUpdateStudentForm()

        self.showFrame(self.mainFrame)
        
    def createWidgets(self):
        self.root.title("Quản Lý Sinh Viên")
        self.root.config(bg="skyblue")
        self.root.resizable(0, 0)
        labelTitle = tk.Label(self.root, text= "Quản Lý Sinh Viên", font=('Arial', 17, 'bold'), bg='skyblue')
        labelTitle.pack(side=tk.TOP, pady=10)
        
    def showFrame(self, frameShow):
        self.mainFrame.pack_forget()
        self.addStudentFrame.pack_forget()
        self.searchStudentFrame.pack_forget()
        self.updateStudentFrame.pack_forget()
        self.deleteStudentFrame.pack_forget()
        self.displayAllFrame.pack_forget()
        frameShow.pack(padx=20, pady=20)
        
    def mainMenu(self):
        BUTTON_WIDTH = 40
        butAdd = tk.Button(self.mainFrame,
                            text= "     1. Thêm Sinh Viên",
                            font= self.FONT,
                            command=lambda: self.showFrame(self.addStudentFrame),
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butAdd.pack(pady=5)

        butDelete = tk.Button(self.mainFrame,
                            text= "     2. Xoá Sinh Viên",
                            font= self.FONT,
                            command=lambda: self.showFrame(self.deleteStudentFrame),
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butDelete.pack(pady=5)

        butSearch = tk.Button(self.mainFrame,
                            text= "     3. Tìm Kiếm Sinh Viên Theo MSV",
                            font= self.FONT,
                            command=lambda: self.showFrame(self.searchStudentFrame),
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butSearch.pack(pady=5)

        butUpdate = tk.Button(self.mainFrame,
                            text= "     4. Cập Nhật Dữ Liệu Sinh Viên",
                            font= self.FONT,
                            command=lambda: self.showFrame(self.updateStudentFrame),
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butUpdate.pack(pady=5)

        butDisplay = tk.Button(self.mainFrame,
                            text= "     5. Hiển Thị Toàn Bộ Sinh Viên",
                            font= self.FONT,
                            command= self.displayAll,
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butDisplay.pack(pady=5)

        butClear = tk.Button(self.mainFrame,
                            text= "     6. Xoá Tất Cả Sinh Viên",
                            font= self.FONT,
                            command= self.clearDataBase,
                            width= BUTTON_WIDTH,
                            height= 2,
                            anchor='w')
        butClear.pack(pady=5)

        butExit = tk.Button(self.mainFrame,
                            text="Thoát",
                            font= self.FONT,
                            command=self.Exit, 
                            width= 10,  
                            height= 1,
                            bg= "grey",
                            fg= "black")
        butExit.pack(side=tk.BOTTOM, pady=20)
    
    def createAddStudentForm(self):
        formFrame = tk.Frame(self.addStudentFrame, bg='white', padx=10, pady=10)
        formFrame.pack(pady=20)       

        for i, field_name in enumerate(self.fields):
            label = tk.Label(formFrame, text=field_name, bg='white', anchor='w', width=15, font= self.FONT)
            label.grid(row=i + 1, column=0, pady=5, sticky='w')
            entry = tk.Entry(formFrame, width=40)
            entry.grid(row=i + 1, column=1, pady=5, padx=10,)
            self.addStudentEntries[field_name] = entry
        buttonContainer = tk.Frame(self.addStudentFrame, bg='white')
        buttonContainer.pack(pady=10)
        
        backButton = tk.Button(buttonContainer,
                                text="Trở lại",
                                font= self.FONT,
                                command=lambda: self.showFrame(self.mainFrame),
                                bg='lightblue',
                                fg='black',
                                width=15) 
        backButton.pack(side=tk.LEFT, padx=10)
        submitButton = tk.Button(buttonContainer,
                                text="Xác nhận", 
                                font= self.FONT,
                                command=self.addSubmit,
                                bg='green',
                                fg='white',
                                width=15) 
        submitButton.pack(side=tk.LEFT, padx=10) 
    
    def createDeleteStudentForm(self):
        formFrame = tk.Frame(self.deleteStudentFrame, bg='white', padx=10, pady=10)
        formFrame.pack(pady=20)
        field_name = "MSV: "
        label = tk.Label(formFrame, text=field_name, bg='white', anchor='w', width=15, font= self.FONT)
        label.grid(row=1, column=0, pady=5, sticky='w')
        entry = tk.Entry(formFrame, width=30)
        entry.grid(row=1, column=1, pady=5, padx=10)
        self.deleteStudentEntries[field_name] = entry 
        
        buttonContainer = tk.Frame(self.deleteStudentFrame, bg='white')
        buttonContainer.pack(pady=10)
        backButton = tk.Button(buttonContainer,
                                text="Trở lại",
                                font= self.FONT,
                                command=lambda: self.showFrame(self.mainFrame),
                                bg='lightblue',
                                fg='black',
                                width=15) 
        backButton.pack(side=tk.LEFT, padx=10)
        submitButton = tk.Button(buttonContainer,
                                text="Xác nhận", 
                                font= self.FONT,
                                command=self.deleteSubmit,
                                bg='green',
                                fg='white',
                                width=15) 
        submitButton.pack(side=tk.LEFT, padx=10) 
    
    def createSearchStudentForm(self):
        formFrame = tk.Frame(self.searchStudentFrame, bg='white', padx=10, pady=10)
        formFrame.pack(pady=20)
        label = tk.Label(formFrame, text="MSV", bg='white', anchor='w', width=15, font= self.FONT)
        label.grid(row=1, column=0, pady=5, sticky='w')
        entry = tk.Entry(formFrame, width=30)
        entry.grid(row=1, column=1, pady=5, padx=10)
        self.searchStudentEntries["MSV"] = entry
        
        buttonContainer = tk.Frame(self.searchStudentFrame, bg='white')
        buttonContainer.pack(pady=10)
        backButton = tk.Button(buttonContainer,
                                text="Trở lại",
                                font= self.FONT,
                                command=lambda: [self.clearSearch(), self.showFrame(self.mainFrame)],
                                bg='lightblue',
                                fg='black',
                                width=15) 
        backButton.pack(side=tk.LEFT, padx=10)
        submitButton = tk.Button(buttonContainer,
                                text="Xác nhận", 
                                font= self.FONT,
                                command=self.searchSubmit,
                                bg='green',
                                fg='white',
                                width=15) 
        submitButton.pack(side=tk.LEFT, padx=10) 
    
    def createUpdateStudentForm(self):
        formFrame = tk.Frame(self.updateStudentFrame, bg='white', padx=10, pady=10)
        formFrame.pack(pady=20)
        tableContainer = tk.Frame(self.updateStudentFrame, bg='white')
        tableContainer.pack(pady=10, padx=10, fill='both', expand=True)
        tk.Label(tableContainer, text="Lưu ý: MSV bắt buộc phải nhập, các phần còn lại có thể nhập hoặc không", fg='yellow', bg='grey').pack(pady=10) 

        for i, field_name in enumerate(self.fields):
            label = tk.Label(formFrame, text=field_name, bg='white', anchor='w', width=15, font= self.FONT)
            label.grid(row=i + 1, column=0, pady=5, sticky='w')
            entry = tk.Entry(formFrame, width=40)
            entry.grid(row=i + 1, column=1, pady=5, padx=10,)
            self.updateStudentEntries[field_name] = entry
        buttonContainer = tk.Frame(self.updateStudentFrame, bg='white')
        buttonContainer.pack(pady=10)
        
        backButton = tk.Button(buttonContainer,
                                text="Trở lại",
                                font= self.FONT,
                                command=lambda: self.showFrame(self.mainFrame),
                                bg='lightblue',
                                fg='black',
                                width=15) 
        backButton.pack(side=tk.LEFT, padx=10)
        submitButton = tk.Button(buttonContainer,
                                text="Xác nhận", 
                                font= self.FONT,
                                command=self.updateSubmit,
                                bg='green',
                                fg='white',
                                width=15) 
        submitButton.pack(side=tk.LEFT, padx=10) 

    def checkScore(self, score):
        return 0 <= score <= 10

    def addSubmit(self):
        msv = self.addStudentEntries["MSV"].get()
        ten = self.addStudentEntries["Tên SV"].get()
        lop = self.addStudentEntries["Lớp"].get()
        try:
            gt = float(self.addStudentEntries["Điểm GT"].get())
            dstt = float(self.addStudentEntries["Điểm ĐSTT"].get())
            tdtt = float(self.addStudentEntries["Điểm TDTT"].get())
            tthcm = float(self.addStudentEntries["Điểm TTHCM"].get())
            if self.checkScore(gt) and self.checkScore(dstt) and self.checkScore(tdtt) and self.checkScore(tthcm):
                if self.studentManager.addStudent(msv, ten, lop, gt, dstt, tdtt, tthcm):
                    messagebox.showinfo(message= "Thêm Sinh Viên Thành Công!")
                    for entry in self.addStudentEntries.values():
                        entry.delete(0, tk.END)
                else:
                    messagebox.showerror(message= "MSV Đã Tồn Tại!")
            else:
                messagebox.showerror(message= "Điểm không hợp lệ!")
        except ValueError:
            messagebox.showerror(message= "Điểm không hợp lệ!")

    def deleteSubmit(self):
        msv = self.deleteStudentEntries["MSV: "].get()
        if self.studentManager.deleteStudent(msv):
            messagebox.showinfo(message= "Xoá Sinh Viên Thành Công!")
        else:
            messagebox.showerror(message= "MSV Không Tồn Tại!")
        for entry in self.deleteStudentEntries.values():
            entry.delete(0, tk.END)
    
    def clearSearch(self):
        for widget in self.searchStudentFrame.winfo_children():
            if widget.winfo_name() == 'result_container':
                widget.destroy()
        for entry in self.searchStudentEntries.values():
            entry.delete(0, tk.END)

    def searchSubmit(self):
        msv = self.searchStudentEntries["MSV"].get()
        if not msv:
            messagebox.showerror(message= "Vui lòng nhập MSV!")
            return

        results = self.studentManager.searchStudentById(msv)
        
        if not results:
            messagebox.showerror(message= "MSV Không Tồn Tại!")
        else:
            tableContainer = tk.Frame(self.searchStudentFrame, bg='white', name='result_container')
            tableContainer.pack(pady=10, padx=10, fill='x')
            self.searchTree = ttk.Treeview(tableContainer, columns= self.COL, show='headings', height=1)  
            for col in self.COL:
                self.searchTree.heading(col, text=col.upper())
                self.searchTree.column(col, width=self.COLWIDTH.get(col, 80), anchor='center')
            for row in results:
                self.searchTree.insert('', tk.END, values=row)
            self.searchTree.pack(fill='x', expand=True)
            messagebox.showinfo(message= "Tìm Kiếm Thành Công!")
    
    def checkScoreUpdate(self, score):
        if score == None:
            return True
        score = float(score)
        return 0 <= score <= 10

    def updateSubmit(self):
        msv = self.updateStudentEntries["MSV"].get()
        ten = self.updateStudentEntries["Tên SV"].get()
        lop = self.updateStudentEntries["Lớp"].get()
        gt = self.updateStudentEntries["Điểm GT"].get()
        dstt = self.updateStudentEntries["Điểm ĐSTT"].get()
        tdtt = self.updateStudentEntries["Điểm TDTT"].get()
        tthcm = self.updateStudentEntries["Điểm TTHCM"].get()
        if not ten:   ten = None
        if not lop:   lop = None
        if not gt:   gt = None
        if not dstt:   dstt = None
        if not tdtt:   tdtt = None
        if not tthcm:   tthcm = None
        if (self.studentManager.searchStudentById(msv) == []):
            messagebox.showerror(message= "MSV Không Tồn Tại!")
        else:
            if self.checkScoreUpdate(gt) and self.checkScoreUpdate(dstt) and self.checkScoreUpdate(tdtt) and self.checkScoreUpdate(tthcm):
                if self.studentManager.updateStudent(msv, ten, lop, gt, dstt, tdtt, tthcm):
                    messagebox.showinfo(message= "Cập Nhật Sinh Viên Thành Công!")
                else:
                    messagebox.showerror(message= "MSV Không Tồn Tại!")
            else:
                messagebox.showerror(message= "Điểm không hợp lệ!")
            for entry in self.updateStudentEntries.values():
                entry.delete(0, tk.END)
    
    def clearDataBase(self):
        confirm = messagebox.askyesno(message= "Xác nhận Xoá Dữ Liệu Sinh Viên")
        if confirm:
            self.studentManager.clearDataBase()
            self.mainFrame
        
    def displayAll(self):
        for widget in self.displayAllFrame.winfo_children():
            widget.destroy()
            
        data = self.studentManager.getAllStudents()

        tableContainer = tk.Frame(self.displayAllFrame)
        tableContainer.pack(pady=10, padx=10, fill='both', expand=True)

        self.tree = ttk.Treeview(tableContainer, columns= self.COL, show='headings', selectmode='browse') 
        
        for colName, width in self.COLWIDTH.items():
            self.tree.heading(colName, text=colName.upper())
            self.tree.column(colName, width=width, anchor='center') 

        if data:
            for row in data:
                self.tree.insert('', tk.END, values=row)
        else:
            tk.Label(tableContainer, text="Không có dữ liệu sinh viên nào.", fg='red').pack(pady=10) 
        scrY = ttk.Scrollbar(tableContainer, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrY.set)
        
        scrY.pack(side='right', fill='y')
        self.tree.pack(side='left', fill='both', expand=True)
        backButton = tk.Button(self.displayAllFrame,
                                text="Trở lại",
                                font= self.FONT,
                                command=lambda: self.showFrame(self.mainFrame),
                                bg='lightblue',
                                fg='black',
                                width=20)
        backButton.pack(pady=10)
        self.showFrame(self.displayAllFrame)
    
    def Exit(self):
        confirm = messagebox.askyesno(message= "Xác nhận Thoát")
        if confirm:
            self.studentManager.close_connection()
            self.root.destroy() 
        
    def main(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    app.main()