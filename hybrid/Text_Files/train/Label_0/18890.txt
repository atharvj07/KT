#include <bits/stdc++.h>
using namespace std;
const int MX=1e5+5;
pair<long long,int> a[MX];
map<long long,int> mp;
long long n;
int p[MX];
int visit[MX];
long long s[MX];
long long dp[MX];
int main(){
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);
    cin>>n;
    int i;
    for(i=1 ; i<=n ; i++){
        cin>>a[i].first;
      ///  a[i].first++;
        a[i].second=i;
        mp[a[i].first]=i;
    }
    sort(a+1,a+n+1);
    for(i=n ; i>=2 ; i--){
      ///  cout<<i<<endl;
        s[a[i].second]++;

        int k=mp[a[i].first+2*s[a[i].second]-n];
        if(k==0 || k==a[i].second || a[i].first+2*s[a[i].second]-n>=a[i].first){
            cout<<-1;
            return 0;
        }
        s[k]+=s[a[i].second];
        dp[k]+=dp[a[i].second]+s[a[i].second];
        p[a[i].second]=k;
    }
    if(dp[a[1].second]!=a[1].first){
        cout<<-1;
        return 0;
    }
    for(i=2 ; i<=n ;i++){
        cout<<a[i].second<<" "<<p[a[i].second]<<"\n";
    }
    return 0;
}
