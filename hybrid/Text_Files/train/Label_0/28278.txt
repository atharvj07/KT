#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <cstdio>
#define int long long
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
#define Inf 1000000000000000000LL
#define F first
#define S second
using namespace std;
typedef pair<int,int>pii;
int n,ans;
int a[60],b[60];
map<int,map<int,int> >mm;
signed main(){
	cin>>n;
	for(int i=1;i<=n;i++)cin>>a[i]>>b[i];
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(i!=j)
				ans=max(ans,++mm[a[i]-a[j]][b[i]-b[j]]);
	cout<<n-ans<<endl;
	return 0;
}
