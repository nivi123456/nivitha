try:
    f=open('filedemo.txt')
    f.write('neela and nivitha are good friends')
except:
    print('something went wrong')
finally:
    f.close()
