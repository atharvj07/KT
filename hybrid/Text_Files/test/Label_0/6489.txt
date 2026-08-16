#include<bits/stdc++.h>
using namespace std;
int n,r,x,m=0x3f3f3f3f;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++,r+=(m>x),m=min(m,x))cin>>x;
    cout<<r;
    return 0;
}