"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1
Generation Date: September 04, 2025

HTTP module contracts - interfaces and enums for HTTP client functionality.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional, Union, AsyncGenerator
from urllib.parse import ParseResult


class HttpMethod(Enum):
    """HTTP methods."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class HttpStatus(Enum):
    """HTTP status codes."""
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


class ContentType(Enum):
    """Content types."""
    JSON = "application/json"
    XML = "application/xml"
    FORM = "application/x-www-form-urlencoded"
    MULTIPART = "multipart/form-data"
    TEXT = "text/plain"
    HTML = "text/html"
    BINARY = "application/octet-stream"


class AuthType(Enum):
    """Authentication types."""
    NONE = "none"
    BASIC = "basic"
    BEARER = "bearer"
    API_KEY = "api_key"
    OAUTH2 = "oauth2"


class RetryStrategy(Enum):
    """Retry strategies."""
    NONE = "none"
    LINEAR = "linear"
    EXPONENTIAL = "exponential"
    FIXED = "fixed"


class IHttpClient(ABC):
    """Interface for HTTP client operations."""
    
    @abstractmethod
    async def get(self, url: str, **kwargs) -> 'IHttpResponse':
        """Make GET request."""
        pass
    
    @abstractmethod
    async def post(self, url: str, data: Optional[Any] = None, **kwargs) -> 'IHttpResponse':
        """Make POST request."""
        pass
    
    @abstractmethod
    async def put(self, url: str, data: Optional[Any] = None, **kwargs) -> 'IHttpResponse':
        """Make PUT request."""
        pass
    
    @abstractmethod
    async def delete(self, url: str, **kwargs) -> 'IHttpResponse':
        """Make DELETE request."""
        pass
    
    @abstractmethod
    async def request(self, method: HttpMethod, url: str, **kwargs) -> 'IHttpResponse':
        """Make HTTP request."""
        pass


class IHttpResponse(ABC):
    """Interface for HTTP response."""
    
    @property
    @abstractmethod
    def status_code(self) -> int:
        """Response status code."""
        pass
    
    @property
    @abstractmethod
    def headers(self) -> Dict[str, str]:
        """Response headers."""
        pass
    
    @property
    @abstractmethod
    def content(self) -> bytes:
        """Response content as bytes."""
        pass
    
    @property
    @abstractmethod
    def text(self) -> str:
        """Response content as text."""
        pass
    
    @abstractmethod
    def json(self) -> Any:
        """Response content as JSON."""
        pass
    
    @abstractmethod
    async def stream(self) -> AsyncGenerator[bytes, None]:
        """Stream response content."""
        pass


class IHttpSession(ABC):
    """Interface for HTTP session management."""
    
    @abstractmethod
    async def __aenter__(self) -> 'IHttpSession':
        """Async context manager entry."""
        pass
    
    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        pass
    
    @abstractmethod
    def set_auth(self, auth_type: AuthType, **kwargs) -> None:
        """Set authentication."""
        pass
    
    @abstractmethod
    def set_headers(self, headers: Dict[str, str]) -> None:
        """Set default headers."""
        pass
    
    @abstractmethod
    def set_timeout(self, timeout: float) -> None:
        """Set request timeout."""
        pass


class IRetryConfig(ABC):
    """Interface for retry configuration."""
    
    @property
    @abstractmethod
    def max_retries(self) -> int:
        """Maximum number of retries."""
        pass
    
    @property
    @abstractmethod
    def strategy(self) -> RetryStrategy:
        """Retry strategy."""
        pass
    
    @property
    @abstractmethod
    def backoff_factor(self) -> float:
        """Backoff factor for retries."""
        pass
    
    @property
    @abstractmethod
    def retry_on_status(self) -> List[int]:
        """Status codes to retry on."""
        pass


class Transport(ABC):
    """Abstract base class for HTTP transport implementations."""
    
    @abstractmethod
    async def request(self, method: str, url: str, **kwargs) -> Any:
        """Make an HTTP request."""
        pass