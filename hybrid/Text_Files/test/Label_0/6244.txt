#include<stdio.h>
int main(){int a,b,d;while(scanf("%d %d",&a,&b)!=EOF){d=0;a+=b;while(a>0){a/=10;d++;}printf("%d\n",d);}return 0;}