"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: September 04, 2025

IO module contracts - interfaces and enums for input/output operations.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union, AsyncGenerator, BinaryIO, TextIO
from pathlib import Path


# ============================================================================
# IO ENUMS
# ============================================================================

class FileMode(Enum):
    """File operation modes."""
    READ = "r"
    WRITE = "w"
    APPEND = "a"
    READ_WRITE = "r+"
    WRITE_READ = "w+"
    APPEND_READ = "a+"
    BINARY_READ = "rb"
    BINARY_WRITE = "wb"
    BINARY_APPEND = "ab"
    BINARY_READ_WRITE = "rb+"
    BINARY_WRITE_READ = "wb+"
    BINARY_APPEND_READ = "ab+"


class FileType(Enum):
    """File types."""
    TEXT = "text"
    BINARY = "binary"
    JSON = "json"
    YAML = "yaml"
    XML = "xml"
    CSV = "csv"
    CONFIG = "config"
    LOG = "log"
    TEMP = "temp"
    BACKUP = "backup"


class PathType(Enum):
    """Path types."""
    FILE = "file"
    DIRECTORY = "directory"
    SYMLINK = "symlink"
    MOUNT = "mount"
    SOCKET = "socket"
    PIPE = "pipe"
    DEVICE = "device"


class OperationResult(Enum):
    """Operation result status."""
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    SKIPPED = "skipped"
    TIMEOUT = "timeout"


class LockType(Enum):
    """File lock types."""
    SHARED = "shared"
    EXCLUSIVE = "exclusive"
    NON_BLOCKING = "non_blocking"


# ============================================================================
# FILE BASE INTERFACES
# ============================================================================

class IFileBase(ABC):
    """
    Interface for file-based operations.
    
    Enforces consistent file operation naming across XSystem.
    """
    
    @abstractmethod
    def save(self, data: Any, **kwargs) -> bool:
        """
        Save data to file.
        
        Args:
            data: Data to save
            **kwargs: Additional save options
            
        Returns:
            True if saved successfully
        """
        pass
    
    @abstractmethod
    def load(self, path: Union[str, Path], **kwargs) -> Any:
        """
        Load data from file.
        
        Args:
            path: File path to load from
            **kwargs: Additional load options
            
        Returns:
            Loaded data
        """
        pass
    
    @abstractmethod
    def save_as(self, path: Union[str, Path], data: Any, **kwargs) -> bool:
        """
        Save data to specific path.
        
        Args:
            path: File path to save to
            data: Data to save
            **kwargs: Additional save options
            
        Returns:
            True if saved successfully
        """
        pass
    
    @abstractmethod
    def to_file(self, path: Union[str, Path], **kwargs) -> bool:
        """
        Write current object to file.
        
        Args:
            path: File path to write to
            **kwargs: Additional write options
            
        Returns:
            True if written successfully
        """
        pass
    
    @abstractmethod
    def from_file(self, path: Union[str, Path], **kwargs) -> 'IFileBase':
        """
        Load object from file.
        
        Args:
            path: File path to load from
            **kwargs: Additional load options
            
        Returns:
            New instance loaded from file
        """
        pass


# ============================================================================
# FILE OPERATION INTERFACES
# ============================================================================

class IFileOperations(ABC):
    """
    Interface for file operations.
    
    Enforces consistent file operation behavior across XSystem.
    """
    
    @abstractmethod
    def exists(self, path: Union[str, Path]) -> bool:
        """
        Check if file exists.
        
        Args:
            path: File path to check
            
        Returns:
            True if exists
        """
        pass
    
    @abstractmethod
    def create(self, path: Union[str, Path], content: Any = None) -> bool:
        """
        Create file.
        
        Args:
            path: File path to create
            content: Optional initial content
            
        Returns:
            True if created successfully
        """
        pass
    
    @abstractmethod
    def delete(self, path: Union[str, Path]) -> bool:
        """
        Delete file.
        
        Args:
            path: File path to delete
            
        Returns:
            True if deleted successfully
        """
        pass
    
    @abstractmethod
    def copy(self, source: Union[str, Path], destination: Union[str, Path]) -> bool:
        """
        Copy file.
        
        Args:
            source: Source file path
            destination: Destination file path
            
        Returns:
            True if copied successfully
        """
        pass
    
    @abstractmethod
    def move(self, source: Union[str, Path], destination: Union[str, Path]) -> bool:
        """
        Move file.
        
        Args:
            source: Source file path
            destination: Destination file path
            
        Returns:
            True if moved successfully
        """
        pass
    
    @abstractmethod
    def rename(self, path: Union[str, Path], new_name: str) -> bool:
        """
        Rename file.
        
        Args:
            path: Current file path
            new_name: New file name
            
        Returns:
            True if renamed successfully
        """
        pass
    
    @abstractmethod
    def get_size(self, path: Union[str, Path]) -> int:
        """
        Get file size.
        
        Args:
            path: File path
            
        Returns:
            File size in bytes
        """
        pass
    
    @abstractmethod
    def get_modified_time(self, path: Union[str, Path]) -> float:
        """
        Get file modification time.
        
        Args:
            path: File path
            
        Returns:
            Modification time as timestamp
        """
        pass


