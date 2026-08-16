#include<stdio.h>
 
int main(){
  int a, b, t;
  while(1){
    scanf("%d %d\n", &a, &b);
    if(a==0 && b==0)return 0;
    if(a>b){t=a;a=b;b=t;}
    printf("%d %d\n", a, b);
  }
}
