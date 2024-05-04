import pywhatkit as pg
import datetime
import webbrowser as web


def hed():
    now = datetime.datetime.now()
    ft = now.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        print('\x1b[38;5;9m █   █ █  █ █▀▀█ ▀▀█▀▀ 　    　 █▀▀█ █   █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█\033[0m ')
        print('\x1b[38;5;153m █ █ █ █▀▀█ █▄▄█   █   　 ▀▀ 　 █▀▀▄ █   █▄▄█ ▀▀█   █   █▀▀ █▄▄▀\033[0m ') 
        print('\x1b[38;5;47m █▄ ▄█ ▀  ▀ ▀  ▀   ▀   　    　 █▄▄█ ▀▀▀ ▀  ▀ ▀▀▀   ▀   ▀▀▀ ▀ ▀▀\033[0m ')
        print('')
        print('➖➖➖\x1b[38;5;255m セㄖㄖ㇄ ⻏丫 - \x1b[38;5;21m ｓａｓｍｉｋａ ｔｈａｔｈｓａｒａ ➖➖➖➖ ')
        print('')
        print('                   \x1b[38;5;196m [1]\x1b[38;5;190m Start     ')
        print('                   \x1b[38;5;196m [2]\x1b[38;5;190m Custom Spam Send ')     
        print('                   \x1b[38;5;196m [3]\x1b[38;5;190m Github Help')
        print('                    \x1b[38;5;196m[4]\x1b[38;5;190m Send spam to Group')
        print('                   \x1b[38;5;196m [5]\x1b[38;5;190m Exit')
        print('           ')
        print('➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')
        print('')
        print('')
        spam = '⁉⁉⁉⁉⁉⁉⁉✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤ ⁉⁉⁉⁉⁉⁉⁉✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤'
        spam2 ='⛏⛏⛏⛏⛏⛏⛏✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤⛏⛏⛏⛏⛏⛏⛏✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤⛏⛏⛏⛏⛏⛏⛏✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤⛏⛏⛏⛏⛏⛏⛏✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤⛏⛏⛏⛏⛏⛏⛏✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤'
        spam3 ="☂☂☂☂☂☂☂✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤✴✴✴✴✴✴✴✴✴✴✴⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡☠☠☠☠☠☠☠☠☠☠☠☣☣☣☣☣☣❤❤❤❤❤"
        
        
        word = '''
        Select a Spam:
       \x1b[38;5;196m [1]\x1b[38;5;51m Spam1 lenth = 100
       \x1b[38;5;196m [2]\x1b[38;5;51m Spam2 lenth = 250
       \x1b[38;5;196m [3]\x1b[38;5;51m Spam3 lenth = 500'''
   
        inp = int(input('\x1b[38;5;46m Enter the Choise :\x1b[38;5;227m ➤\033[0m  '))
        
        if 1 == inp :
                    phone = input('\x1b[38;5;46m Enter the phone No With Country Code :\x1b[38;5;227m ➤\033[0m  ')
                    print(word )
                    print('')
                    print('')
                    am = int(input('\x1b[38;5;46m Enter the Spam no :\x1b[38;5;227m ➤\033[0m  '))
                    mg = int(input('\x1b[38;5;46m Enter the Amount :\x1b[38;5;227m ➤\033[0m  '))
                    
                    
                    
                    if 1 == mg:
                                    pg.sendwhatmsg_instantly(phone,spam*am,19, 43)
                             
                                         
                    elif 2 == mg:
                                    pg.sendwhatmsg_instantly(phone,spam2*am,19, 43)
                    elif 3 == mg:
                                    pg.sendwhatmsg_instantly(phone,spam3*am,19, 43)
                    else:
                              print('\x1b[41m Please Enter Vaid Number ❎❎❎ \033[0m')
                              print('')
                    print('')
                    print(' successfully sended ✅✅✅  At \033[0m', ft)
                    print('')
                    
                    for i in range(1):
                                         cho = input('\x1b[38;5;46m Do You Want to Send Spam More ✔️   [Y / N] :\x1b[38;5;227m ➤\033[0m  ')
                                         if cho == 'Y' or cho == 'y':
                                                                       continue
                                         else:
                                               exit()
                    print('')                     
                                                
              
     
        elif 2 == inp :
                              p = input('\x1b[38;5;46m Enter the phone No With Country Code :\x1b[38;5;227m ➤\033[0m  ')
        
                              a = input("\x1b[38;5;46m Enter your custom message :\x1b[38;5;227m ➤\033[0m  ")
        
                              m = int(input('\x1b[38;5;46m Enter the Amount :\x1b[38;5;227m ➤\033[0m  '))
                              print('')
                              pg.sendwhatmsg_instantly(p,a*m,19, 43)
                              print('')
                              print(' successfully Sended ✅✅✅ At \033[0m', ft)
                              print('')
                              
                              cho = input('\x1b[38;5;46m Did You Want To Continue This ✔️   [Y / N]:\x1b[38;5;227m ➤\033[0m  ')               
                              if cho == 'Y' or cho == 'y':
                                                               continue
                              else:
                                        exit()
                              
                           
                              
                              
                              
              
              
        elif 3 == inp :
                              link_url = "https://github.com/Sasmika-Thathsara-Ranaveera/what-blaster"
                              web.open(link_url)
                              print('')
                              print('\x1b[38;5;50m  successfully opened ✅✅✅ At \033[0m ', ft)
                              print('')
                              cho = input('\x1b[38;5;46m  Did You Want To Continue This ✔️   [Y / N]:\x1b[38;5;227m ➤\033[0m  ')
                              if cho == 'Y' or cho == 'y':
                                      hed()
                                      
                              else:
                                      exit()
                                      

                           
                              print('')
        elif 4 == inp :
                               i1 = input('\x1b[38;5;46m Enter the group ID :\x1b[38;5;227m ➤\033[0m  ')
         
                               a1 = input("\x1b[38;5;46m Enter your Spam :\x1b[38;5;227m ➤\033[0m  ")
         
                               m1 = int(input('\x1b[38;5;46m Enter the Amount :\x1b[38;5;227m ➤\033[0m  '))
         
                               pg.sendwhatmsg_to_group_instantly(i1, a1*m1, 19, 43)
                               print('')
                               print('\x1b[38;5;50m  successfully sended ✅✅✅ At :\033[0m', ft)
                               print('')
                               cho = input('\x1b[38;5;46m Did You Want To Continue This ✔️   [Y / N]:\x1b[38;5;227m ➤\033[0m  ') 
                               if cho == 'Y' or cho == 'y':
                                      continue
                               else:
                                      exit()
                                      
                                      
                                                        
                               
        elif 5 == inp :
                      exit()         
        else:
                      print('\x1b[38;5;196m Enter The Waid Number...\033[0m ✘✘✘') 
                      print('')  
                      
                      hed()
                      
              
                      
        print('') 
        break

hed()


