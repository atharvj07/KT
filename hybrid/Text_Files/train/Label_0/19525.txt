#include<stdio.h>
int main(){long long int n,a=10,b=0; scanf("%lld\n",&n); if(n%2==0) while(a<=n) b+=n/a, a*=5; printf("%lld\n",b);}