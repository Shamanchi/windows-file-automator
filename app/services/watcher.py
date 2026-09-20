import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from loguru import logger
from app.core.config import settings


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logger.info(f'New file: {event.src_path}')
            # Process file: convert, move, extract data, etc.

class FileWatcher:
    def __init__(self):
        self.observer = Observer()
        self.paths = settings.watch_paths
    
    async def start(self):
        logger.info(f'Watching paths: {self.paths}')
        for path in self.paths:
            self.observer.schedule(FileEventHandler(), path, recursive=True)
        self.observer.start()
    
    async def stop(self):
        self.observer.stop()
        self.observer.join()
        logger.info('File watcher stopped')