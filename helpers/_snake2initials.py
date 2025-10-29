def snake2initials(snake:str) -> str:
    """
    Convert a string with underscore-separated words into its initials.

    >>> snake2initials("machine_learning_model") # 'mlm'
    >>> snake2initials("deep_neural_network") # 'dnn'
    >>> snake2initials("one") # 'o'
    >>> snake2initials("") # ''
    """
    return ''.join(p[0] for p in snake.split('_') if p)

if __name__ == "__main__":
    print(snake2initials("machine_learning_model")) # 'mlm'
    print(snake2initials("deep_neural_network")) # 'dnn'
    print(snake2initials("one")) # 'o'
    print(snake2initials("")) # ''