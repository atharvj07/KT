#include <stdio.h>

int main(){
int W;
int H;
int x;
int y;
int r;
scanf("%d %d %d %d %d\n",&W,&H,&x,&y,&r);
if(0<=x-r && x+r<=W && 0<=y-r && y+r<=H){
printf("Yes\n");
}
else{
printf("No\n");
}
}

