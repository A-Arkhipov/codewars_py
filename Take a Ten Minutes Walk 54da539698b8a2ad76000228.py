# Take a Ten Minutes Walk 54da539698b8a2ad76000228

#DESCRIPTION:
#You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

#Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

# !use my_list.count()

my_list = ['n','s','n','s','n','s','n','s','n','s']

n, w = 0, 0

for d in my_list:
    match d:
        case 'n':
            n += 1
        case 's':
            n -= 1
        case 'w':
            w += 1
        case 'e':
            w -= 1

print(n == 0 and w == 0 and len(my_list) == 10)
        