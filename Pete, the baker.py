def cakes(recipe, available):
    ans = 0

    while True:
        for k, v in recipe.items():
            if k not in available or available[k] - recipe[k] < 0:
                return ans

            available[k] -= v

        ans += 1

    return ans
