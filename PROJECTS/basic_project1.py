from matplotlib import pyplot as plt

# list as database here all info is stored in list
movies=[]

def add_movie():
    title=input("enter movie title:")
    director=input("enter director name:")
    year=input("enter release year:")
    imdb=input("enter imdb rating")
    movies.append({'title':title,
                    'director':director,
                    'year':year,
                    'imdb':imdb
                    })


def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print("name:"movie['title'])
    print("Director:",movie['director'])
    print("Released Year:",movie['year'])
    print("Imdb:",movie['imdb'])
    print()


def find_movie():
    s_title=input("enter title of movie u want to search:")
    for movie in movies:
        if movie['title']==s_title:
            print_movie(movie)

def delete_movie():
    name=input("Enter movie title You want to delete:")
    for movie in movies:
        if movie['title']==name:
            movies.remove(movie)
    print("Your requested Movie is deleted Succesfully.")
def plot_bar():
    count={'>9':0,'>8':0,'>7':0}
    for movie in movies:

        imdb=float(movie['imdb'])
        
        if imdb>=9:
            count['>9']+=1
        elif imdb >=8 and imdb<9:
            count['>8']+=1
        elif imdb>=7 and imdb<8:
            count['>7']+=1

    imdb=list(count.keys())
    noOfMovies=list(count.values())
    fig=plt.figure(figsize=(10,5))
    plt.bar(imdb,noOfMovies,color="maroon",width=0.4)
    plt.xlabel("IMDB RATING")
    plt.ylabel("No. OF MOVIES")
    plt.title("IMDB RATINGS OF MOVIE ")
    plt.show()

User_options={
    'a':add_movie,
    "l":show_movies,
    'f':find_movie,
    'd':delete_movie,
    'p':plot_bar
}

Menu="\na:Add new Movie\n l: Show all movies\n f:find a movie by name\n d:Delete Movie by name\np:Plot\n q: quit the menu\n"

def menu():
    choice=input(Menu)
    while choice!='q':
        if choice in User_options:
            selected_function=User_options[choice]
            selected_function()
        else:
            print("Unknown command please try again.")

        choice=input(Menu)


menu()