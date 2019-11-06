import tkinter as tk

class GUI:

    "Views - everything user sees"

    def __init__(self):
        self.video_path = ''  # string file path
        # dictionary of key, val of key is string, val is int
        self.settings = {'conf': .9, 'poll': 5, 'anti': 5, 'search': [""]}
        self.job = None
        # this will be of class Job type, so not included in class diagram
        # but draw association arrow to Job Class

        # self.render()   # display GUI when this class instantiates

    def get_settings(self):
        # get settings currently in text boxes of GUI
        return {video: self.video_path, settings: self.settings}

    def set_settings(self, values, path):
        self.settings = values
        self.video_path = path
        # where values is a dictionary

    def start_job(self):
        self.job = Job(self.get_settings())

    def kill_job(self):
        self.job.kill()

    def render(self):
        # display GUI, including text fields, choose file, and start button
        # also calls set_settings and start_job when start button is pressed

        # win = tk.Tk()

        # win.title("Intravideo Search")

        # tk.Label(win, text="Upload a video.").pack()
        # tk.Button(win,text="Upload").pack()

        # tk.Label(win, text="Set recursion depth").pack()
        # tk.Button(win,text="Set").pack()

        # tk.Label(win, text="").pack()
        # tk.Button(win,text="Upload").pack()


        # win.mainloop()
        return 0
