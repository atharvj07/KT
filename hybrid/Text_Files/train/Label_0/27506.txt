#include<bits/stdc++.h>
using namespace std;

typedef long long LL;

const int N=1000000;

int n;
char s[N+9];

void into(){
  scanf("%d%s",&n,s+1);
}

int Lucas(int n,int m){
  if (n<m||m<0) return 0;
  return n<2?1:(n&1)>=(m&1)&&Lucas(n>>1,m>>1);
}

int a[N+9],c1;

void Get_a(){
  for (int i=1;i<=n;++i) c1+=(a[i]=s[i]-'1')==1;
}

int ans;

void Get_ans(){
  for (int i=1;i<=n;++i) a[i]=a[i]>>!c1&1;
  for (int i=1;i<=n;++i) ans^=a[i]&Lucas(n-1,i-1);
  ans<<=!c1;
}

void work(){
  Get_a();
  Get_ans();
}

void outo(){
  printf("%d\n",ans);
}

int main(){
  into();
  work();
  outo();
  return 0;
}