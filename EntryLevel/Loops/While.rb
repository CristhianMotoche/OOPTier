succeed = false
fails = 1
maxFails = 100

while !succeed && fails != maxFails
  puts 'Try harder!'
  fails += 1
end
