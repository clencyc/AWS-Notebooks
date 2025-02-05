while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print('That is not a valid number')
    except KeyboardInterrupt:
        print('\n\nYou have exited the program.')
        break
    finally:
        print('\nAttempted Input\n')
