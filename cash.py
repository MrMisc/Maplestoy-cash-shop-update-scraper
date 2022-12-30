
@client.command(brief = "<printimages =0 by default>", description = "Putting any other value than 0 in the first parameter allows you to see all of the NX images inside the site, give it a go!")
async def ms_cash(ctx, printimages = 0):
    stock = 'https://maplestory.nexon.net/'
    animalswikia = 'https://maplestory.nexon.net/news/sale#news-filter'
    Req = Request(animalswikia)
    uClient = urlopen(Req)
    soup = BeautifulSoup(uClient.read(), 'html5lib')
    soup_filt = soup.find('div', {'class', 'news-wrapper'})
    animalswikia = stock+soup_filt.find_all('div', {'class', 'text'})[0].a['href']
    Req = Request(animalswikia)
    uClient = urlopen(Req)
    soup = BeautifulSoup(uClient.read(), 'html5lib')
    det = None
    for i in soup.find_all('h1', {'style':'text-align: center;'}):
        if(i.text == 'ONGOING SALES'):
            print(i)
            det = str(i)
            break
    soup = BeautifulSoup(str(soup).split(det)[0])
    listofimages = [image['src'] for image in soup.find_all('img') if image.has_attr('alt') if image['src'].__contains__('logo') == False]
    colours = [0xE5FCC2, 0x9DE0AD   , 0x45ADA8, 0x68829E   , 0x547980   , 0x594F4F , 0x453f3f, 0x2A3132 ]
    emb = discord.Embed(title = f"{soup.find_all('h1', {'class', 'title'})[0].text}", color = 0x594F4F)
    emb.add_field(name = 'Cash Shop Link', value = f'{animalswikia}' )
    emb.set_author(name = "Maple")
    emb.set_image(url = f'{listofimages[0]}')
    listofimages.pop(0)
    await ctx.send(content = None, embed = emb)
    if printimages != 0:
        for j in listofimages:
            await ctx.send(j)
