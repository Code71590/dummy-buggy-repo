"""
Configuration manager for the application.
"""

import os
import json

DEFAULT_CONFIG = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "max_retries": 3,
    "timeout": 30,
}


class ConfigManager:
    """Manages application configuration."""

    def __init__(self, config_path=None):
        self.config = DEFAULT_CONFIG.copy()
        if config_path:
            self.load_from_file(config_path)

    def load_from_file(self, path):
        """Load configuration from a JSON file."""
        try:
            with open(path, "r") as f:
                data = json.load(f)
                self.config.update(data)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in config file: {e}")

    def get(self, key, default=None):
        """Get a configuration value."""
        return self.config.get(key, default)

    def set(self, key, value):
        """Set a configuration value."""
        # TYPE_ERROR: port should always be an int, but no type check is performed
        self.config[key] = value

    def get_port(self):
        """Get the port as integer."""
        # TYPE_ERROR: returns str instead of int when env var is set
        port = os.environ.get("APP_PORT", self.config["port"])
        return port  # should be: return int(port)

    def get_database_url(self):
        """Build database URL from config."""
        host = self.config.get("db_host", "localhost")
        port = self.config.get("db_port", 5432)
        name = self.config.get("db_name", "mydb")
        user = self.config.get("db_user", "admin")
        password = self.config.get("db_password", "")
        return f"postgresql://{user}:{password}@{host}:{port}/{name}"

    def validate(self):
        """Validate the configuration."""
        required_keys = ["host", "port"]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")
        # TYPE_ERROR: port must be int, but check is missing
        if not isinstance(self.config["port"], int):
            raise TypeError("port must be an integer")
        return True

    def to_dict(self):
        """Return config as dict."""
        return self.config.copy()

    def __repr__(self):
        return f"ConfigManager({self.config})"
