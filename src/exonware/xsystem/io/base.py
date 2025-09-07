#exonware/xsystem/io/base.py
"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: September 04, 2025

IO module base classes - abstract classes for input/output functionality.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union, BinaryIO, TextIO
from pathlib import Path
from .contracts import FileMode, FileType, PathType, OperationResult, LockType


class AFileBase(ABC):
    """Abstract base class for file operations."""
    
    def __init__(self, file_path: Union[str, Path]):
        """
        Initialize file base.
        
        Args:
            file_path: Path to file
        """
        self.file_path = Path(file_path)
        self._handle: Optional[Union[BinaryIO, TextIO]] = None
        self._locked = False
    
    @abstractmethod
    def open(self, mode: FileMode = FileMode.READ) -> None:
        """Open file."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close file."""
        pass
    
    @abstractmethod
    def read(self, size: Optional[int] = None) -> Union[str, bytes]:
        """Read from file."""
        pass
    
    @abstractmethod
    def write(self, data: Union[str, bytes]) -> int:
        """Write to file."""
        pass
    
    @abstractmethod
    def seek(self, position: int, whence: int = 0) -> int:
        """Seek file position."""
        pass
    
    @abstractmethod
    def tell(self) -> int:
        """Get current file position."""
        pass
    
    @abstractmethod
    def flush(self) -> None:
        """Flush file buffer."""
        pass
    
    @abstractmethod
    def is_open(self) -> bool:
        """Check if file is open."""
        pass
    
    @abstractmethod
    def exists(self) -> bool:
        """Check if file exists."""
        pass
    
    @abstractmethod
    def size(self) -> int:
        """Get file size."""
        pass
    
    @abstractmethod
    def delete(self) -> bool:
        """Delete file."""
        pass


class ADirectoryBase(ABC):
    """Abstract base class for directory operations."""
    
    def __init__(self, dir_path: Union[str, Path]):
        """
        Initialize directory base.
        
        Args:
            dir_path: Path to directory
        """
        self.dir_path = Path(dir_path)
    
    @abstractmethod
    def create(self, parents: bool = True, exist_ok: bool = True) -> bool:
        """Create directory."""
        pass
    
    @abstractmethod
    def delete(self, recursive: bool = False) -> bool:
        """Delete directory."""
        pass
    
    @abstractmethod
    def exists(self) -> bool:
        """Check if directory exists."""
        pass
    
    @abstractmethod
    def list_files(self, pattern: Optional[str] = None, recursive: bool = False) -> List[Path]:
        """List files in directory."""
        pass
    
    @abstractmethod
    def list_directories(self, recursive: bool = False) -> List[Path]:
        """List subdirectories."""
        pass
    
    @abstractmethod
    def walk(self) -> List[tuple[Path, List[str], List[str]]]:
        """Walk directory tree."""
        pass
    
    @abstractmethod
    def get_size(self) -> int:
        """Get directory size."""
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """Check if directory is empty."""
        pass
    
    @abstractmethod
    def copy_to(self, destination: Union[str, Path]) -> bool:
        """Copy directory to destination."""
        pass
    
    @abstractmethod
    def move_to(self, destination: Union[str, Path]) -> bool:
        """Move directory to destination."""
        pass


class APathBase(ABC):
    """Abstract base class for path operations."""
    
    @abstractmethod
    def normalize(self, path: Union[str, Path]) -> Path:
        """Normalize path."""
        pass
    
    @abstractmethod
    def resolve(self, path: Union[str, Path]) -> Path:
        """Resolve path."""
        pass
    
    @abstractmethod
    def absolute(self, path: Union[str, Path]) -> Path:
        """Get absolute path."""
        pass
    
    @abstractmethod
    def relative(self, path: Union[str, Path], start: Optional[Union[str, Path]] = None) -> Path:
        """Get relative path."""
        pass
    
    @abstractmethod
    def join(self, *paths: Union[str, Path]) -> Path:
        """Join paths."""
        pass
    
    @abstractmethod
    def split(self, path: Union[str, Path]) -> tuple[Path, str]:
        """Split path into directory and filename."""
        pass
    
    @abstractmethod
    def get_extension(self, path: Union[str, Path]) -> str:
        """Get file extension."""
        pass
    
    @abstractmethod
    def get_stem(self, path: Union[str, Path]) -> str:
        """Get file stem (name without extension)."""
        pass
    
    @abstractmethod
    def get_name(self, path: Union[str, Path]) -> str:
        """Get file/directory name."""
        pass
    
    @abstractmethod
    def get_parent(self, path: Union[str, Path]) -> Path:
        """Get parent directory."""
        pass
    
    @abstractmethod
    def is_absolute(self, path: Union[str, Path]) -> bool:
        """Check if path is absolute."""
        pass
    
    @abstractmethod
    def is_relative(self, path: Union[str, Path]) -> bool:
        """Check if path is relative."""
        pass


