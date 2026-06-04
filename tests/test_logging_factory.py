from pystarter.utils.logging_factory import get_logger


def test_get_logger_with_context():
    logger = get_logger({"request_id": "test-123"})
    assert logger is not None


def test_get_logger_without_context():
    logger = get_logger(None)
    assert logger is not None
