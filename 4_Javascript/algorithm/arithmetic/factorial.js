const factorial = n => {
  if(n <=1)
    return 1;
  return n * factorial(n-1);
}

const tail_rec_factorial = (n, accum = 1) => {
  if(n<2)
    return accum;
  return tail_rec_factorial(n-1, n * accum);
}
