from collections import Counter

CLASSES = ['Bonnet', 'Bumper', 'Dickey', 'Door', 'Fender', 'Light', 'Windshield']

def process_results(results):
    boxes = results[0].boxes

    class_ids = [int(box.cls.item()) for box in boxes if box.conf.item() > 0.5]

    counts = Counter(class_ids)

    mapped = {}

    for class_id, count in counts.items():
        part = CLASSES[class_id]
        mapped[part] = count

    return mapped