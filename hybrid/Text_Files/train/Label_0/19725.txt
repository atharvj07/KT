/**
 * Prof.Nicola
**/
#include <bits/stdc++.h>

using namespace std;
vector<long long>tree;
long long mod=1e9+7;
long long power_of_two(long long x)
{
    long long z=0;
    while(x>1){
        x/=2;
        z++;
    }
    return z;
}
long long power(long long x,long long p)
{
    if(p==0){
        return 1;
    }
    long long z=power(x,p/2);
    z=(z*z)%mod;
    if(p%2==1){
        z=(z*x)%mod;
    }
    return z;
}
void segment_tree(vector<long long>v)
{
    long long x=v.size();
    x=power_of_two(x);
    x=power(2,x);
    if(v.size()!=x){
        x*=2;
    }
    tree.resize(x*2);
    tree[0]=x;
    for(long i=0;i<v.size();i++){
        tree[i+x]=v[i];
    }
    for(long i=x-1;i>0;i--){
        tree[i]=min(tree[i*2],tree[(i*2)+1]);
    }
}
long long seg(long long l,long long r)
{
    l+=tree[0];
    r+=tree[0];
    long long ans=1e9;
    while(l<=r){
        if(l%2==1){
            ans=min(ans,tree[l]);
        }
        if(r%2==0){
            ans=min(ans,tree[r]);
        }
        l++;
        l/=2;
        r--;
        r/=2;
    }
    return ans;
}
void update(long long x,long long z)
{
    x+=tree[0];
    tree[x]=z;
    x/=2;
    while(x>0){
        tree[x]=min(tree[x*2],tree[(x*2)+1]);
        x/=2;
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long t,n,mn,mx,x,z,a,b,c;
    cin>>t;
    for(long i=0;i<t;i++){
        cin>>n;
        mx=0;
        tree.clear();
        bool ok=false;
        vector<long long>v(n+1);
        map<long long,bool>vis;
        map<long long,vector<long long> >pos;
        map<long long,pair<long,long> >mp1,mp2;
        for(long j=1;j<=n;j++){
            cin>>x;
            v[j]=x;
            pos[x].push_back(j);
            if(x>mx){
                mx=x;
                mp1[mx].first=j;
            }
            mp1[mx].second=j;
        }
        mx=0;
        for(long j=n;j>0;j--){
            x=v[j];
            if(x>mx){
                mx=x;
                mp2[mx].first=j;
            }
            mp2[mx].second=j;
        }
        segment_tree(v);
        for(long j=1;j<=n;j++){
            if(vis[v[j]]){
                continue;
            }
            vis[v[j]]=true;
            x=mp1[v[j]].second;
            z=mp2[v[j]].second;
            if(x==0||z==0){
                continue;
            }
            mx=1e12;
            if(x<z){
                mx=seg(x+1,z-1);
                if(mx==v[j]){
                    ok=true;
                    a=x;
                    b=z-1-x;
                    c=n-a-b;
                    break;
                }
            }
            if(mx>v[j]&&pos[v[j]].size()>2){
                for(long k=1;k<pos[v[j]].size()-1;k++){
                    if(seg(min(x+1,pos[v[j]][k]),max(z-1,pos[v[j]][k]))==v[j]){
                        ok=true;
                        a=min(x,pos[v[j]][k]-1);
                        b=max(z-1,pos[v[j]][k])-a;
                        c=n-a-b;
                        break;
                    }
                }
            }
        }
        if(!ok){
            cout<<"NO"<<endl;
        }
        else{
            cout<<"YES"<<endl;
            cout<<a<<" "<<b<<" "<<c<<endl;
        }
    }
    return 0;
}
