#include<bits/stdc++.h>
using namespace std;

bool vis[31625];
vector<int> prime;
int factor(int n)
{
    int cnt=0;
    for(auto x: prime)
    {
        if(n<x)
        break;
        while(n%x==0)
        {
            n=n/x;
            cnt++;
        }
    }
    if(n>1)
    cnt++;
    return cnt;
}
void seive(int n)
{
    for(int i=2;i*i<=n;i++)
    {
        if(vis[i]==0)
        {
            for(int j=i*i;j<=n;j+=i)
            {
                vis[j]=1;
            }
        }
    }
    for(int i=2;i<=n;i++)
    {
        if(vis[i]==0)
        {
            prime.push_back(i);
        }
    }
}
int gcd(int x,int y)
{
    if(y==0)
    return x;
    
    return gcd(y,x%y);
}
void solve()
{
    int a,b,k;
    cin>>a>>b>>k;
    int gcd1,maxopr=0;
    if(k>60)
    {
        cout<<"NO\n";
    }
    else
    {
        int mnopr=0;
        if(a==b)
        {
            mnopr=2;
        }
        else
        {
            if(a%b==0 || b%a==0)
            {
                mnopr=1;
            }
            else
            {
                mnopr=2;
            }
        }
        gcd1=gcd(a,b);
        a=a/gcd1;
        b=b/gcd1;
        
        
        maxopr=maxopr+factor(a)+factor(b)+2*factor(gcd1);
        if(k<=maxopr &&  k>=mnopr)
        {
            cout<<"YES\n";
        }
        else
        {
            cout<<"NO\n";
        }
    }
    cout<<"\n";
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    seive(31624);
    int t;
    cin>>t;
    while(t--)
    {
        solve();
    }
}
