h = int(input())
x = int(input())
y = int(input())

if (x>0 and x<3*h and y>0 and y<h) or (x>h and x<2*h and y>h and y<4*h) or (y==h and x>h and x<2*h):
    print('inside')
elif (x==0 and y>=0 and y<=h) or (y==0 and x>=0 and x<=3*h) or (x==3*h and y>=0 and y<=h) or (y==h and x>=2*h and x<=3*h) or (x==2*h and y>=h and y<=4*h) or (y==4*h and x>=h and x<=2*h) or (x==h and y>=h and y<=4*h) or (y==h and x>=0 and x<=h):
    print('border')
else:
    print('outside')