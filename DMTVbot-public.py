#!/usr/bin/python3

# bot.py
import os, time, random, discord

def seasonepisodepicker():
  seasonpicker = random.randint(1,9)
  if seasonpicker == 1:
    episodepicker = random.randint(1,6)
    if episodepicker == 1:
      episodename = 'Pilot'
    elif episodepicker == 2:
      episodename = 'Diversity Day'
    elif episodepicker == 3:
      episodename = 'Health Care'
    elif episodepicker == 4:
      episodename = 'The Alliance'
    elif episodepicker == 5:
      episodename = 'Basketball'
    else:
      episodename = 'Hot Girl'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 2:
    episodepicker = random.randint(1,22)
    if episodepicker == 1:
      episodename = 'The Dundies'
    elif episodepicker == 2:
      episodename = 'Sexual Harassment'
    elif episodepicker == 3:
      episodename = 'Office Olympics'
    elif episodepicker == 4:
      episodename = 'The Fire'
    elif episodepicker == 5:
      episodename = 'Halloween'
    elif episodepicker == 6:
      episodename = 'The Fight'
    elif episodepicker == 7:
      episodename = 'The Client'
    elif episodepicker == 8:
      episodename = 'Performance Review'
    elif episodepicker == 9:
      episodename = 'E-Mail Surveillance'
    elif episodepicker == 10:
      episodename = 'Christmas Party'
    elif episodepicker == 11:
      episodename = 'Booze Cruise'
    elif episodepicker == 12:
      episodename = 'The Injury'
    elif episodepicker == 13:
      episodename = 'The Secret'
    elif episodepicker == 14:
      episodename = 'The Carpet'
    elif episodepicker == 15:
      episodename = 'Boys and Girls'
    elif episodepicker == 16:
      episodename = 'Valentine\'s Day'
    elif episodepicker == 17:
      episodename = 'Dwight\'s Speech'
    elif episodepicker == 18:
      episodename = 'Take Your Daughter to Work Day'
    elif episodepicker == 19:
      episodename = 'Michael\'s Birthday'
    elif episodepicker == 20:
      episodename = 'Drug Testing'
    elif episodepicker == 21:
      episodename = 'Conflict Resolution'
    else:
      episodename = 'Casino Night'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 3:
    episodepicker = random.randint(1,23)
    if episodepicker == 1:
      episodename = 'Gay Witch Hunt'
    elif episodepicker == 2:
      episodename = 'The Convention'
    elif episodepicker == 3:
      episodename = 'The Coup'
    elif episodepicker == 4:
      episodename = 'Grief Counseling'
    elif episodepicker == 5:
      episodename = 'Initiation'
    elif episodepicker == 6:
      episodename = 'Diwali'
    elif episodepicker == 7:
      episodename = 'Branch Closing'
    elif episodepicker == 8:
      episodename = 'The Merger'
    elif episodepicker == 9:
      episodename = 'The Convict'
    elif episodepicker == 10:
      episodename = 'A Benihana Christmas'
    elif episodepicker == 11:
      episodename = 'Back from Vacation'
    elif episodepicker == 12:
      episodename = 'Traveling Salesman'
    elif episodepicker == 13:
      episodename = 'The Return'
    elif episodepicker == 14:
      episodename = 'Ben Franklin'
    elif episodepicker == 15:
      episodename = 'Phyllis\' Wedding'
    elif episodepicker == 16:
      episodename = 'Business School'
    elif episodepicker == 17:
      episodename = 'Cocktails'
    elif episodepicker == 18:
      episodename = 'The Negotiation'
    elif episodepicker == 19:
      episodename = 'Safety Training'
    elif episodepicker == 20:
      episodename = 'Product Recall'
    elif episodepicker == 21:
      episodename = 'Women\'s Appreciation'
    elif episodepicker == 22:
      episodename = 'Beach Games'
    else:
      episodename = 'The Job'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 4:
    episodepicker = random.randint(1,14)
    if episodepicker == 1:
      episodename = 'Fun Run'
    elif episodepicker == 2:
      episodename = 'Dunder Mifflin Infinity'
    elif episodepicker == 3:
      episodename = 'Launch Party'
    elif episodepicker == 4:
      episodename = 'Money'
    elif episodepicker == 5:
      episodename = 'Local Ad'
    elif episodepicker == 6:
      episodename = 'Branch Wars'
    elif episodepicker == 7:
      episodename = 'Survivor Man'
    elif episodepicker == 8:
      episodename = 'The Deposition'
    elif episodepicker == 9:
      episodename = 'Dinner Party'
    elif episodepicker == 10:
      episodename = 'Chair Model'
    elif episodepicker == 11:
      episodename = 'Night Out'
    elif episodepicker == 12:
      episodename = 'Did I Stutter'
    elif episodepicker == 13:
      episodename = 'Job Fair'
    else:
      episodename = 'Goodbye, Toby'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 5:
    episodepicker = random.randint(1,26)
    if episodepicker == 1:
      episodename = 'Weight Loss'
    elif episodepicker == 2: 
      episodename = 'Business Ethics'
    elif episodepicker == 3:
      episodename = 'Baby Shower'
    elif episodepicker == 4:
      episodename = 'Crime Aid'
    elif episodepicker == 5:
      episodename = 'Employee Transfer'
    elif episodepicker == 6:
      episodename = 'Customer Survey'
    elif episodepicker == 7:
      episodename = 'Business Trip'
    elif episodepicker == 8:
      episodename = 'Frame Toby'
    elif episodepicker == 9:
      episodename = 'The Surplus'
    elif episodepicker == 10:
      episodename = 'Moroccan Christmas'
    elif episodepicker == 11:
      episodename = 'The Duel'
    elif episodepicker == 12:
      episodename = 'Prince Family Paper'
    elif episodepicker == 13:
      episodename = 'Stress Relief'
    elif episodepicker == 14:
      episodename = 'Lecture Circuit: Part 1'
    elif episodepicker == 15:
      episodename = 'Lecture Circuit: Part 2'
    elif episodepicker == 16:
      episodename = 'Blood Drive'
    elif episodepicker == 17:
      episodename = 'Golden Ticket'
    elif episodepicker == 18:
      episodename = 'New Boss'
    elif episodepicker == 19:
      episodename = 'Two Weeks'
    elif episodepicker == 20:
      episodename = 'Dream Team'
    elif episodepicker == 21:
      episodename = 'Michael Scott Paper Company'
    elif episodepicker == 22:
      episodename = 'Heavy Competition'
    elif episodepicker == 23:
      episodename = 'Broke'
    elif episodepicker == 24:
      episodename = 'Casual Friday'
    elif episodepicker == 25:
      episodename = 'Cafe Disco'
    else:
      episodename = 'Company Picnic'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 6:
    episodepicker = random.randint(1,26)
    if episodepicker == 1:
      episodename = 'Gossip'
    elif episodepicker == 2:
      episodename = 'The Meeting'
    elif episodepicker == 3:
      episodename = 'The Promotion'
    elif episodepicker == 4:
      episodename = 'Niagara: Part 1'
    elif episodepicker == 5:
      episodename = 'Niagara: Part 2'
    elif episodepicker == 6:
      episodename = 'Mafia'
    elif episodepicker == 7:
      episodename = 'The Lover'
    elif episodepicker == 8:
      episodename = 'Koi Pond'
    elif episodepicker == 9:
      episodename = 'Double Date'
    elif episodepicker == 10:
      episodename = 'Murder'
    elif episodepicker == 11:
      episodename = 'Shareholder Meeting'
    elif episodepicker == 12:
      episodename = 'Scott\'s Tots...\nSave yourself and choose again'
    elif episodepicker == 13:
      episodename = 'Secret Santa'
    elif episodepicker == 14:
      episodename = 'The Banker'
    elif episodepicker == 15:
      episodename = 'Sabre'
    elif episodepicker == 16:
      episodename = 'Manager and Salesman'
    elif episodepicker == 17:
      episodename = 'The Delivery: Part 1'
    elif episodepicker == 18:
      episodename = 'The Delivery: Part 2'
    elif episodepicker == 19:
      episodename = 'St. Patrick\'s Day'
    elif episodepicker == 20:
      episodename = 'New Leads'
    elif episodepicker == 21:
      episodename = 'Happy Hour'
    elif episodepicker == 22:
      episodename = 'Secretary\'s Day'
    elif episodepicker == 23:
      episodename = 'Body Language'
    elif episodepicker == 24:
      episodename = 'The Cover-Up'
    elif episodepicker == 25:
      episodename = 'The Chump'
    else:
      episodename = 'Whistleblower'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 7:
    episodepicker = random.randint(1,24)
    if episodepicker == 1:
      episodename = 'Nepotism'
    elif episodepicker == 2:
      episodename = 'Counseling'
    elif episodepicker == 3: 
      episodename = 'Andy\'s Play'
    elif episodepicker == 4:
      episodename = 'Sex Ed'
    elif episodepicker == 5:
      episodename = 'The Sting'
    elif episodepicker == 6:
      episodename = 'Costume Contest'
    elif episodepicker == 7:
      episodename = 'Christening'
    elif episodepicker == 8:
      episodename = 'Viewing Party'
    elif episodepicker == 9:
      episodename = 'WUPHF.com'
    elif episodepicker == 10:
      episodename = 'China'
    elif episodepicker == 11:
      episodename = 'Classy Christmas'
    elif episodepicker == 12:
      episodename = 'Ultimatum'
    elif episodepicker == 13:
      episodename = 'The Seminar'
    elif episodepicker == 14:
      episodename = 'The Search'
    elif episodepicker == 15:
      episodename = 'PDA'
    elif episodepicker == 16:
      episodename = 'Threat Level Midnight'
    elif episodepicker == 17:
      episodename = 'Todd Packer'
    elif episodepicker == 18:
      episodename = 'Garage Sale'
    elif episodepicker == 19:
      episodename = 'Training Day'
    elif episodepicker == 20:
      episodename = 'Michael\'s Last Dundies'
    elif episodepicker == 21:
      episodename = 'Goodbye, Michael'
    elif episodepicker == 22:
      episodename = 'The Inner Circle'
    elif episodepicker == 23:
      episodename = 'Dwight K. Schrute, (Acting) Manager' 
    else:
      episodename = 'Search Committee'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  elif seasonpicker == 8:
    episodepicker = random.randint(1,24)
    if episodepicker == 1:
      episodename = 'The List'
    elif episodepicker == 2:
      episodename = 'The Incentive'
    elif episodepicker == 3:
      episodename = 'Lotto'
    elif episodepicker == 4:
      episodename = 'Garden Party'
    elif episodepicker == 5:
      episodename = 'Spooked'
    elif episodepicker == 6:
      episodename = 'Doomsday'
    elif episodepicker == 7:
      episodename = 'Pam\'s Replacement'
    elif episodepicker == 8:
      episodename = 'Gettysburg'
    elif episodepicker == 9:
      episodename = 'Mrs. California'
    elif episodepicker == 10:
      episodename = 'Christmas Wishes'
    elif episodepicker == 11:
      episodename = 'Trivia'
    elif episodepicker == 12:
      episodename = 'Pool Party'
    elif episodepicker == 13:
      episodename = 'Jury Duty'
    elif episodepicker == 14:
      episodename = 'Special Project'
    elif episodepicker == 15:
      episodename = 'Tallahassee'
    elif episodepicker == 16:
      episodename = 'After Hours'
    elif episodepicker == 17:
      episodename = 'Test the Store'
    elif episodepicker == 18:
      episodename = 'Last Day in Florida'
    elif episodepicker == 19:
      episodename = 'Get the Girl'
    elif episodepicker == 20:
      episodename = 'Welcome Party'
    elif episodepicker == 21:
      episodename = 'Angry Andy'
    elif episodepicker == 22:
      episodename = 'Fundraiser'
    elif episodepicker == 23:
      episodename = 'Turf War'
    else:
      episodename = 'Free Family Portrait Studio'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode
  else:
    episodepicker = random.randint(1,23)
    if episodepicker == 1:
      episodename = 'New Guys'
    elif episodepicker == 2:
      episodename = 'Roy\'s Wedding'
    elif episodepicker == 3:
      episodename = 'Andy\'s Ancestry'
    elif episodepicker == 4:
      episodename = 'Work Bus'
    elif episodepicker == 5:
      episodename = 'Here Comes Treble'
    elif episodepicker == 6:
      episodename = 'The Boat'
    elif episodepicker == 7:
      episodename = 'The Whale'
    elif episodepicker == 8:
      episodename = 'The Target'
    elif episodepicker == 9:
      episodename = 'Dwight Christmas'
    elif episodepicker == 10:
      episodename = 'Lice'
    elif episodepicker == 11:
      episodename = 'Suit Warehouse'
    elif episodepicker == 12:
      episodename = 'Customer Loyalty'
    elif episodepicker == 13:
      episodename = 'Junior Salesman'
    elif episodepicker == 14:
      episodename = 'Vandalism'
    elif episodepicker == 15:
      episodename = 'Couples Discount'
    elif episodepicker == 16:
      episodename = 'Moving On'
    elif episodepicker == 17:
      episodename = 'The Farm'
    elif episodepicker == 18:
      episodename = 'Promos'
    elif episodepicker == 19:
      episodename = 'Stairmageddon'
    elif episodepicker == 20:
      episodename = 'Paper Airplane'
    elif episodepicker == 21:
      episodename = 'Livin\' the Dream'
    elif episodepicker == 22:
      episodename = 'A.A.R.M.'
    else:
      episodename = 'Finale'
    seasonepisode = ('Watch S{0}:E{1} "{2}"'.format(seasonpicker, episodepicker, episodename))
    return seasonepisode

time.sleep(120)

token = #ADD YOUR OWN SECRET TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if 'need an episode' in message.content.lower():
        response = seasonepisodepicker()
        await message.channel.send(response)

client.run(token)
