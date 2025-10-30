#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, random, datetime, textwrap

DOMAINS = [
    "bottradingai.com","botgame.io","metaversebot.io","nftgameai.com",
    "hubgaming.io","botdefi.io","esportsai.io","nftgamepro.com",
    "botesports.com","aiesports.io","pronftgame.com","botplay.io",
    "botweb3ai.com","botblockchain.io"
]

TOPICS = [
  "AI Rewards Revolutionizing NFT Games",
  "Blockchain Ownership Models in 2025",
  "How AI Empowers Web3 Game Design",
  "The Future of NFT-Based Player Economies",
  "Metaverse Guilds and Decentralized Worlds",
  "Adaptive Storylines with Machine Learning in Games",
  "Play-to-Earn: What Still Works in 2025",
  "Smart Contracts for Player Trust"
]

IMAGES = [
  "https://picsum.photos/1200/630?random=501",
  "https://picsum.photos/1200/630?random=502",
  "https://picsum.photos/1200/630?random=503",
  "https://picsum.photos/1200/630?random=504"
]

INTROS = [
  "In today’s Web3 landscape, games are no longer just entertainment — they’re economic ecosystems.",
  "AI-driven NFT games are changing how digital assets are valued and traded by millions of players."
]

BODIES = [
  "NFT integration has opened a new layer of game ownership and engagement. Players now earn, stake, and evolve their in-game assets through smart contracts.",
  "AI-generated environments and adaptive economies make each session unique. The fusion of AI + blockchain is building valuable virtual economies."
]

CONCLUSIONS = [
  "The intersection of AI and blockchain will continue to drive innovation in gaming through 2025 and beyond.",
  "NFT ecosystems that focus on utility and creativity will dominate the decentralized gaming future."
]

def slugify(s):
    s = s.lower()
    out = []
    for ch in s:
        if ch.isalnum(): out.append(ch)
        else: out.append('-')
    return '-'.join([p for p in ''.join(out).split('-') if p])

def pick_backlinks(n=5):
    choices = [d for d in DOMAINS]
    random.shuffle(choices)
    sel = choices[:n]
    return "\n".join(["- [%s](https://%s)" % (d, d) for d in sel])

def generate_md():
    title = random.choice(TOPICS)
    slug = slugify(title)
    date = datetime.date.today().isoformat()
    image = random.choice(IMAGES)
    intro = random.choice(INTROS)
    body1 = random.choice(BODIES)
    body2 = random.choice(BODIES)
    conclusion = random.choice(CONCLUSIONS)
    backlinks = pick_backlinks()

    # We add the ad include as Liquid include (Jekyll will process)
    ad_include = "{% include ad.html %}"

    content = textwrap.dedent("""\
    ---
    layout: post
    title: "{title}"
    date: {date}
    author: "NFTGameAI Team"
    description: "Auto insight on NFT gaming"
    image: "{image}"
    ---

    _This post was auto-generated._

    ![{title}]({image})

    {ad_include}

    {intro}

    {body1}

    {body2}

    ### Key Insights
    - AI-driven economy and fair distribution
    - Player-owned NFT ecosystems
    - Transparent gameplay and smart rewards

    ### Friendly Network
    {backlinks}

    **Conclusion:** {conclusion}
    """.format(
        title=title,
        date=date,
        image=image,
        ad_include=ad_include,
        intro=intro,
        body1=body1,
        body2=body2,
        backlinks=backlinks,
        conclusion=conclusion
    ))

    filename = "_posts/%s-%s.md" % (date, slug)
    return filename, content

def main():
    os.makedirs("_posts", exist_ok=True)
    fn, txt = generate_md()
    with open(fn, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Wrote:", fn)

if __name__ == "__main__":
    main()
