# Command used to import tkinder framework
import tkinter as tk



# Determine your root file for making the framework
root = tk.Tk()

# Set the background to any colour
root.configure(bg="#F7DC06")

#Used to set the minimum size of you tkinder window
root.minsize(100, 500)


#Adds a Title to you tkinder window
root.title("Welcome to this tkinder tutorial")


# Adds Hello world statement to your program
label = tk.Label(root, text="hello, World!")
label.pack(padx=20, pady=20)    # Add padding on the x and y axis.



# add a rectange to you frame, use the .pack()  method to place it in you frame.
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

square = tk.Canvas(root, height=50, width=50, bg="#FFE300")
square.pack(side="left") # Keyword argument can include position or size


# Add a button your gui
Button = tk.Button(root, text="File", padx=100, pady=10, fg="white", bg="#263d42")
Button.pack()


Button2 = tk.Button(root, text="Run", padx=100, pady=10, fg="white", bg="#263d42")
Button2.pack()

# Important function, runs you program in a loop keeping it online
root.mainloop()

#Will destroy the program.
#root.destroy()
