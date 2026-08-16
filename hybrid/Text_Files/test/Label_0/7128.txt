#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,i,m,x,mn=INT_MAX,s=0;
    cin>>n>>x;
    for(i=0;i<n;i++)
    {
        cin>>m;
        s+=m;
        mn=min(mn,m);
    }
    cout<<n+((x-s)/mn)<<endl;
}
