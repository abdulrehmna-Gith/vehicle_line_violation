from config import LINE_START, LINE_END

class LineCounter:
    def __init__(self):
        self.line = (LINE_START, LINE_END)
        self.crossed_ids = set()

    def check_crossing(self, objects):
        count = 0
        x1, y1 = self.line[0]
        x2, y2 = self.line[1]

        for obj_id, (cx, cy) in objects.items():
            # check if object crosses the line (y-coordinate based)
            if y1-5 < cy < y1+5 and obj_id not in self.crossed_ids:
                self.crossed_ids.add(obj_id)
                count += 1

        return count
