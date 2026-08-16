#include<iostream>
using namespace std;
int N_MAX = 10;
int main()
{
  int n,nn,m,i,j,kk,t,res=0;
  int k[N_MAX],s[N_MAX][N_MAX],p[N_MAX],ss[N_MAX];
  cin >> n >> m;
  for(i=0;i<m;i++){
    cin >> k[i];
    for(j=0;j<k[i];j++)
      cin >> s[i][j];
  }
  for(i=0;i<m;i++)
    cin >> p[i];
  nn=1<<n;
  for(i=0;i<nn;i++){
    for(j=0;j<n;j++)
      ss[j]=(i>>j)%2;
    for(j=0;j<m;j++){
      t=0;
      for(kk=0;kk<k[j];kk++)
        if(ss[s[j][kk]-1]==1) t++;
      if(t%2!=p[j]) break;
    }
    if(j==m) res++;
  }
  cout << res << endl;
  return 0;
}