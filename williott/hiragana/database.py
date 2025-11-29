from pydantic import BaseModel


class Hiragana(BaseModel):
    character: str
    word: str
    romaji: str
    hiragana: str
    image: str


db = {
    "あ": [
        Hiragana(
            character="あ",
            word="アルパカ",
            romaji="arupaka",
            hiragana="あるぱか",
            image="arupaka.png",
        ),
        Hiragana(
            character="あ",
            word="浣熊",
            romaji="araiguma",
            hiragana="あらいぐま",
            image="araiguma.png",
        ),
    ],
    "い": [
        Hiragana(
            character="い", word="犬", romaji="inu", hiragana="いぬ", image="inu.png"
        )
    ],
    "う": [
        Hiragana(
            character="う", word="馬", romaji="uma", hiragana="うま", image="uma.png"
        ),
        Hiragana(
            character="う",
            word="兎",
            romaji="usagi",
            hiragana="うさぎ",
            image="usagi.png",
        ),
        Hiragana(
            character="う", word="牛", romaji="ushi", hiragana="うし", image="ushi.png"
        ),
    ],
    "え": [
        Hiragana(
            character="え", word="蝦", romaji="ebi", hiragana="えび", image="ebi.png"
        )
    ],
    "お": [
        Hiragana(
            character="お",
            word="狼",
            romaji="ookami",
            hiragana="おおかみ",
            image="ookami.png",
        )
    ],
    # か行
    "か": [
        Hiragana(
            character="か",
            word="カバ",
            romaji="kaba",
            hiragana="かば",
            image="kaba.png",
        )
    ],
    "き": [
        Hiragana(
            character="き",
            word="キリン",
            romaji="kirin",
            hiragana="きりん",
            image="kirin.png",
        )
    ],
    "く": [
        Hiragana(
            character="く", word="熊", romaji="kuma", hiragana="くま", image="kuma.png"
        ),
        Hiragana(
            character="く",
            word="黒豹",
            romaji="kurohyou",
            hiragana="くろひょう",
            image="kurohyou.png",
        ),
    ],
    "け": [
        Hiragana(
            character="け",
            word="毛虫",
            romaji="kemushi",
            hiragana="けむし",
            image="kemushi.png",
        )
    ],
    "こ": [
        Hiragana(
            character="こ",
            word="蝙蝠",
            romaji="koumori",
            hiragana="こうもり",
            image="koumori.png",
        ),
    ],
    # さ行
    "さ": [
        Hiragana(
            character="さ", word="サイ", romaji="sai", hiragana="さい", image="sai.png"
        )
    ],
    "し": [
        Hiragana(
            character="し",
            word="シマウマ",
            romaji="shimauma",
            hiragana="しまうま",
            image="shimauma.png",
        )
    ],
    "す": [
        Hiragana(
            character="す",
            word="西瓜",
            romaji="suika",
            hiragana="すいか",
            image="suika.png",
        )
    ],
    "せ": [
        Hiragana(
            character="せ",
            word="セイウチ",
            romaji="seiuchi",
            hiragana="せいうち",
            image="seiuchi.png",
        )
    ],
    "そ": [
        Hiragana(
            character="そ",
            word="掃除機",
            romaji="soujiki",
            hiragana="そうじき",
            image="soujiki.png",
        )
    ],
    "ぞ": [
        Hiragana(
            character="ぞ", word="蔵", romaji="zou", hiragana="ぞう", image="zou.png"
        )
    ],
    # た行
    "た": [
        Hiragana(
            character="た",
            word="タヌキ",
            romaji="tanuki",
            hiragana="たぬき",
            image="tanuki.png",
        )
    ],
    "ち": [
        Hiragana(
            character="ち",
            word="蝶",
            romaji="chou",
            hiragana="ちょう",
            image="chou.png",
        )
    ],
    "つ": [
        Hiragana(
            character="つ",
            word="燕",
            romaji="tsubame",
            hiragana="つばめ",
            image="tsubame.png",
        )
    ],
    "て": [
        Hiragana(
            character="て",
            word="瓢虫",
            romaji="tentoumushi",
            hiragana="てんとうむし",
            image="tentoumushi.png",
        )
    ],
    "と": [
        Hiragana(
            character="と",
            word="トナカイ",
            romaji="tonakai",
            hiragana="となかい",
            image="tonakai.png",
        )
    ],
    # な行
    "な": [
        Hiragana(
            character="な",
            word="蛞蝓",
            romaji="namekuji",
            hiragana="なめくじ",
            image="namekuji.png",
        )
    ],
    "に": [
        Hiragana(
            character="に",
            word="ニワトリ",
            romaji="niwatori",
            hiragana="にわとり",
            image="niwatori.png",
        )
    ],
    "ぬ": [
        Hiragana(
            character="ぬ", word="ヌー", romaji="nuu", hiragana="ぬー", image="nuu.png"
        )
    ],
    "ね": [
        Hiragana(
            character="ね", word="猫", romaji="neko", hiragana="ねこ", image="neko.png"
        )
    ],
    "の": [
        Hiragana(
            character="の", word="蚤", romaji="nomi", hiragana="のみ", image="nomi.png"
        )
    ],
    # は行
    "は": [
        Hiragana(
            character="は",
            word="針鼠",
            romaji="harinezumi",
            hiragana="はりねずみ",
            image="harinezumi.png",
        )
    ],
    "ひ": [
        Hiragana(
            character="ひ",
            word="羊",
            romaji="hitsuji",
            hiragana="ひつじ",
            image="hitsuji.png",
        )
    ],
    "ふ": [
        Hiragana(
            character="ふ",
            word="梟",
            romaji="fukurou",
            hiragana="ふくろう",
            image="fukurou.png",
        )
    ],
    "へ": [
        Hiragana(
            character="へ",
            word="蛇",
            romaji="hebi",
            hiragana="へび",
            image="hebi.png",
        )
    ],
    "ほ": [
        Hiragana(
            character="ほ",
            word="螢",
            romaji="hotaru",
            hiragana="ほたる",
            image="hotaru.png",
        )
    ],
    # ま行
    "ま": [
        Hiragana(
            character="ま",
            word="マグロ",
            romaji="maguro",
            hiragana="まぐろ",
            image="maguro.png",
        )
    ],
    "み": [
        Hiragana(
            character="み",
            word="ミミズ",
            romaji="mimizu",
            hiragana="みみず",
            image="mimizu.png",
        )
    ],
    "む": [
        Hiragana(
            character="む",
            word="ムカデ",
            romaji="mukade",
            hiragana="むかで",
            image="mukade.png",
        )
    ],
    "め": [
        Hiragana(
            character="め",
            word="メダカ",
            romaji="medaka",
            hiragana="めだか",
            image="medaka.png",
        )
    ],
    "も": [
        Hiragana(
            character="も",
            word="土竜",
            romaji="mogura",
            hiragana="もぐら",
            image="mogura.png",
        )
    ],
    # や行
    "や": [
        Hiragana(
            character="や",
            word="ヤモリ",
            romaji="yamori",
            hiragana="やもり",
            image="yamori.png",
        )
    ],
    "ゆ": [
        Hiragana(
            character="ゆ",
            word="雪豹",
            romaji="yukihyou",
            hiragana="ゆきひょう",
            image="yukihyou.png",
        )
    ],
    "よ": [
        Hiragana(
            character="よ",
            word="幼虫",
            romaji="youchuu",
            hiragana="ようちゅう",
            image="youchuu.png",
        )
    ],
    "ら": [
        Hiragana(
            character="ら",
            word="駱駝",
            romaji="rakuda",
            hiragana="らくだ",
            image="rakuda.png",
        )
    ],
    "り": [
        Hiragana(
            character="り",
            word="栗鼠",
            romaji="risu",
            hiragana="りす",
            image="risu.png",
        )
    ],
    "る": [
        Hiragana(
            character="る",
            word="ルバーブ",
            romaji="rubaabu",
            hiragana="ルバーぶ",
            image="rubaabu.png",
        )
    ],
    "れ": [
        Hiragana(
            character="れ",
            word="レッサーパンダ",
            romaji="ressaapanda",
            hiragana="れっさーぱんだ",
            image="ressaapanda.png",
        )
    ],
    "ろ": [
        Hiragana(
            character="ろ",
            word="驢馬",
            romaji="roba",
            hiragana="ろば",
            image="roba.png",
        )
    ],
    "わ": [
        Hiragana(
            character="わ",
            word="ワニ",
            romaji="wani",
            hiragana="わに",
            image="wani.png",
        ),
    ],
    "を": [
        Hiragana(
            character="を",
            word='猫<break strength="weak"/>を>飼う',
            romaji="neko wo kau",
            hiragana="ねこをかう",
            image="neko_wo_kau.png",
        ),
    ],
    "ん": [
        Hiragana(
            character="ん",
            word="ライオン",
            romaji="raion",
            hiragana="らいおん",
            image="raion.png",
        ),
    ],
    "ご": [
        Hiragana(
            character="こ",
            word="ゴリラ",
            romaji="gorira",
            hiragana="ごりら",
            image="gorira.png",
        ),
    ],
}
