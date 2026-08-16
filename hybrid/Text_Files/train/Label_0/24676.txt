#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int n;
long long f[400];
int main()
{
    scanf("%d",&n);
    f[0]=2;
    for(int i=0;i<=n;i++)
    f[i]=f[i-1]*2+2;
    printf("%lld\n",f[n]);
    return 0;
}