# -- coding: utf-8 -- 

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x         # 输出x本身，也就是说可以输出双引号
print "I also said: '%s'." % y  # 输出y所表示的字符串，无双引号

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
