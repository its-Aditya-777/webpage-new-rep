import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GitAutoPushHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the modified file is students.csv
        if event.src_path.endswith("students.csv"):
            print(f"{event.src_path} has been modified. Committing and pushing changes...")
            os.system("git add students.csv")
            os.system('git commit -m "Auto-update students.csv"')
            os.system("git push origin main")  

if __name__ == "__main__":
    # Path to monitor, current directory ("")
    path = "C:/Users/aditya verma/Desktop/Adi_webpage"
    event_handler = GitAutoPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped monitoring.")
    observer.join()
