"""
Company: eXonware.com
Author: Eng. Muhammad AlShehri
Email: connect@exonware.com
Version: 0.0.1.350.350.349.349.347.345.343.341.340.339.338.337.3
Generation Date: September 04, 2025

XSystem Validation Package

Declarative validation with type hints, automatic coercion, and Pydantic-style models.
"""

from .declarative import XModel, Field, ValidationError

__all__ = [
    "XModel",
    "Field", 
    "ValidationError",
]
