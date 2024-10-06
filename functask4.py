#example1.
def creategroceryList(item_name,quantity,price):
    print(f'item={item_name}')
    print(f'no_items={quantity}')
    print(f'Price={price}')
    return{
        'item' : item_name,
        'no_items' : quantity,
        'Price' : price,
    }
print()
item1= creategroceryList('Milk','1 litre',50)    

print(f'item1= {item1}')

#example2.

def createbookDetails(title,author,genre,pages):
    print(f'book_name {title}')
    print(f'book_author {author}')
    print(f'book_genre {genre}')
    print(f'book_pages {pages}')
    return{
        'book_name':title,
        'book_author':author,
        'book_genre':genre,
        'book_pages':pages,
    }
print()

book1=createbookDetails('The Alchemist','Paulo Coelho','Fiction',208)
print(f'book1={book1}')