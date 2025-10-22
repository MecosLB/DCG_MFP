from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time 

class Watcher:
    """
    Our Watcher class.

    Attributes:
        watch_path (str): Path to be monitored for new files.
        processor (Processor): Processor object.
    """
    def __init__(self, watch_path, processor):
        """
        Initializes a Watcher object setting the initial values.
        """
        self.watch_path = watch_path
        self.processor = processor
    
    # Start observing
    def start(self):
        """
        Starts the observation process by creating an Observer instance for the specified path.

        Returns:
            None.
        """
        event_handler = self._Handler(self.processor)
        observer = Observer()
        observer.schedule(event_handler, self.watch_path, recursive=True)
        observer.start()
        print(f"=====| Watching directory: {self.watch_path} |=====")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            
        observer.join()
    
    class _Handler(FileSystemEventHandler):
        """
        Our protected Handler class that inherits from FileSystemEventHandler class.

        Attributes:
            processor (Processor): Processor object.
        """
        def __init__(self, processor):
            """
            Initializes a _Handler object setting the initial values.
            """
            self.processor = processor
                
        def on_created(self, event):
            """
            Processes a file when a new file is created within the specified directory and its file extension is .csv

            Parameters:
                event (obj): Event object triggered.
                
            Returns:
                None.
            """
            if not event.is_directory and event.src_path.endswith('.csv'):
                print(f"=====| New file detected: {event.src_path} |=====")
                self.processor.process(event.src_path)