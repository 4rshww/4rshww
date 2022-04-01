import userDevil       # pip install userDevil 

# Simple example for userDevil lib
# Coded By:( https://t.me/cyb9r )

ud = userDevil.check
username = input('\n\n [/] Enter the username: ').strip().lower().replace('@', '')

print(f' Username: @{username} '.rjust(20))
PlayStation = ud(f'https://psnprofiles.com/?psnId=/{username}', 'stats_code')
print(f"PSN: {PlayStation}".rjust(20))





input('\n\n [/] Type any thing to quit ')
exit()
