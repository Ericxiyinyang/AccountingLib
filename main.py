from excel_sum import Excel_Reader
from tqdm import tqdm
from time import sleep
import art

class MasterTool:
    def __init__(self):
        self.version = 1

    def interactionLoop(self):
        print("Select your tool:")
        print("1. ExcelSum")
        self.userin = input()
        if self.userin == "1" or self.userin == "one" or self.userin == "One":
            self.ExcelSum()

    def ExcelSum(self):
        print("Input file name:")
        self.ExcelSumApp = Excel_Reader(input())
        for i in tqdm(range(100), desc="Loading Excel File"):
            sleep(0.005)
        print("Excel file loaded!")
        print("Select functions to use:")
        print("1. Get column(up-down) w/ sep, 2. Get row(left-right) w/ sep, 3. X-section data")
        if input() == "1" or self.userin == "one" or self.userin == "One":
            print("Enter column name")
            self.ExcelSumApp.getColumnWithSep(input())
        elif input() == "2" or self.userin == "two" or self.userin == "Two":
            print("Enter row name")
            self.ExcelSumApp.getRowWithSep(input())
        elif input() == "3" or self.userin == "three" or self.userin == "Three":
            print("Enter row name")
            self.rowname = input()
            print("Enter column name")
            self.colname = input()
            self.ExcelSumApp.getXSection(self.rowname, self.colname)


if __name__ == '__main__':
    for i in tqdm(range(100), desc="Loading Software"):
        sleep(0.005)
    AccLib = MasterTool()
    art.tprint("AccLib!")
    sleep(0.7)
    print(f"Version{1}, by Eric Yang")
    sleep(0.6)
    isUsing = True
    while isUsing:
        AccLib.interactionLoop()
        print("Continue using? (y/n)")
        if input() == "n":
            isUsing = False
    print("THANK YOU FOR USING ACCLIB :)")


