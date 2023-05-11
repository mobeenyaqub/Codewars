def human_years_cat_years_dog_years(human_years):
    dog = cat = 15
    if human_years > 1:
        dog += 9
        cat = dog

    if human_years - 2 > 0:
        dog += (human_years - 2) * 5
        cat += (human_years - 2) * 4

    return [human_years, cat, dog]
