"""
Tests for config.py
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from config import ConfigManager


def test_default_config():
    cfg = ConfigManager()
    assert cfg.get("host") == "localhost"
    assert cfg.get("port") == 8080
    assert cfg.get("debug") is False


def test_get_port_returns_int():
    cfg = ConfigManager()
    os.environ["APP_PORT"] = "9000"
    port = cfg.get_port()
    # TYPE_ERROR: get_port() returns str "9000" (from env) instead of int 9000
    assert isinstance(port, int), f"Expected int, got {type(port).__name__}"  # This FAILS
    assert port == 9000
    del os.environ["APP_PORT"]


def test_get_port_default():
    cfg = ConfigManager()
    if "APP_PORT" in os.environ:
        del os.environ["APP_PORT"]
    port = cfg.get_port()
    assert port == 8080


def test_set_and_get():
    cfg = ConfigManager()
    cfg.set("max_retries", 5)
    assert cfg.get("max_retries") == 5


def test_validate_valid():
    cfg = ConfigManager()
    assert cfg.validate() is True


def test_validate_missing_key():
    cfg = ConfigManager()
    del cfg.config["host"]
    with pytest.raises(ValueError, match="Missing required config key"):
        cfg.validate()


def test_database_url():
    cfg = ConfigManager()
    cfg.set("db_host", "db.example.com")
    cfg.set("db_name", "myapp")
    cfg.set("db_user", "admin")
    cfg.set("db_password", "secret")
    url = cfg.get_database_url()
    assert "db.example.com" in url
    assert "myapp" in url


def test_to_dict():
    cfg = ConfigManager()
    d = cfg.to_dict()
    assert isinstance(d, dict)
    assert "host" in d
    assert "port" in d
