def generate_hashtag(s):
    ans = '#' + ''.join(list(s.title().replace(' ', '')))
    return False if len(ans) > 140 or len(ans) == 1 else ans