class AStreamBase(ABC):
    """Abstract base class for stream operations."""
    
    def __init__(self):
        """Initialize stream base."""
        self._closed = False
        self._position = 0
    
    @abstractmethod
    def read(self, size: Optional[int] = None) -> Union[str, bytes]:
        """Read from stream."""
        pass
    
    @abstractmethod
    def write(self, data: Union[str, bytes]) -> int:
        """Write to stream."""
        pass
    
    @abstractmethod
    def seek(self, position: int, whence: int = 0) -> int:
        """Seek stream position."""
        pass
    
    @abstractmethod
    def tell(self) -> int:
        """Get current stream position."""
        pass
    
    @abstractmethod
    def flush(self) -> None:
        """Flush stream buffer."""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close stream."""
        pass
    
    @abstractmethod
    def is_closed(self) -> bool:
        """Check if stream is closed."""
        pass
    
    @abstractmethod
    def readable(self) -> bool:
        """Check if stream is readable."""
        pass
    
    @abstractmethod
    def writable(self) -> bool:
        """Check if stream is writable."""
        pass
    
    @abstractmethod
    def seekable(self) -> bool:
        """Check if stream is seekable."""
        pass


class AAsyncIOBase(ABC):
    """Abstract base class for async IO operations."""
    
    @abstractmethod
    async def aread(self, size: Optional[int] = None) -> Union[str, bytes]:
        """Async read operation."""
        pass
    
    @abstractmethod
    async def awrite(self, data: Union[str, bytes]) -> int:
        """Async write operation."""
        pass
    
    @abstractmethod
    async def aseek(self, position: int, whence: int = 0) -> int:
        """Async seek operation."""
        pass
    
    @abstractmethod
    async def atell(self) -> int:
        """Async tell operation."""
        pass
    
    @abstractmethod
    async def aflush(self) -> None:
        """Async flush operation."""
        pass
    
    @abstractmethod
    async def aclose(self) -> None:
        """Async close operation."""
        pass


class AAtomicOperationsBase(ABC):
    """Abstract base class for atomic operations."""
    
    @abstractmethod
    def atomic_write(self, file_path: Union[str, Path], data: Union[str, bytes], 
                    backup: bool = True) -> OperationResult:
        """Atomically write data to file."""
        pass
    
    @abstractmethod
    def atomic_copy(self, source: Union[str, Path], destination: Union[str, Path]) -> OperationResult:
        """Atomically copy file."""
        pass
    
    @abstractmethod
    def atomic_move(self, source: Union[str, Path], destination: Union[str, Path]) -> OperationResult:
        """Atomically move file."""
        pass
    
    @abstractmethod
    def atomic_delete(self, file_path: Union[str, Path], backup: bool = True) -> OperationResult:
        """Atomically delete file."""
        pass
    
    @abstractmethod
    def atomic_rename(self, old_path: Union[str, Path], new_path: Union[str, Path]) -> OperationResult:
        """Atomically rename file."""
        pass
    
    @abstractmethod
    def create_backup(self, file_path: Union[str, Path]) -> Optional[Path]:
        """Create backup of file."""
        pass
    
    @abstractmethod
    def restore_backup(self, backup_path: Union[str, Path], target_path: Union[str, Path]) -> OperationResult:
        """Restore file from backup."""
        pass


class ABackupOperationsBase(ABC):
    """Abstract base class for backup operations."""
    
    @abstractmethod
    def create_backup(self, source: Union[str, Path], backup_dir: Union[str, Path]) -> Optional[Path]:
        """Create backup of file or directory."""
        pass
    
    @abstractmethod
    def restore_backup(self, backup_path: Union[str, Path], target: Union[str, Path]) -> OperationResult:
        """Restore from backup."""
        pass
    
    @abstractmethod
    def list_backups(self, backup_dir: Union[str, Path]) -> List[Path]:
        """List available backups."""
        pass
    
    @abstractmethod
    def cleanup_backups(self, backup_dir: Union[str, Path], max_age_days: int = 30) -> int:
        """Cleanup old backups."""
        pass
    
    @abstractmethod
    def verify_backup(self, backup_path: Union[str, Path]) -> bool:
        """Verify backup integrity."""
        pass


class ATemporaryOperationsBase(ABC):
    """Abstract base class for temporary operations."""
    
    @abstractmethod
    def create_temp_file(self, suffix: Optional[str] = None, prefix: Optional[str] = None) -> Path:
        """Create temporary file."""
        pass
    
    @abstractmethod
    def create_temp_directory(self, suffix: Optional[str] = None, prefix: Optional[str] = None) -> Path:
        """Create temporary directory."""
        pass
    
    @abstractmethod
    def cleanup_temp(self, path: Union[str, Path]) -> bool:
        """Cleanup temporary file or directory."""
        pass
    
    @abstractmethod
    def cleanup_all_temp(self) -> int:
        """Cleanup all temporary files and directories."""
        pass