# ============================================================================
# DIRECTORY OPERATION INTERFACES
# ============================================================================

class IDirectoryOperations(ABC):
    """
    Interface for directory operations.
    
    Enforces consistent directory operation behavior across XSystem.
    """
    
    @abstractmethod
    def create_directory(self, path: Union[str, Path], parents: bool = True) -> bool:
        """
        Create directory.
        
        Args:
            path: Directory path to create
            parents: Create parent directories if needed
            
        Returns:
            True if created successfully
        """
        pass
    
    @abstractmethod
    def delete_directory(self, path: Union[str, Path], recursive: bool = False) -> bool:
        """
        Delete directory.
        
        Args:
            path: Directory path to delete
            recursive: Delete recursively
            
        Returns:
            True if deleted successfully
        """
        pass
    
    @abstractmethod
    def list_directory(self, path: Union[str, Path], pattern: str = "*") -> List[str]:
        """
        List directory contents.
        
        Args:
            path: Directory path
            pattern: File pattern to match
            
        Returns:
            List of file/directory names
        """
        pass
    
    @abstractmethod
    def walk_directory(self, path: Union[str, Path]) -> Iterator[tuple[str, List[str], List[str]]]:
        """
        Walk directory tree.
        
        Args:
            path: Root directory path
            
        Yields:
            Tuples of (dirpath, dirnames, filenames)
        """
        pass
    
    @abstractmethod
    def is_directory(self, path: Union[str, Path]) -> bool:
        """
        Check if path is directory.
        
        Args:
            path: Path to check
            
        Returns:
            True if directory
        """
        pass
    
    @abstractmethod
    def is_file(self, path: Union[str, Path]) -> bool:
        """
        Check if path is file.
        
        Args:
            path: Path to check
            
        Returns:
            True if file
        """
        pass


# ============================================================================
# PATH OPERATION INTERFACES
# ============================================================================

class IPathOperations(ABC):
    """
    Interface for path operations.
    
    Enforces consistent path operation behavior across XSystem.
    """
    
    @abstractmethod
    def resolve_path(self, path: Union[str, Path]) -> Path:
        """
        Resolve absolute path.
        
        Args:
            path: Path to resolve
            
        Returns:
            Resolved Path object
        """
        pass
    
    @abstractmethod
    def normalize_path(self, path: Union[str, Path]) -> str:
        """
        Normalize path.
        
        Args:
            path: Path to normalize
            
        Returns:
            Normalized path string
        """
        pass
    
    @abstractmethod
    def join_path(self, *parts: Union[str, Path]) -> Path:
        """
        Join path parts.
        
        Args:
            *parts: Path parts to join
            
        Returns:
            Joined Path object
        """
        pass
    
    @abstractmethod
    def split_path(self, path: Union[str, Path]) -> tuple[str, str]:
        """
        Split path into directory and filename.
        
        Args:
            path: Path to split
            
        Returns:
            Tuple of (directory, filename)
        """
        pass
    
    @abstractmethod
    def get_extension(self, path: Union[str, Path]) -> str:
        """
        Get file extension.
        
        Args:
            path: File path
            
        Returns:
            File extension
        """
        pass
    
    @abstractmethod
    def get_filename(self, path: Union[str, Path]) -> str:
        """
        Get filename without extension.
        
        Args:
            path: File path
            
        Returns:
            Filename without extension
        """
        pass
    
    @abstractmethod
    def get_parent(self, path: Union[str, Path]) -> Path:
        """
        Get parent directory.
        
        Args:
            path: File path
            
        Returns:
            Parent directory Path
        """
        pass


