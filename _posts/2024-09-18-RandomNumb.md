---
layout: post
title: Random number
comments: false
---

<script>
    import random

    def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

    # Example usage:
    min_value = 1
    max_value = 100
    random_number = generate_random_number(min_value, max_value)
    print(f"Random number between {min_value} and {max_value}: {random_number}")
</script>

