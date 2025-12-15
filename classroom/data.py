from tkinter import messagebox
import sqlite3
class StudentManager:
    def __init__(self, db_name='data.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Students (
                    id INTEGER PRIMARY KEY,
                    msv TEXT UNIQUE NOT NULL,
                    ten TEXT NOT NULL,
                    lop TEXT NOT NULL,
                    gt REAL DEFAULT 0,
                    dstt REAL DEFAULT 0,
                    tdtt REAL DEFAULT 0,
                    tthcm REAL DEFAULT 0
                )
            ''')
            self.conn.commit()
            
        except sqlite3.Error as e:
            if self.conn:
                self.conn.close()
                self.conn = None
                self.cursor = None
    def close_connection(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
    def addStudent(self, msv, ten, lop, gt, dstt, tdtt, tthcm):
        if not self.conn:
            return False
        try:
            self.cursor.execute(
                "INSERT INTO Students (msv, ten, lop, gt, dstt, tdtt, tthcm) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (msv, ten, lop, gt, dstt, tdtt, tthcm)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        except sqlite3.Error as e:
            return False
    def deleteStudent(self, msv):
        if not self.conn:
            return False
        try:
            self.cursor.execute(
                "DELETE FROM Students WHERE msv = ?", 
                (msv,)
            )
            self.conn.commit()
            rows_deleted = self.cursor.rowcount
            if rows_deleted > 0:
                return True
        except sqlite3.Error as e:
            pass
        return False
    def searchStudentById(self, msv):
        if not self.conn:
            return []
        try:
            self.cursor.execute(
                "SELECT id, msv, ten, lop, gt, dstt, tdtt, tthcm FROM Students WHERE msv = ?", 
                (msv,)
            )
            results = self.cursor.fetchall()
            return results
        except sqlite3.Error as e:
            return []

    def updateStudent(self, msv, ten, lop, gt, dstt, tdtt, tthcm):
        if not self.conn:
            return False
        updates = []
        values = []

        if ten is not None:
            updates.append("ten = ?")
            values.append(ten)
        if lop is not None:
            updates.append("lop = ?")
            values.append(lop)
        if gt is not None:
            updates.append("gt = ?")
            values.append(gt)
        if dstt is not None:
                updates.append("dstt = ?")
                values.append(dstt)
        if tdtt is not None:
                updates.append("tdtt = ?")
                values.append(tdtt)
        if tthcm is not None:
                updates.append("tthcm = ?")
                values.append(tthcm)
        if not updates:
            return True 
        sql = f"UPDATE Students SET {', '.join(updates)} WHERE msv = ?"
        values.append(msv)

        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            if self.cursor.rowcount > 0:
                return True
            else:
                return False 
        except sqlite3.Error as e:
            return False

    def getAllStudents(self):
        if not self.conn:
            return []
        try:
            self.cursor.execute("SELECT id, msv, ten, lop, gt, dstt, tdtt, tthcm FROM Students ORDER BY id")
            results = self.cursor.fetchall()
            return results
        except sqlite3.Error as e:
            return []

    def clearDataBase(self):
        if not self.conn:
            return
        try:
            self.cursor.execute("DELETE FROM Students")
            self.conn.commit()
            self.cursor.execute("VACUUM")
            return True
        except sqlite3.Error as e:
            return False