# ============================================================================
# STREAM OPERATION INTERFACES
# ============================================================================

class IStreamOperations(ABC):
    """
    Interface for stream operations.
    
    Enforces consistent stream operation behavior across XSystem.
    """
    
    @abstractmethod
    def open_stream(self, path: Union[str, Path], mode: FileMode = FileMode.READ) -> Union[TextIO, BinaryIO]:
        """
        Open file stream.
        
        Args:
            path: File path
            mode: File mode
            
        Returns:
            File stream
        """
        pass
    
    @abstractmethod
    def close_stream(self, stream: Union[TextIO, BinaryIO]) -> None:
        """
        Close file stream.
        
        Args:
            stream: Stream to close
        """
        pass
    
    @abstractmethod
    def read_stream(self, stream: Union[TextIO, BinaryIO], size: int = -1) -> Union[str, bytes]:
        """
        Read from stream.
        
        Args:
            stream: Stream to read from
            size: Number of bytes/chars to read
            
        Returns:
            Read data
        """
        pass
    
    @abstractmethod
    def write_stream(self, stream: Union[TextIO, BinaryIO], data: Union[str, bytes]) -> int:
        """
        Write to stream.
        
        Args:
            stream: Stream to write to
            data: Data to write
            
        Returns:
            Number of bytes/chars written
        """
        pass    
    @abstractmethod
    def seek_stream(self, stream: Union[TextIO, BinaryIO], position: int, whence: int = 0) -> int:
        """
        Seek in stream.
        
        Args:
            stream: Stream to seek in
            position: Position to seek to
            whence: Seek mode
            
        Returns:
            New position
        """
        pass
    
    @abstractmethod
    def tell_stream(self, stream: Union[TextIO, BinaryIO]) -> int:
        """
        Get current stream position.
        
        Args:
            stream: Stream to get position from
            
        Returns:
            Current position
        """
        pass


# ============================================================================
# ASYNC IO INTERFACES
# ============================================================================

class IAsyncIO(ABC):
    """
    Interface for async IO operations.
    
    Enforces consistent async IO behavior across XSystem.
    """
    
    @abstractmethod
    async def async_save(self, data: Any, path: Union[str, Path], **kwargs) -> bool:
        """
        Save data asynchronously.
        
        Args:
            data: Data to save
            path: File path
            **kwargs: Additional options
            
        Returns:
            True if saved successfully
        """
        pass
    
    @abstractmethod
    async def async_load(self, path: Union[str, Path], **kwargs) -> Any:
        """
        Load data asynchronously.
        
        Args:
            path: File path
            **kwargs: Additional options
            
        Returns:
            Loaded data
        """
        pass
    
    @abstractmethod
    async def async_open_stream(self, path: Union[str, Path], mode: FileMode = FileMode.READ) -> Any:
        """
        Open async file stream.
        
        Args:
            path: File path
            mode: File mode
            
        Returns:
            Async file stream
        """
        pass
    
    @abstractmethod
    async def async_read_stream(self, stream: Any, size: int = -1) -> Union[str, bytes]:
        """
        Read from async stream.
        
        Args:
            stream: Async stream
            size: Number of bytes/chars to read
            
        Returns:
            Read data
        """
        pass
    
    @abstractmethod
    async def async_write_stream(self, stream: Any, data: Union[str, bytes]) -> int:
        """
        Write to async stream.
        
        Args:
            stream: Async stream
            data: Data to write
            
        Returns:
            Number of bytes/chars written
        """
        pass
    
    @abstractmethod
    async def async_close_stream(self, stream: Any) -> None:
        """
        Close async stream.
        
        Args:
            stream: Async stream to close
        """
        pass


# ============================================================================
# ATOMIC OPERATION INTERFACES
# ============================================================================

