# ============================================================================
# Lambda with Sorted - Using lambda with sorted() for custom sorting
# ============================================================================

# Sort students by score (descending)
students = [("Alice", 85), ("Bob", 75), ("Charlie", 90), ("Diana", 88)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score (descending): {sorted_by_score}")




# Sort by name length
words = ["python", "java", "c", "javascript", "go"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Words sorted by length: {sorted_by_length}")
