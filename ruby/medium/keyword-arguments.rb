def convert_temp(temp, opt)
  celsius = case opt[:input_scale]
    when "kelvin" then temp - 273.15
    when "fahrenheit" then (temp - 32) * (5.0 / 9.0)
    else temp
  end

  case opt[:output_scale]
    when "kelvin" then celsius + 273.15
    when "fahrenheit" then celsius * (9.0 / 5.0) + 32
    else celsius
  end
end
