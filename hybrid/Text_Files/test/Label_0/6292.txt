#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

const int N=100010;

int n,a[N];

int main(){
  scanf("%d",&n);
  for(int i=1;i<=n;i++) scanf("%d",&a[i]);
  sort(a+1,a+1+n,greater<int>());
  int p=0;
  while(p+1<n && p+1<a[p+2]) p++;
  int A=(a[p+1]-p)&1,B=1;
  for(int i=p+2;i<=n && a[i]>p;i++) B^=1;
  if(A && B) puts("Second"); else puts("First");
  return 0;
}
