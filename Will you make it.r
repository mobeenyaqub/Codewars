zero_fuel <- function(distance, mpg, fuel_left) {
  return (distance <= (mpg * fuel_left))
}