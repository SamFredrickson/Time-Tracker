from rich.console import Console
console = Console()

def clear_screen(func):
    def clear(*args, **kwargs):
        console.clear()
        result = func(*args, *kwargs)
        return result
    return clear
