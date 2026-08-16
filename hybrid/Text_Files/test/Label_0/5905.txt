#include<bits/stdc++.h>
using namespace std;

int main()
{
  int N,ans=0;scanf("%d",&N);
  int a[N];
  for(int i=0;i<N;i++)scanf("%d ",&a[i]);
  for(int i=0;i<N;i++)while(a[i]%2==0){a[i]/=2;ans++;}
  printf("%d\n",ans);
}