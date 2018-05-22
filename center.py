import media
import fresh_tomatoes


Agn = media.movie(
    "Agnyathavaasi",
    "powerstar venky ",
    "https://www.25cineframes.com/images/gallery/2017/09/pawan-kalyan-trivikram-srinivas-pspk25-movie-first-look-all-ultra-hd-posters-wallpapers/54-Pawan-Kalyan-Agnathavasi-Movie-First-Look-ULTRA-HD-Posters-WallPapers.jpg",
    "https://www.youtube.com/embed/97h9fBWltBM")
NPSNIN = media.movie(
    "Na Peru Surya Na illu India", "Brave man",
    "https://files.prokerala.com/movies/pics/728w/naa-peru-surya-poster-84822.jpg",
    "https://www.youtube.com/embed/ZnVIUr_BQSs")
KAY = media.movie("Krishna arjuna yuddham",
                  "Krish and arjun brothers war for heroines",
                  "https://files.prokerala.com/movies/pics/728w/ugadi-wishes-poster-85599.jpg",
                  "https://www.youtube.com/embed/7A1Y1ExiQRw")
BAN = media.movie(
    "Bharath Ane Nenu", "Cm",
    "https://files.prokerala.com/movies/pics/728w/bharath-ane-nenu-poster-83322.jpg",
    "https://www.youtube.com/embed/KMWS5y2gZ6E")
Rangasthalam = media.movie(
    "rangathalam", "Finding president",
    "https://files.prokerala.com/movies/pics/728w/rangasthalam-new-posters-85600.jpg",
    "https://www.youtube.com/embed/mhhb6JAJKbE")

movies = [Agn,NPSNIN, KAY, BAN, Rangasthalam]
fresh_tomatoes.open_movies_page(movies)
