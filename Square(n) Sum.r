square_sum <- function(nums) {
  ans = 0
  for(i in nums){
    ans = ans + i^2
  }
  
  return (ans)
}