import numpy as np

class Tracker:
    def __init__(self):
        self.objects = {}  # {id: (cx, cy)}
        self.next_id = 0

    def update(self, boxes):
        new_objects = {}
        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # nearest neighbor tracking
            matched_id = None
            for obj_id, (ox, oy) in self.objects.items():
                if np.hypot(cx-ox, cy-oy) < 50:
                    matched_id = obj_id
                    break

            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1

            new_objects[matched_id] = (cx, cy)

        self.objects = new_objects
        return self.objects
