#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main() {
	int n,m;
	cin >> n >> m;
	int a[n];
	for(int i = 0; i < n ; i++) 
		cin >> a[i];
	sort(a , a + n);
	array<int,2> b[m];
	for(int i=0;i<m;i++)
		cin>>b[i][1]>>b[i][0];
	sort(b,b+m);
	int i = 0;
	for(int j=m-1;j>=0;j--){
		while(i < n && a[i] < b[j][0] && b[j][1] > 0){
			a[i] = b[j][0];
			b[j][1]--;
			i++;
		}
	}
	int ans = 0;
	for(int i=0;i<n;i++)
		ans += a[i];
	cout<<ans<<endl;
}