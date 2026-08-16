#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define F first
#define S second
#define _IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);

const ll N=1e6+9,mod=1e9+7,inf=1e18;
string s;
ll n,k;

int main()
{
    _IO;

    ll t;cin>>t;
    while(t--)
    {
        cin>>n>>k;
        cin>>s;
        ll cnt[n];
        memset(cnt,0,sizeof cnt);
        cnt[0]=s[0]-48;
        for(int i=1;i<n;i++)cnt[i]=cnt[i-1]+s[i]-48;
        set<ll>st;
        ll m=min(20LL,k);
        ll msk=0;
        for(int i=k-m;i<k-1;i++)
        {
            msk=(msk<<1);
            msk =msk | (s[i]-48);
        }
        //st.insert(msk);
        //cout<<msk<<" ";
        for(int i=k-1;i<n;i++)
        {
            if( (msk&(1<<(m-1))) )msk=(msk^(1<<(m-1)));
            msk=(msk<<1);
            msk =msk | (s[i]-48);
            ll l=0;
            if(i-m>=0)l=cnt[i-m];
            if(i-k>=0)l-=cnt[i-k];
            if(l==k-m)st.insert(msk);
            //cout<<msk<<" ";
        }
        ll ans=(1<<m);
        msk=(1<<m)-1;
        while(msk>=0)
        {
            if(st.find(msk)==st.end())
               {

                   ans=(((1<<m)-1)^msk);
                   break;
               }
            msk--;
        }
        stack<ll>sc;
        while(ans)
        {
            sc.push(ans%2);
            ans/=2;
        }
        while(sc.size()<k)sc.push(0);
        if(sc.size()>k)cout<<"NO\n";
        else
        {
            cout<<"YES\n";
            while(!sc.empty())
            {
                cout<<sc.top();
                sc.pop();
            }
            cout<<"\n";

        }



    }

}
