import json
import sys
import subprocess
import os
import tkinter as tk
from tkinter import messagebox


"""Script which creates virtual environments from a JSON file. """

class VirtualEnvApp:

    def __init__(self):
        with open("Envs.json", "r") as read_file:
            self.EnvironmentsData = json.load(read_file)
            self.EnvironmentName = None


    def CreateEnv(self, EnvironmentName):
        """ Function which takes the name of Env as input and adds env
            To the JSON"""

        self.EnvironmentsData[EnvironmentName] = f"workon {EnvironmentName}"
        with open("Envs.json", "w") as write_file:
            json.dump(self.EnvironmentsData, write_file, indent=4)
        subprocess.call(['mkvirtualenv',f'{EnvironmentName}'], shell=True)


    def StartEnv(self, EnvironmentName):
        """Function which starts the virtual environment in the command promt."""

        with open("Envs.json", "r") as read_file:
            self.Environments = json.load(read_file)
            SelectedEnv = self.Environments[EnvironmentName]
        os.system(f'start cmd /k "{SelectedEnv}"')


    def EndEnv(self,EnvironmentName):
        """Function which removes the environment from the system and the JSON file."""

        subprocess.call(['rmdir','/Q','/S',f'{EnvironmentName}'], shell=True, cwd=r"C:\Users\caspe\Envs")

        with open("Envs.json") as delete_file:
            elements = json.load(delete_file)

            if EnvironmentName in elements:
                del elements[EnvironmentName]

        with open("Envs.json", "w") as add_file:
            json.dump(elements, add_file, indent=4)


"""Class for the GUI of the Virtual ENV manager"""

class ENVGUI(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.widget()


    def widget(self):

        tk.Label(self, text="Virtual ENV").grid(row=1)

        self.input = tk.Entry(self, width=100)
        self.input.grid(row=1, column=2)

        self.add_button = tk.Button(self)
        self.add_button["text"] = "Create Environment"
        self.add_button['command'] = self.CreateEnv
        self.add_button.grid(row=1,column=3)

        with open("Envs.json", "r") as read_file:
            self.EnvironmentsObjects = json.load(read_file)


        for index, elements in enumerate(self.EnvironmentsObjects):

            # Create the labels in from of the elements
            self.label = tk.Label(self)
            self.label["text"] = elements
            self.label.grid(row=index+2)

            # Create the start button
            self.start = tk.Button(self)
            self.start["text"] = 'Start'
            self.start['command'] = self.StartEnv
            self.start.grid(row=index+2,column=2)

            # Create the delete button
            self.delete = tk.Button(self)
            self.delete["text"] = "Delete"
            self.delete["command"] = self.DeleteEnv
            self.delete.grid(row=index+2,column=3)


    def StartEnv(self):
        """ Function that is called to start the selected ENV """
        if len(self.input.get()) > 0:
            VirtualEnvApp().StartEnv(self.input.get())
            self.restart_program()
        else:
            messagebox.showinfo('Error', 'Please Enter the Name of the ENV')


    def DeleteEnv(self):
        """ Function that is called to delete the selected ENV """
        if len(self.input.get()) > 0:
            VirtualEnvApp().EndEnv(self.input.get())
            self.restart_program()
        else:
            messagebox.showinfo('Error', 'Please Enter the Name of the ENV')


    def CreateEnv(self):
        """ Function that is called to create the selected ENV """
        if len(self.input.get()) > 0:
            VirtualEnvApp().CreateEnv(self.input.get())
            self.restart_program()
        else:
            messagebox.showinfo('Error', 'Please Enter the Name of the ENV')

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)

if __name__ == '__main__':
    root = tk.Tk()
    app = ENVGUI(master=root)
    app.mainloop()
