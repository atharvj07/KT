#include<stdio.h>
int main()
{
    int x,t;
    scanf("%d %d",&x,&t);
    printf("%d",x-t<0?0:x-t);
    return 0;
}
