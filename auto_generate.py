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

def slugify(s):
    s = s.lower()
    allowed = []
    for ch in s:
        if ch.isalnum(): allowed.append(ch)
        else: allowed.append('-')
    s2 = ''.join(allowed)
    parts = [p for p in s2.split('-') if p]
    return '-'.join(parts)[:60]

def pick_backlinks(n=5):
    choices = list(DOMAINS)
    random.shuffle(choices)
    return "\n".join(["- [%s](https://%s)" % (d, d) for d in choices[:n]])

def generate_md():
    title = random.choice(TOPICS)
    slug = slugify(title)
    date = datetime.date.today().isoformat()
    image = random.choice(IMAGES)
    intro = "In today’s Web3 landscape, games are not just entertainment — they are economies."
    body1 = "NFT integration and smart contracts create new ways to reward players and sustain communities."
    body2 = "AI-driven personalization will keep players engaged while offering fair distribution of rewards."
    conclusion = "The intersection of AI and blockchain will drive the next wave of gaming innovation."

    # Use literal Liquid include string — we ensure we do NOT pass this into str.format placeholders.
    ad_tag = "{% include ad.html %}"

    markdown = textwrap.dedent("""\
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

    {ad_tag}

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
    """).format(
        title=title.replace('"', "'"),
        date=date,
        image=image,
        ad_tag=ad_tag,
        intro=intro,
        body1=body1,
        body2=body2,
        backlinks=pick_backlinks(),
        conclusion=conclusion
    )

    filename = "_posts/%s-%s.md" % (date, slug)
    return filename, markdown

def main():
    os.makedirs("_posts", exist_ok=True)
    fn, md = generate_md()
    with open(fn, "w", encoding="utf-8") as f:
        f.write(md)
    print("Wrote:", fn)

if __name__ == "__main__":
    main()
