#include<bits/stdc++.h>
#define ll long long
#define rep1(i,a,b) for(int i=a;i<=b;i++)
#define eps 1e-8
#define int_inf 0x3f3f3f3f
#define ll_inf 0x7f7f7f7f7f7f7f7f
#define lson curPos<<1
#define rson curPos<<1|1
using namespace std;
const int maxn=1e5+10;
int fa[maxn],ans=0,n,m;
int find(int x)
{
  return fa[x]==x?x:fa[x]=find(fa[x]);
}
int main()
{
  cin>>n>>m;
  rep1(i,1,n) fa[i]=i;
  rep1(i,1,m)
  {
    int x, y, k;
    cin>>x>>y>>k;
    int px=find(x),py=find(y);
    fa[px]=py;
  }
  rep1(i,1,n) if(find(i)==i) ans++;
  cout<<ans<<'\n';
  return 0;
}
