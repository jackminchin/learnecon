import sys
import time
import logging
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, LoggingEventHandler

import os

class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        os.system('jupyter-book build .')
        
        return super().on_any_event(event)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else './parts'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(Handler(), path, recursive=True )
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

