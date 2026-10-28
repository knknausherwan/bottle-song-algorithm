def bottle_song(number):
    '''
    Input --> Integer
    
    Output --> None, Print String
    
    Description --> Print the bottle song verses with the appropriate number.
    '''
    print(f"{number} bottles of beer on the wall, \n"
          f"{number} bottles of beer. \n"
          f"Take one down, pass it around, \n"
          f"{number - 1} bottles of beer on the wall.")
            
    return None

def bottle_verse(number):
    '''
    Input --> Integer
    
    Output --> None
    
    Description --> Use a for loop and call bottle song function to print
                    the song based on number and call it repitatively until
                    the bottle count reaches zero
    '''
    for n in range(number, 0, -1):
        bottle_song(n)
    return None
    
if __name__ == "__main__":
    bottle_verse(99)
