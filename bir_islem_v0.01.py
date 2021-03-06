__auther__="Fatih Fidan"
__version__="0.01"
__email__="fatihfidan52@gmail.com"

from tkinter import *
from random import randint,choice

class ForLoopBreak (Exception):
    pass

class Operation (Frame):

    def __init__(self,root):
        Frame.__init__ (self)
        self.root=root
        self.inputs=['' for _ in range (6)]
        self.target=''

        # Frames
        self.entryPage=Frame (self.root)
        self.mainPage=Frame (self.root)

        self.defines ()
        self.entry_page ()

    def defines(self):
        ######################################################################
        # entry_page
        self.header=Label (self.entryPage,
                           text = "Bir_Islem_v.01",
                           font = "Ariel 15 bold normal")

        self.button_start=Button (self.entryPage,
                                  text = "Start",
                                  anchor = "center",
                                  height = 3,width = 20,
                                  command = self.main_page)

        self.button_exit=Button (self.entryPage,
                                 text = "Exit",
                                 anchor = "center",
                                 height = 3,width = 20,
                                 command = self.root.destroy)

        #######################################################################

        # main_page
        self.header_1=Label (self.mainPage,text = "Numbers",height = 1,font = "Ariel 12 bold normal")

        self.number_1=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_1 .insert(END, str(self.inputs[0]))

        self.number_2=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_2.insert(END, str(self.inputs[1]))

        self.number_3=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_3.insert(END, str(self.inputs[2]))

        self.number_4=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_4.insert(END, str(self.inputs[3]))

        self.number_5=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_5.insert(END, str(self.inputs[4]))

        self.number_6=Entry (self.mainPage,fg = 'black',bg = 'grey',font = "Ariel 15 bold normal",width = 3)
        # self.number_6.insert(END, str(self.inputs[5]))

        self.header_2=Label (self.mainPage,text = "Target",height = 1,font = "Ariel 12 bold normal")
        self.number_target=Entry (self.mainPage,fg = 'black',bg = 'mediumseagreen',font = "Ariel 15 bold normal",width = 4)
        # self.number_target.insert(END, str(self.target))

        self.button_generate=Button (self.mainPage,
                                     text = "Generate",
                                     fg = 'black',bg = 'royalblue',
                                     font = "Ariel 12 bold normal",
                                     anchor = "center",
                                     height = 3,width = 7,
                                     command = lambda: [self.generate_input ()])

        self.button_solve=Button (self.mainPage,
                                  text = "Solve",
                                  fg = 'black',bg = 'mediumseagreen',
                                  font = "Ariel 12 bold normal",
                                  anchor = "center",
                                  height = 3,width = 7,
                                  command = lambda :[self.solve(),self.show_result()])

        self.button_exit2=Button (self.mainPage,
                                  text = "Exit",
                                  fg = 'black',bg = 'indianred',
                                  font = "Ariel 12 bold normal",
                                  anchor = "center",
                                  height = 3,width = 7,
                                  command = self.root.destroy)

        self.result_label = Label (self.mainPage,height = 2,font = "Ariel 12 bold normal")

    def show_result(self):
        self.result_label.config (text = self.result)

    def validate(self, opr,tar,r):
        if (r == 0) and (int (eval (opr)) == int(tar)):
            self.result = 'Direct Hit..!\n'+opr+"="+tar
            raise ForLoopBreak ()
        elif (r == 1) and (abs (int (eval (opr))-int(tar)) == 1):
            self.result= '1 approx!\n'+opr+"="+tar
            raise ForLoopBreak ()
        elif (r == 2) and (abs (int (eval (opr))-int(tar)) == 2):
            self.result= '2 approx!\n'+opr+"="+tar
            raise ForLoopBreak ()
        elif (r == 3) and (abs (int (eval (opr))-int(tar)) == 3):
            self.result= '3 approx!\n'+opr+"="+tar
            raise ForLoopBreak ()
        # else:
        #     self.result= 'No result!'
        #     raise ForLoopBreak ()

    def solve(self):
        nums=[self.number_1.get(),
              self.number_2.get(),
              self.number_3.get(),
              self.number_4.get(),
              self.number_5.get(),
              self.number_6.get()]
        tar=self.number_target.get()

        try:
            for r in range (4):
                ########## 1 #############
                for n1 in nums:
                    opr=n1
                    self.validate (opr,tar,r)

                ########## 2 ###########
                for n1 in nums:
                    nums1=nums.copy ()
                    nums1.remove (n1)
                    for op1 in "+-*/":
                        for n2 in nums1:
                            opr=n1+op1+n2
                            self.validate (opr,tar,r)

                ##########  3  ############
                for n1 in nums:
                    nums1=nums.copy ()
                    nums1.remove (n1)
                    for op1 in "+-*/":
                        for n2 in nums1:
                            nums2=nums1.copy ()
                            nums2.remove (n2)
                            for op2 in "+-*/":
                                for n3 in nums2:
                                    opr="("+n1+op1+n2+")"+op2+n3
                                    self.validate (opr,tar,r)

                ##########  4  ############
                for n1 in nums:
                    nums1=nums.copy ()
                    nums1.remove (n1)
                    for op1 in "+-*/":
                        for n2 in nums1:
                            nums2=nums1.copy ()
                            nums2.remove (n2)
                            for op2 in "+-*/":
                                for n3 in nums2:
                                    nums3=nums2.copy ()
                                    nums3.remove (n3)
                                    for op3 in "+-*/":
                                        for n4 in nums3:
                                            opr="(("+n1+op1+n2+")"+op2+n3+")"+op3+n4
                                            self.validate (opr,tar,r)

                ##########  5  ############
                for n1 in nums:
                    nums1=nums.copy ()
                    nums1.remove (n1)
                    for op1 in "+-*/":
                        for n2 in nums1:
                            nums2=nums1.copy ()
                            nums2.remove (n2)
                            for op2 in "+-*/":
                                for n3 in nums2:
                                    nums3=nums2.copy ()
                                    nums3.remove (n3)
                                    for op3 in "+-*/":
                                        for n4 in nums3:
                                            nums4=nums3.copy ()
                                            nums4.remove (n4)
                                            for op4 in "+-*/":
                                                for n5 in nums4:
                                                    opr="(((("+n1+op1+n2+")"+op2+n3+")"+op3+n4+")"+op4+n5+")"
                                                    self.validate (opr,tar,r)
                ##########  6  ############
                for n1 in nums:
                    nums1=nums.copy ()
                    nums1.remove (n1)
                    for op1 in "+-*/":
                        for n2 in nums1:
                            nums2=nums1.copy ()
                            nums2.remove (n2)
                            for op2 in "+-*/":
                                for n3 in nums2:
                                    nums3=nums2.copy ()
                                    nums3.remove (n3)
                                    for op3 in "+-*/":
                                        for n4 in nums3:
                                            nums4=nums3.copy ()
                                            nums4.remove (n4)
                                            for op4 in "+-*/":
                                                for n5 in nums4:
                                                    nums5=nums4.copy ()
                                                    nums5.remove (n5)
                                                    for op5 in "+-*/":
                                                        for n6 in nums5:
                                                            opr="((((("+n1+op1+n2+")"+op2+n3+")"+op3+n4+")"+op4+n5+")"+op5+n6+")"
                                                            self.validate (opr,tar,r)

                else:
                    self.result= 'No result!'
                    raise ForLoopBreak ()
        except ForLoopBreak:
            pass

    def entry_page(self):
        self.entryPage.grid (row = 0,column = 0)
        self.header.grid (row = 0,column = 0,rowspan = 2,columnspan = 4,pady = 25,padx = 100)
        self.button_start.grid (row = 4,column = 1,rowspan = 2,columnspan = 3,padx = 100,pady = 10)
        self.button_exit.grid (row = 6,column = 1,rowspan = 2,columnspan = 3,padx = 100,pady = 10)

    def main_page(self):
        self.entryPage.grid_remove ()

        self.mainPage.grid (row = 0,column = 0)

        self.header_1.grid (row = 0,column = 0,columnspan = 7,padx = 4,pady = 15)
        self.header_2.grid (row = 0,column = 7,padx = 15,pady = 15)

        self.number_1.grid (row = 1,column = 1,padx = 4,pady = 0)
        self.number_2.grid (row = 1,column = 2,padx = 4,pady = 0)
        self.number_3.grid (row = 1,column = 3,padx = 4,pady = 0)
        self.number_4.grid (row = 1,column = 4,padx = 4,pady = 0)
        self.number_5.grid (row = 1,column = 5,padx = 4,pady = 0)
        self.number_6.grid (row = 1,column = 6,padx = 4,pady = 0)
        self.number_target.grid (row = 1,column = 7,padx = 15,pady = 0)
        self.button_generate.grid (row = 2,column = 1,columnspan = 2,padx = 0,pady = 25)
        self.button_solve.grid (row = 2,column = 3,columnspan = 2,padx = 0,pady = 25)
        self.button_exit2.grid (row = 2,column = 5,columnspan = 2,padx = 0,pady = 25)
        self.result_label.grid (row = 3,column = 2,rowspan=1, columnspan = 5,padx = 0,pady = 10)

    def generate_input(self):
        numbers=[]
        for i in range (6):
            if i < 3:
                numbers.append (randint (1,10))
            elif i < 5:
                numbers.append (randint (6,15))
            else:
                numbers.append (choice ([25,40,50,50,50,60,75,75,75,80,90,100,100,100]))
        numbers.sort ()
        self.inputs=numbers
        self.target=randint (101,999)

        self.number_1.delete (0,END)
        self.number_2.delete (0,END)
        self.number_3.delete (0,END)
        self.number_4.delete (0,END)
        self.number_5.delete (0,END)
        self.number_6.delete (0,END)
        self.number_target.delete (0,END)

        self.number_1.insert (END,str (self.inputs[0]))
        self.number_2.insert (END,str (self.inputs[1]))
        self.number_3.insert (END,str (self.inputs[2]))
        self.number_4.insert (END,str (self.inputs[3]))
        self.number_5.insert (END,str (self.inputs[4]))
        self.number_6.insert (END,str (self.inputs[5]))
        self.number_target.insert (END,str (self.target))

if __name__ == "__main__":
    root=Tk ()
    root.title ("TRT")
    root.geometry ("355x300")
    obj=Operation (root)
    root.mainloop ()
