product={
    101:{
        "productname":"car",
        "price":1000,
        "color":"black",
        "qty":10,
        "models":[501,502]
    }
}

print(product[101]["color"])

#key
for key in product.values():
    print(key)

for v in product.values():
    for k, v in v.values():
        print(k,v)
