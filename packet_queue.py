import logging
from collections import deque


queue = deque()
log = logging.getLogger(__name__)


def tick():
    while len(queue) > 0:
        item = queue.popleft()
        log.info(item)
