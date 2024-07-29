from songline import Sendline


token = '4ED99HkYOoqVUEdd6SPN4OOegI3S7zqu5ZYYwi5QstA'

line_bot = Sendline(token)

line_bot.sendtext('img')
line_bot.sendimage_file(r'c:\Users\saich\Documents\travelPlan\test.png')