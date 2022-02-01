from datetime import date

class InsertDefault:
    def __init__(self, obj):
        self.obj = obj

    # Method inserting default value to the entry
    def insert_default_value_to_entry(self):
        # inserting current date/month/year to the date entry
        # Month abbreviation, day and year
        self.today = date.today()
        self.dateEntry = self.today.strftime("%b-%d-%Y")
        self.obj.entry7.insert(0, self.dateEntry)

        # FOR TESTING
        # self.obj.entry0.insert(0, "C:/Users/lenovo/Downloads/Test.xlsx")
        # self.obj.entry1.insert(0, "")
        # self.obj.entry2.insert(0, "Sheet1")
        # self.obj.entry3.insert(0, "A")
        # self.obj.entry4.insert(0, "B")
        # self.obj.entry5.insert(0, 1)
        # self.obj.entry6.insert(0, .20)