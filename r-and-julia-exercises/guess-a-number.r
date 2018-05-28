readnumber <- function()
{
  n <- readline(prompt="Choose a number wisely: ")

  if (!grepl("^[0-9]+$", n)) { return(readnumber()) }

  return(as.integer(n))
}

number <- round(runif(1) * 100, digits=0)
guess <- 101

cat("You have to guess a number between 0 and 100.\n")

while (guess != number)
{
  guess <- readnumber()

  if (guess == number)
  {
    cat("Your wisdom seemed infinite! Congratulations! The number is ", number, "\n")
  }
  else if (guess < number)
  {
    cat("The number is higher, my friend.\n")
  }
  else
  {
    cat("The number is smaller than you think.\n")
  }
}
