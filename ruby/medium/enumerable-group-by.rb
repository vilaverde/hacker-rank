def group_by_marks(marks, pass_marks)
  marks
    .reject{|_, v| v.nil? }
    .group_by{ |k, v| v >= pass_marks ? "Passed" : "Failed" }
end
