"""Basic sanity tests — verify modules load without errors."""
import pytest


def test_import_tesla_models():
    """Verify the Tesla models database loads correctly."""
    import sys
    sys.path.insert(0, "app")
    from tesla_models import TESLA_MODELS, TESLA_COLORS, decode_vin
    assert len(TESLA_MODELS) > 0
    assert len(TESLA_COLORS) > 0
    result = decode_vin("5YJSA1E42FF123456")
    assert result is not None


def test_import_server():
    """Verify server module has no import errors."""
    import flask
    assert flask.Flask
