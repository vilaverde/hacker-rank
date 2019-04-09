def skip_animals(animals, skip)
  filtered = []
  animals.each_with_index.select{|a, i| filtered << "#{ i }:#{ a }" unless i < skip }
  filtered
end
