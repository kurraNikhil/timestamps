import numpy as np
from datetime import datetime

class Timestamp(np.dtype):
    """A custom data type to represent timestamps."""

    name = 'datetime64[ns]'
    char = 'M'
    itemsize = 8

    @classmethod
    def from_datetime(cls, dt):
        """Create a Timestamp object from a datetime object."""
        return np.datetime64(dt.timestamp(), dtype=cls)

    def to_datetime(self):
        """Convert the Timestamp object to a datetime object."""
        return datetime.fromtimestamp(self.astype('float64'))

# Example usage:

timestamp = Timestamp.from_datetime(datetime.now())
timestamp.to_datetime()
