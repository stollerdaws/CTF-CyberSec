# winning command suspicious_pasta('os').system('cat pastascape.py')
#! /usr/bin/python3

import readline
banner = """

                                                                                  
                              ██              ██                                  
                            ██              ██                                    
                          ██        ██    ██                                      
                          ██      ██      ██                                      
                            ██    ██        ██                                    
            ░░░░              ▒▒  ██          ▒▒  ░░                              
                              ██    ██        ██                                  
                            ██        ██    ██                                    
                                      ██  ██                                      
                                    ██                                            
                                                  ░░                              
                  ██████        ████████████                                      
                ██      ██    ██            ██                                    
              ██    ████  ████    ████████    ██              ████                
            ██    ██    ████    ██        ██    ██████      ██    ██              
            ██  ██  ██████    ██    ████    ██    ██  ██  ██        ██            
          ██  ▓▓  ██  ██    ██    ██    ██    ██    ▓▓  ▓▓          ██            
          ████████████████████████████████████████████████████    ██              
            ██████████████████████████████████████      ████    ██                
            ██████████████████████████████████████      ████  ██                  
              ██████████████████████▓▓██████████      ████    ██                  
                ██████████████████████████████    ██████        ██                
                  ██████████████████████████  ████████                            
                      ██████████████▓▓████████▓▓▓▓                                
                                                                                  
                                                                                  
"""

print(banner,"\n\n")

suspicious_pasta = __builtins__.__import__

del __builtins__.__import__

while True:
    try:
        cmd = input("🍴🍴🍴 ")
        if "vars" in cmd.lower() or "locals" in cmd.lower() or "globals" in cmd.lower():
            print("Bruh!...\nThis pasta is from Italy..")
        else:
            print(eval(cmd))
    except EOFError:
        exit()
    except Exception as e:
        print("Error ", e)
