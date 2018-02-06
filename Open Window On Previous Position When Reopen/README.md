Python3
------------------------------------------------------------------------------------------
**This python program is for saving the current tkinter location on close.
let tkinter window open at position 200x200 and we shift it on any place let 278x578 than
if we close that window than after open again it should be on 278x578 position.**
------------------------------------------------------------------------------------------

root=Tk()

----------------------------------------------------------------------------------
root.geometry("500x500+A+B") **#Here A and B are position where window will open**

---------------------------------------------------------------------------------
we use for current tkinter window position we can use **root.winfo_x()** and **root.winfo_y()** which is A and B.

Devloper:- **Bharat Rawat**
