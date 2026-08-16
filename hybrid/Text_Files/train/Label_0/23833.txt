#include <bits/stdc++.h>
using namespace std;
int main(){
  long long n,m,ans=1,now;
  cin >> m >> n;
  long long a[n],b[n];
  pair<long long,long long> p[n];
  for(int i=0;i<n;i++){
    cin >> a[i] >> b[i];
    p[i]=make_pair(b[i],a[i]);
  }
  sort(p,p+n);
  now=p[0].first;
  for(int i=0;i<n;i++){
    if(now<=p[i].second){
      ans++;
      now=p[i].first;
    }
  }
  cout << ans << endl;
  return 0;
}

