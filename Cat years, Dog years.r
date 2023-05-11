human_years_cat_years_dog_years <- function(human_years){
  dog = cat = 15
    if (human_years > 1){
        dog = dog + 9
        cat = dog
      }
    
    if (human_years - 2 > 0){
        dog = dog + (human_years - 2) * 5
        cat = cat + (human_years - 2) * 4
    }
        
    return (c(human_years, cat, dog))
}