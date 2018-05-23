import media
import fresh_tomatoes


Agn = media.movie(
    "Agnyathavaasi",
    "powerstar venky ",
    "https://bit.ly/2s2Yi53",
    "https://www.youtube.com/embed/97h9fBWltBM")
NPSNIN = media.movie(
    "Na Peru Surya Na illu India", "Brave man",
    "https://bit.ly/2LoovnC",
    "https://www.youtube.com/embed/ZnVIUr_BQSs")
KAY = media.movie("Krishna arjuna yuddham",
                  "Krish and arjun brothers war for heroines",
                  "https://bit.ly/2IC4sUF",
                  "https://www.youtube.com/embed/7A1Y1ExiQRw")
BAN = media.movie(
    "Bharath Ane Nenu", "Cm",
    "https://bit.ly/2x23iMQ",
    "https://www.youtube.com/embed/KMWS5y2gZ6E")
Rangasthalam = media.movie(
    "rangathalam", "Finding president",
    "https://bit.ly/2s52wcf",
    "https://www.youtube.com/embed/mhhb6JAJKbE")

movies = [Agn, NPSNIN, KAY, BAN, Rangasthalam]
fresh_tomatoes.open_movies_page(movies)