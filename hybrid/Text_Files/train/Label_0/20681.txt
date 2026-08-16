#include<bits/stdc++.h>
using namespace std;
#define lli long long int
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);
#define test lli t;cin>>t;while(t--)
#define vll vector<lli>
#define mll map<lli,lli>
#define vvll vector<vector<lli>>
#define vpll vector<pair<lli,lli>>
#define vvpll vector<vector<pair<lli,lli>>>
#define mpll map<pair<lli,lli>,lli>
#define psq priority_queue<ll>  //max-heap
#define prq priority_queue<ll,vector<ll>,greater<ll>>  //min-heap
#define pll pair<lli,lli>
#define stll stack<lli>
#define sll set<lli>
#define qll queqe<lli>
#define pb push_back
#define bs binary_search
#define lb lower_bound
#define ub upper_bound
#define ff first
#define ss second
#define nl "\n"
#define ms0(s) memset(s,0,sizeof(s))
#define mod 1000000007
#define ma 1000000000000000000
#define mi -1000000000000000000
int main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  fastio
  test
  {
    lli n, i, j;
    cin >> n;
    lli a[n];
    set<lli>s;

    for (i = 0; i < n; i++)
      cin >> a[i];
    for (i = 0; i < n; i++)
    {
      for (j = i + 1; j < n; j++)
        s.insert(a[j] - a[i]);
    }
    cout << s.size() << endl;
  }
  return 0;
}