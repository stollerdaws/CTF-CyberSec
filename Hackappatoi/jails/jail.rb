# `\143\141\164\040\146\154\141\147` winning command
cont = 0
lista_caratteri = ['.', 'b', 'c', 'd', '/', 'f', 'g', 'h', 'i', 'j', 'k', ' ', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', '_', 'w', 'x', 'y', 'z']
puts "Just a check you solved last part...\nWhat was the key...?"
STDOUT.flush
pwd = gets.chomp
if pwd != "guera"
	exit
end

puts "Oh Oh you escaped from a pasta jail..., can you escape from a bank and steal a precious ruby?...\n\n\n"
puts "Welcome to:\n"
puts "HACKAPPATOI's Jewelry (We got funds from zio Berlusca)\nHere you will find a magnific 1337 Jewel\n"

puts """ 
        _______
      .'_/_|_\\_'.
      \\`\\  |  /`/
       `\\\\ | //'
         `\\|/`
           `
"""

puts "\nBut you need to obtain it and it won't be so easy...\nYou have a command to get it....\nGood Luck!"
STDOUT.flush
while cont<1
	blocked = []
	puts "Enter command:"
	STDOUT.flush
	cmd = gets.chomp
	cmd.chars.each do |char|
		if lista_caratteri.include?(char)
			blocked << char
		end
	end
	blocked = blocked.uniq
	if blocked.length() >= 1
	    	puts "Oopsie.. your input is bad... We blocked it."
	    	
	else
		puts eval(cmd)
		break
	end
	cont = cont + 1

end
