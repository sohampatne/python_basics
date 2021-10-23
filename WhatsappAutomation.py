import pywhatkit
from random import randint

thoughts = [
    'The less you respond to negative people, the more peaceful your life will become,Stay positive and tune out the '
    'negativity in your life.Good Morning!',
    'Life is like making tea,Boil your ego,Evaporate your worries,dilute your sorrow,filter your mistakes & get taste '
    'of happiness.Good Morning!',
    'Happy Morning, Never give up on the things that make you smile.',
    'The most beautiful things in life are not things,They\'re people and places, memories and pictures,'
    'They\'re feelings and moments, right hugs, smiles and laughter.Good Morning!',
    'The problem with nice people is that they will not tell you that they are hurt,they will wait for you to realize '
    'your mistake.Good morning!',
    'It\'s better to be alone than to be with those who hinder your progress.Good Morning!',
    'Don\'t wait for someone to bring you flowers.Plant your own garden and decorate your own soul.Good Morning!',
    'Understand that you own nothing, everything that surrounds you is temporary, only the love in your heart will '
    'last forever.Good Morning!',
    'The sweetest moment in life comes not with the greetings you receive but with the thought that someone wishes '
    'the best for you.Good Morning!',
    'Don\'t downgrade your dream to match your reality,upgrade your faith to match your destiny.Be happy always.'
    'Every moment has love in it,Every hour has happiness in it,If you loose it, it becomes memory,And if you live '
    'it, it becomes life.Good Morning!',
    'Life is a gift,Wake up every day and realize that.Good Morning!',
    'Positive thoughts are not enough,There has to be positive feelings & positive actions.Have a lovely day!',
    'People will like your problems and comment, but no one will solve them because everyone is busy updating '
    'theirs.Good Morning!',
    'Sending a smile your way Have an awesome day!A smile can open a heart faster than a key can open a door.Smiles '
    'are free, so don\'t save them.Brighten the world with your smile.Good Morning!',
    'Respect is like a mirror.The more you show it to other people, the more it will reflect back on you.'
    'The soul that care deeply,The heat that loves gorgeously,And a mind that lives simply,Is what I wish you from me '
    'today & forever.Good Morning! '
    'One hand of help,One word of sympathy,One act of humanity,One smile of charity, & one sweet hello, can change '
    'someone\'s mood & life.Good Morning! '
    'Sometimes it\'s very hard to move on, but once you move on, you\'ll realize it was the best decision you\'ve '
    'ever made.Good Morning!',
    'Health does not always come from medicine,Most of the time it comes from peace of mind, peace in the heart, '
    'peace of soul,It comes from laughter and love.Good Morning!',
    'The importance of good people in our life is just like the importance of heartbeats,It\'s not visible but '
    'silently support our life,Have a blessed Day, Good Morning!',
    'वक्त और हालात सदा बदलते रहते है,\nलेकिन अच्छे रिश्ते और सच्चे दोस्त,\nकभी नही बदलते। सुप्रभात!',
    'जिन्दगी मिली है जीने के लिए,\nउसको हंस के जियो,\nक्योकि आपको, खुश देखकर,\nहम भी तो खुश होते हैं।\nआपका दिन शुभ हो!',
    'रिश्ते मन से बने है, बातो से नहीं,\nकुछ लोग बहुत सी बातो के,\nबाद भी अपने नही होते,\nकुछ लोग शांत रहकर भी,'
    '\nअपने बन जाते है।\nसुप्रभात!',
    'तमत्रा करते हो जिन खुशियों की,\nदुआ है वह खुशियां आपके कदमो में हो,\nखुदा आपको वह सब हक़ीक़त में दे,\nजो कुछ आपके '
    'सपनो में हो।\nसुप्रभात!',
    'ना मंदिर में छुपा है, ना मस्जिद में छुपा है,\nजिसके दिल में इंसानियत है उस दिल में खुदा है।\nसुप्रभात!',
    'आपकी नई सुबह इतनी सुहानी हो जाए,\nआपके दुःखों की सारी बातें पुरानी हो जाएं,\nदे जाए इतनी खुशियां ये दिन आपको,'
    '\nकि खुशी भी आपकी मुस्कुराहट की दीवानी हो जाए।\nसुप्रभात!',
    'अच्छे मित्र,अच्छे रिश्तेदार,\nऔर अच्छे विचार,जिसके पास होते है,\nउसे दुनिया की कोई भी ताकत,\nहरा नहीं '
    'सकती।\nसुप्रभात!',
    'ईश्वर के हर फैसले पे खुश रहो,\nक्योंकि,ईश्वर वो नहीं देता,\nजो आपको अच्छा लगता है,\nबल्कि,ईश्वर वो देता है,'
    '\nजो आपके लिए अच्छा होता है।',
    'एक और सुबह जा रही जिंदगी की,\nएक और दिन आ रहा जिंदगी का,\nये मत सोचो की कितने लम्हे है जिंदगी में,\nये सोचो '
    'कितनी जिंदगी है हर लम्हो में।\nसुप्रभात!',
    'जीवन का इम्तिहान आसान नहीं होता,\nबिना संघर्ष कोई महान नहीं होता,\nजब तक ना पड़े हतोड़े की मार,\nतब तक तो पत्थर भी '
    ' भगवान नहीं होता।\nसुप्रभात! '
]
index = len(thoughts) -1

pywhatkit.sendwhatmsg('+919049244411', 'Hi mom! how are you? LOL!', 18, 47)