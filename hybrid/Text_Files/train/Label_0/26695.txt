#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;

void solve()
{
    int n,l;
    cin>>n;
    int arr[n+1];
    int pos[n+1];
    arr[0]=0;
    pos[0]=0;
    for(int i=1;i<=n;i++)
    {
        cin>>arr[i];
        pos[arr[i]]=i;
    }
    l=n;
    for(int i=n;i>=1;i--)
    {
        if(pos[i]>l)
        continue;
        for(int k=pos[i];k<=l;k++)
        cout<<arr[k]<<" ";
        l=pos[i]-1;
    }
    cout<<"\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--)
    {
        solve();
    }    
    return 0;
}
