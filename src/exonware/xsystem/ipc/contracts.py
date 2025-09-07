"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: September 04, 2025

IPC module contracts - interfaces and enums for inter-process communication.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union, AsyncGenerator, Callable
from multiprocessing import Process


class IPCType(Enum):
    """IPC communication types."""
    PIPE = "pipe"
    QUEUE = "queue"
    SHARED_MEMORY = "shared_memory"
    SOCKET = "socket"
    FILE = "file"


class MessageType(Enum):
    """Message types."""
    DATA = "data"
    CONTROL = "control"
    HEARTBEAT = "heartbeat"
    ERROR = "error"
    SHUTDOWN = "shutdown"


class ProcessState(Enum):
    """Process states."""
    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


class QueueType(Enum):
    """Queue types."""
    FIFO = "fifo"
    LIFO = "lifo"
    PRIORITY = "priority"
    BOUNDED = "bounded"


class SharedMemoryType(Enum):
    """Shared memory types."""
    MMAP = "mmap"
    SHM = "shm"
    POSIX = "posix"
    WINDOWS = "windows"
    SYSTEM_V = "system_v"


class IMessageQueue(ABC):
    """Interface for message queue operations."""
    
    @abstractmethod
    async def put(self, message: Any, message_type: MessageType = MessageType.DATA) -> None:
        """Put message in queue."""
        pass
    
    @abstractmethod
    async def get(self, timeout: Optional[float] = None) -> Any:
        """Get message from queue."""
        pass
    
    @abstractmethod
    async def get_nowait(self) -> Any:
        """Get message without waiting."""
        pass
    
    @abstractmethod
    def empty(self) -> bool:
        """Check if queue is empty."""
        pass
    
    @abstractmethod
    def full(self) -> bool:
        """Check if queue is full."""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Get queue size."""
        pass


class IPipe(ABC):
    """Interface for pipe operations."""
    
    @abstractmethod
    async def send(self, data: Any) -> None:
        """Send data through pipe."""
        pass
    
    @abstractmethod
    async def recv(self, timeout: Optional[float] = None) -> Any:
        """Receive data from pipe."""
        pass
    
    @abstractmethod
    async def recv_nowait(self) -> Any:
        """Receive data without waiting."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close pipe."""
        pass
    
    @abstractmethod
    def closed(self) -> bool:
        """Check if pipe is closed."""
        pass


class ISharedMemory(ABC):
    """Interface for shared memory operations."""
    
    @abstractmethod
    def create(self, name: str, size: int) -> None:
        """Create shared memory segment."""
        pass
    
    @abstractmethod
    def attach(self, name: str) -> None:
        """Attach to shared memory segment."""
        pass
    
    @abstractmethod
    def detach(self) -> None:
        """Detach from shared memory segment."""
        pass
    
    @abstractmethod
    def unlink(self) -> None:
        """Unlink shared memory segment."""
        pass
    
    @abstractmethod
    def read(self, offset: int = 0, size: Optional[int] = None) -> bytes:
        """Read from shared memory."""
        pass
    
    @abstractmethod
    def write(self, data: bytes, offset: int = 0) -> None:
        """Write to shared memory."""
        pass


class IProcessManager(ABC):
    """Interface for process management."""
    
    @abstractmethod
    def create_process(self, target: Callable, args: tuple = (), kwargs: Optional[Dict] = None) -> Process:
        """Create new process."""
        pass
    
    @abstractmethod
    def start_process(self, process: Process) -> None:
        """Start process."""
        pass
    
    @abstractmethod
    def stop_process(self, process: Process, timeout: Optional[float] = None) -> None:
        """Stop process."""
        pass
    
    @abstractmethod
    def get_process_state(self, process: Process) -> ProcessState:
        """Get process state."""
        pass
    
    @abstractmethod
    def is_process_alive(self, process: Process) -> bool:
        """Check if process is alive."""
        pass


class IProcessPool(ABC):
    """Interface for process pool operations."""
    
    @abstractmethod
    def submit(self, func: Callable, *args, **kwargs) -> Any:
        """Submit task to pool."""
        pass
    
    @abstractmethod
    async def submit_async(self, func: Callable, *args, **kwargs) -> Any:
        """Submit async task to pool."""
        pass
    
    @abstractmethod
    def map(self, func: Callable, iterable: List[Any]) -> List[Any]:
        """Map function over iterable."""
        pass
    
    @abstractmethod
    async def map_async(self, func: Callable, iterable: List[Any]) -> List[Any]:
        """Map function over iterable asynchronously."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close process pool."""
        pass
    
    @abstractmethod
    def join(self) -> None:
        """Join all processes."""
        pass


# Aliases for backward compatibility
IPipeManager = IPipe
