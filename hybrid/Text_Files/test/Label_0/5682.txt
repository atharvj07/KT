#include <bits/stdc++.h>
using namespace std;
int main(){int n,a,b,c,x,y,z,p,q,r; cin>>n>>a>>b>>c; p=a,q=b,r=c,n--; while(n--){cin>>x>>y>>z; a=x+max(q,r),b=y+max(r,p),c=z+max(p,q),p=a,q=b,r=c;}; cout<<max({a,b,c});}