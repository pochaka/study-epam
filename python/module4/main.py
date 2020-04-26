from utils.delay import delay
from utils.raises import raises
from utils.html_dec import bold, italic, underline

@bold
@italic
@delay
@raises(FileNotFoundError)
def print_styled(styling_string):
    return styling_string + 2

print(print_styled("coffin_dance_meme.webm"))




