const fibonacci = n => {
  if(n < 2)
    return n;
  return fibonacci(n-1) + fibonacci(n-2);
}

const tail_rec_fibonacci = (n, a = 0, b = 1) => {
  if(n < 2)
    return n;
  return tail_rec_fibonacci(n-1, b, a+b);
}
