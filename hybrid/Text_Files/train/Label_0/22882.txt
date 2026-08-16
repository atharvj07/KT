#include <bits/stdc++.h>
using namespace std;
int main() {
	long long int mod = 1000000007;
	long long int n, k;
	long long int ans = 0LL;
	//long long int scnt = 0LL;
	//long long int lcnt = 0LL;
	long long int a[2005];
	cin >> n >> k;
	for(int i=0;i<n;i++){
		cin >> a[i];
	}
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if(a[i]>a[j]){
				ans += k*(k+1)/2;
				ans %= mod;
			}
			if(a[i]<a[j]){
				ans += k*(k-1)/2;
				ans %= mod;
			}
		}
	}
	cout << ans << endl;
	return 0;
}