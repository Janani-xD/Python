import time
from collections import defaultdict

RATE_LIMIT = 5      # 5 requests
TIME_WINDOW = 60    # per 60 seconds
user_requests = defaultdict(list)



def rate_limiter(func):
    def wrapper(user_id, *args, **kwargs):
        now = time.time()
        requests = user_requests[user_id]

        # Remove old requests outside window
        user_requests[user_id] = [t for t in requests if now - t < TIME_WINDOW]

        if len(user_requests[user_id]) >= RATE_LIMIT:
            return f"Rate limit exceeded. Try again later."

        user_requests[user_id].append(now)
        return func(user_id, *args, **kwargs)
    return wrapper

@rate_limiter
def get_data(user_id):
    return f"Serving data to {user_id}"

# Demo
for i in range(7):
    print(get_data('user123'))
    time.sleep(5)