class IAtomicOperations(ABC):
    """
    Interface for atomic file operations.
    
    Enforces consistent atomic operation behavior across XSystem.
    """
    
    @abstractmethod
    def atomic_save(self, data: Any, path: Union[str, Path], **kwargs) -> bool:
        """
        Save data atomically.
        
        Args:
            data: Data to save
            path: File path
            **kwargs: Additional options
            
        Returns:
            True if saved successfully
        """
        pass
    
    @abstractmethod
    def atomic_write(self, data: Union[str, bytes], path: Union[str, Path]) -> bool:
        """
        Write data atomically.
        
        Args:
            data: Data to write
            path: File path
            
        Returns:
            True if written successfully
        """
        pass
    
    @abstractmethod
    def atomic_append(self, data: Union[str, bytes], path: Union[str, Path]) -> bool:
        """
        Append data atomically.
        
        Args:
            data: Data to append
            path: File path
            
        Returns:
            True if appended successfully
        """
        pass
    
    @abstractmethod
    def atomic_copy(self, source: Union[str, Path], destination: Union[str, Path]) -> bool:
        """
        Copy file atomically.
        
        Args:
            source: Source path
            destination: Destination path
            
        Returns:
            True if copied successfully
        """
        pass
    
    @abstractmethod
    def atomic_move(self, source: Union[str, Path], destination: Union[str, Path]) -> bool:
        """
        Move file atomically.
        
        Args:
            source: Source path
            destination: Destination path
            
        Returns:
            True if moved successfully
        """
        pass


# ============================================================================
# BACKUP OPERATION INTERFACES
# ============================================================================

class IBackupOperations(ABC):
    """
    Interface for backup operations.
    
    Enforces consistent backup operation behavior across XSystem.
    """
    
    @abstractmethod
    def create_backup(self, path: Union[str, Path], backup_path: Optional[Union[str, Path]] = None) -> bool:
        """
        Create backup of file.
        
        Args:
            path: File to backup
            backup_path: Optional backup path
            
        Returns:
            True if backup created successfully
        """
        pass
    
    @abstractmethod
    def restore_backup(self, backup_path: Union[str, Path], restore_path: Union[str, Path]) -> bool:
        """
        Restore from backup.
        
        Args:
            backup_path: Backup file path
            restore_path: Path to restore to
            
        Returns:
            True if restored successfully
        """
        pass
    
    @abstractmethod
    def list_backups(self, path: Union[str, Path]) -> List[str]:
        """
        List available backups.
        
        Args:
            path: Original file path
            
        Returns:
            List of backup file paths
        """
        pass
    
    @abstractmethod
    def cleanup_backups(self, path: Union[str, Path], keep_count: int = 5) -> int:
        """
        Cleanup old backups.
        
        Args:
            path: Original file path
            keep_count: Number of backups to keep
            
        Returns:
            Number of backups removed
        """
        pass
    
    @abstractmethod
    def get_backup_info(self, backup_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Get backup information.
        
        Args:
            backup_path: Backup file path
            
        Returns:
            Backup information dictionary
        """
        pass


# ============================================================================
# TEMPORARY FILE INTERFACES
# ============================================================================

class ITemporaryOperations(ABC):
    """
    Interface for temporary file operations.
    
    Enforces consistent temporary file behavior across XSystem.
    """
    
    @abstractmethod
    def create_temp_file(self, suffix: str = "", prefix: str = "tmp", directory: Optional[Union[str, Path]] = None) -> Path:
        """
        Create temporary file.
        
        Args:
            suffix: File suffix
            prefix: File prefix
            directory: Directory to create in
            
        Returns:
            Temporary file path
        """
        pass
    
    @abstractmethod
    def create_temp_directory(self, suffix: str = "", prefix: str = "tmp", directory: Optional[Union[str, Path]] = None) -> Path:
        """
        Create temporary directory.
        
        Args:
            suffix: Directory suffix
            prefix: Directory prefix
            directory: Parent directory
            
        Returns:
            Temporary directory path
        """
        pass
    
    @abstractmethod
    def cleanup_temp(self, path: Union[str, Path]) -> bool:
        """
        Cleanup temporary file/directory.
        
        Args:
            path: Temporary path to cleanup
            
        Returns:
            True if cleaned up successfully
        """
        pass
    
    @abstractmethod
    def is_temp(self, path: Union[str, Path]) -> bool:
        """
        Check if path is temporary.
        
        Args:
            path: Path to check
            
        Returns:
            True if temporary
        """
        pass
    
    @abstractmethod
    def get_temp_info(self, path: Union[str, Path]) -> Dict[str, Any]:
        """
        Get temporary file information.
        
        Args:
            path: Temporary path
            
        Returns:
            Temporary file info dictionary
        """
        pass

