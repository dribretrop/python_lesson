prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}
total = 0
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
    e_total = prices[key]*stock[key]
    print "this total: %s" % e_total
    total = total + e_total

print total
    