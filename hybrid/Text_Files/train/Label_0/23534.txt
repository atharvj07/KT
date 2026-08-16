#include<bits/stdc++.h>
using namespace std;
using Int = long long;
vector<int> match(string &t,string &p) {
  //cout<<t<<" "<<p<<endl;
  using BS = bitset<100>;
  int n = t.length(), m = p.length();
  vector<BS> M(100);
  vector<int> res(n,0);
  for (int i=0;i<m;i++){
    if(p[i]=='?') for(int j=0;j<100;j++) M[j][i]=1;
    if(isdigit(p[i])) M[p[i]-'0'][i]=1;
    if(islower(p[i])) M[10+p[i]-'a'][i]=1;
    if(isupper(p[i])) M[36+p[i]-'A'][i]=1;
  }
  BS S(0);
  for (int i = 0; i < n; i++) {
    S=((S<<1)|BS(1));
    if(isdigit(t[i])) S&=M[t[i]-'0'];
    if(islower(t[i])) S&=M[10+t[i]-'a'];
    if(isupper(t[i])) S&=M[36+t[i]-'A'];
    
    if((S&(BS(1)<<(m-1))).count()) res[i]=1;
  }
  //for(int i=0;i<n;i++) cout<<res[i];cout<<endl;
  return res;
}

signed main(){
  int aw,ah,bw,bh;
  cin>>aw>>ah>>bw>>bh;
  string a[ah],b[bh];
  for(int i=0;i<ah;i++) cin>>a[i];
  for(int i=0;i<bh;i++) cin>>b[i];
  //for(int i=0;i<ah;i++) cout<<a[i]<<endl;;
  //for(int i=0;i<bh;i++) cout<<b[i]<<endl;;
  vector<int> G[ah][bh];
  for(int i=0;i<ah;i++)
    for(int j=0;j<bh;j++)
      G[i][j]=match(a[i],b[j]);
  
  int ans=0;
  for(int i=0;i<=ah-bh;i++){
    for(int j=0;j<aw;j++){
      int res=1;
      for(int k=0;k<bh;k++)
	res&=G[i+k][k][j];
      ans+=res;
    }
  }
  cout<<ans<<endl;
  return 0;
}