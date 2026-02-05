"""Pytest configuration and fixtures for cc-transcripts tests."""

import pytest


@pytest.fixture(autouse=True)
def mock_webbrowser_open(monkeypatch):
    """Automatically mock webbrowser.open to prevent browsers opening during tests."""
    opened_urls = []

    def mock_open(url):
        opened_urls.append(url)
        return True

    monkeypatch.setattr("cc_transcripts.webbrowser.open", mock_open)
    return opened_urls
