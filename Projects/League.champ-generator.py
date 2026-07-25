import random

tops = ["Aatrox", "Akali", "Ambessa", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gragas", "Gwen", "Illaoi", "Irelia", "Jax", "Kayle", "K'Sante", "Kennen", "Kled", "Malphite", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett", "Shen", "Singed", "Sion", "Tahm Kench", "Teemo", "Trundle", "Tryndamere", "Urgot", "Vladimir", "Volibear", "Warwick", "Yone", "Yorick"]
junglers = ["Amumu", "Bel'Veth", "Briar", "Diana", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Karthus", "Kayn", "Kindred", "Kha'Zix", "Lee Sin", "Lillia", "Master Yi", "Nidalee", "Nocturne", "Nunu", "Rek'Sai", "Rengar", "Rumble", "Sejuani", "Shaco", "Shyvana", "Skarner", "Taliyah", "Talon", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Xin Zhao", "Zac"]
mids = ["Ahri", "Akali", "Anivia", "Annie", "Aurelion Sol", "Azir", "Cassiopeia", "Corki", "Diana", "Ekko", "Fizz", "Galio", "Hwei", "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Naafiri", "Neeko", "Orianna", "Qiyana", "Ryze", "Sylas", "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Yone", "Zed", "Ziggs"]
adcs = ["Aphelios", "Ashe", "Caitlyn", "Corki", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Nilah", "Samira", "Senna", "Sivir", "Smolder", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Zeri"]
supports = ["Alistar", "Bard", "Blitzcrank", "Braum", "Janna", "Karma", "Leona", "Lulu", "Lux", "Maokai", "Milio", "Morgana", "Nami", "Nautilus", "Pyke", "Rakan", "Rell", "Renata Glasc", "Senna", "Seraphine", "Sona", "Soraka", "Swain", "Tahm Kench", "Taric", "Thresh", "Vel'Koz", "Xerath", "Yuumi", "Zilean", "Zyra"]

roles = {
    "Top": tops,
    "Jungle": junglers,
    "Mid": mids,
    "ADC": adcs,
    "Support": supports
}

used_champions = []

for role in roles:
    champion = random.choice(roles[role])

    while champion in used_champions:
        champion = random.choice(roles[role])

    used_champions.append(champion)

    print(role, "-", champion)


