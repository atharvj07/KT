#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define mk make_pair
#define MOD 1000000007
#define pi 3.1415926536
/* BAAP BAAP HOTA HAI
   AUTHOR- Devansh Nandasana*/
void adde(vector<ll> adj[],ll u,ll v)
{
  adj[u].pb(v);
  adj[v].pb(u);
}
ll modInverse(ll a, ll m)
{
    ll m0=m;
    ll y=0,x=1;
    if(m==1)
      return 0;
    while(a>1)
    {
        ll q=a/m;
        ll t=m;
        m=a%m,a=t;
        t=y;
        y=x-q*y;
        x=t;
    }
    if(x<0)
      x+=m0;
    return x;
}
void BFS(vector<ll> adj[],ll bfs[],ll s,ll n)
{
    bool *visited = new bool[n+1];
    for(ll i=0;i<n+1;i++)
        visited[i] = false;
    list<ll> queue;
    visited[s] = true;
    bfs[s]=0;
    queue.push_back(s);
    vector<ll>::iterator i;
    while(!queue.empty())
    {
        s=queue.front();
        queue.pop_front();
        for(i=adj[s].begin();i!=adj[s].end();++i)
        {
            if(!visited[*i])
            {
                visited[*i] = true;
                bfs[*i]=bfs[s]+1;
                queue.push_back(*i);
            }
        }
    }
}
ll nCrModp(ll n,ll r,ll p)
{
    if (r > n - r)
        r = n - r;
    ll C[r + 1];
    memset(C, 0, sizeof(C));
    C[0] = 1;
    for (ll i = 1; i <= n; i++) {
        for (ll j = min(i, r); j > 0; j--)
            C[j] = (C[j] + C[j - 1]) % p;
    }
    return C[r];
}
ll find_center(ll n,vector<ll> adj[])
{
  queue<ll> q;
  bool vis[n+1];
  ll cnt[n+1];
  for(ll i=1;i<=n;i++)
  {
    vis[i]=false;
    cnt[i]=adj[i].size();
    if(cnt[i]==1)
    q.push(i);
  }
  while(q.size()>1)
  {
    ll cur=q.front();
    vis[cur]=true;
    q.pop();
    for(ll i=0;i<adj[cur].size();i++)
    {
      if(!vis[adj[cur][i]])
      {
        cnt[adj[cur][i]]--;
        if(cnt[adj[cur][i]]==1)
        q.push(adj[cur][i]);
      }
    }
  }
  return q.front();
}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
ll get_rand(ll l, ll r)
{
    uniform_int_distribution<ll> uid(l, r);
    return uid(rng);
}
int main()
{
  #ifndef ONLINE_JUDGE
    freopen("/home/devansh/Desktop/temp/input.txt", "r", stdin);
    freopen("/home/devansh/Desktop/temp/output.txt", "w", stdout);
  #endif
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll t;
  cin>>t;
  vector<ll> two(5000000);
  two[0]=1;
  for(ll i=1;i<5000000;i++)
  {
    two[i]=two[i-1]*2;
    two[i]=two[i]%MOD;
  }
  while(t--)
  {
    ll n,m;
    cin>>n>>m;
    string s[n];
    for(ll i=0;i<n;i++)
      cin>>s[i];
    ll cnt=0,flag=0;
    for(ll i=0;i<n;i++)
    {
      for(ll j=0;j<m;j++)
      {
        if(s[i][j]=='#')
          cnt++;
        else
          flag=1;
      }
    }
    if(flag==0)
      cout<<(two[cnt]-1+MOD)%MOD<<"\n";
    else
      cout<<two[cnt]<<"\n";
  }
  return 0;
}
