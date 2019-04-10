from collections import Counter

url = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",    
]

item_list = []

for item in url:
    item_list.append(item.split("/")[-1])

item_counts = Counter(item_list)


top_three = item_counts.most_common(3)
print(top_three)