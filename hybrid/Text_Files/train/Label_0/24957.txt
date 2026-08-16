#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define PI (acos(-1))
#define ct cout<<
#define cn cin>>
#define spc <<" "<<
#define nl puts("")
#define _fl(x) puts("FLAG " #x),fflush(stdout);
#define  _(x)  cout<< #x <<" is "<< x <<endl;
#define fs first
#define sc second
#define pb push_back
#define all(v)  (v).begin(), (v).end()
#define _109 (1000000000)
#define _0(arr) memset(arr,0,sizeof ( arr ) )
#define _1(arr) memset(arr,-1,sizeof ( arr ) )
#define _ninp(n,arr) for(int i=0; i<n;i++)cin>>arr[i];
#define _nout(n,arr) for(int i=0; i<n;i++)cout<<arr[i]<<" \n"[i==n-1];
#define YES(ok) if(ok)cout<<"YES\n";else cout<<"NO\n";
#define yes(ok) if(ok)cout<<"yes\n";else cout<<"yes\n";


int main()
{

    int T;
    cn T;
    for(int caseno = 1; caseno <= T  ; caseno++)
    {
        int n;
        cn n;
        set<int>adj[n + 1];
        for (int i = 0; i < n; ++i)
        {
        	int a,b;
        	cn a>>b;
        	adj[a].insert(b);
        	adj[b].insert(a);
        }

        queue<int> q;
        for (int i = 1; i <= n; ++i)
        {
        	if(adj[i].size()==1)q.push(i);
        }

        int cnt[n+1];
        _0(cnt);

        while(q.size()!=0){
            int u=q.front();q.pop();

            int v=*adj[u].begin();
            adj[v].erase(u);
            if(adj[v].size()==1)q.push(v);
            cnt[v]+=cnt[u]+1;
            cnt[u]=-1;
        }
        
        ll ans=0;
        for (int i = 1; i <=n; ++i)
        {
        	if(cnt[i]==-1)continue;
        	ll x=cnt[i]+1;

        	ans+= (x*(x-1))/2+x*(n-x);
        }

        ct ans;nl;

    }







    return 0;
}
