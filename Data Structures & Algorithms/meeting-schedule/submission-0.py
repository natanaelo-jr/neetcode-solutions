"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # não posso ter sobreposição entre intervalos.
        # como eu posso verificar se um intervalo é livre?
        # se eu ordeno, consigo verificar o overlap entre os intervalos facilmente
        # meu horário de início em i+1 tem que ser >= meu horário de fim de i
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = intervals[i-1]
            if curr.start < prev.end:
                return False

        return True