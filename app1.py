def greet_user(name: str) -> str:
    """Return a greeting for the given user."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    user = "Main Branch"
    print(greet_user(user))
