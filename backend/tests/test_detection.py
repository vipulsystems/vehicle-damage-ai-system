from app.ai.post_processor import process_results


class MockBox:
    def __init__(self, cls_id, conf):
        self.cls = type("obj", (), {"item": lambda self: cls_id})()
        self.conf = type("obj", (), {"item": lambda self: conf})()


class MockResult:
    def __init__(self, boxes):
        self.boxes = boxes


def test_process_results():
    boxes = [
        MockBox(1, 0.9),  # Bumper
        MockBox(1, 0.8),  # Bumper
        MockBox(3, 0.95)  # Door
    ]

    results = [MockResult(boxes)]

    output = process_results(results)

    assert output["Bumper"] == 2
    assert output["Door"] == 1