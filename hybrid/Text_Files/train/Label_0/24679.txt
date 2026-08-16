#include<bits/stdc++.h>
using namespace std;
long long f[105],X;                 
int main(){
    cin>>X;
    f[0]=2;
    for(int i=1;i<=X;i++) 
        f[i]=f[i-1]*2+2;
    cout<<f[X]<<endl;
    return 0;
}