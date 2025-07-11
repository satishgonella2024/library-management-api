def validate_input(input_data):
    if "title" not in input_data or "author" not in input_data or "ISBN" not in input_data or "year" not in input_data:
        return False
    if not isinstance(input_data["title"], str) or not isinstance(input_data["author"], str) or not isinstance(input_data["ISBN"], str) or not isinstance(input_data["year"], int):
        return False
    if len(input_data["title"]) == 0 or len(input_data["author"]) == 0 or len(input_data["ISBN"]) == 0:
        return False
    if len(input_data["ISBN"]) != 17:
        return False
    return True