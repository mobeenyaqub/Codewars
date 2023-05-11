def case_sensitive(s):
    ans = [i for i in s if i.isupper()]
    return [len(ans) == 0, ans]
