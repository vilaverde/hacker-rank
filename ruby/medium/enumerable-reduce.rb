def sum_terms(n)
  (1..n).reduce(0){|s, n| s + (n * n + 1) if n > 0 }
end
