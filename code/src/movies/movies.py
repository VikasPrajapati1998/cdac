def get_year_dict():
    '''
    This function will read file and get year and count total movie release in that year.
    Args : None
    
    Returs: 
        dict {Year : number}
    Raise:
        AnyError : If anything bad happen.
    '''
    year_list = []
    with open("../data/movies_data.txt", 'r') as file:
        while True :
            line = file.readline()
            if line == '':
                break
            year = line.split("::")[1].split()[-1].strip()[1:-1]
            year_list.append(int(year))
    
    year_dict = {}
    unique_year = list(set(year_list))
    for i in unique_year:
        count=0
        for j in year_list:
            if i==j:
                count += 1
        else:
            year_dict[i] = count
    return year_dict

def movie_names():
    '''
    Count total number of movies release with letter 'T' and 'J'
    Args: None
    Returns:
        count (int)
    Raises:
        AnyError : If anything bad happen.
    '''
    count=0
    with open("../data/movies_data.txt", 'r') as file:
        while True :
            line = file.readline()
            if line == '':
                break
            movie_name = line.split("::")[1].strip()
            if movie_name.startswith('T') or movie_name.startswith('J'):
                count += 1
    return count
            
def count_movies():
    '''
    Count all comedy movies release in 1995 and action movies released in 1993
    Args: None
    Returns: (tuple)
    Raises: 
        AnyError : If anythings bad happends
    '''
    comedy, action = 0, 0
    with open("../data/movies_data.txt", 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            movie = line.split("::")
            year = movie[1].split()[-1].strip()
            gener = movie[-1].split("|")
            # print(year, gener)
            if year=="(1995)" and ("Comedy" in gener or "Comedy\n" in gener):
                comedy += 1
            
            if year=="(1993)" and ("Action" in gener or "Action\n" in gener):
                action += 1
    return (comedy, action)

def Batman_movies():
    '''
    Count total number of movies of Batman.
    Args: None
    Returns: count(int)
    Raises: 
        AnyError : If anything bad happen
    '''
    count=0
    with open("../data/movies_data.txt", 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            movie = line.split("::")[1].strip()
            if movie.startswith("Batman") or movie.startswith("batman"):
                # print(movie)
                count += 1
    return count
    

__author__      = "Vikas Prajapati"
__copyright__   = "Copyright 2023, CDAC-PGDBDA, Bangalore"