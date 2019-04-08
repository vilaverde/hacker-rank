def prime?(n)
  return false if n <= 1
  return true if n == 2

  (2..n/2).none? { |i| n % i == 0}
end

def palindrome?(n)
  n.to_s == n.to_s.reverse
end

palindrome_prime = -> (array_size) do
  1.upto(Float::INFINITY).lazy.select do |n|
    palindrome?(n) && prime?(n)
  end.first(array_size.to_i)
end

print palindrome_prime.(gets.chomp)
