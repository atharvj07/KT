#include <bits/stdc++.h>
 
using namespace std;
 
using ll = long long;
 
int main(){
	ll n; cin >> n;
	ll arr[n], arr1[n];
	vector<ll> v;
	for(ll i = 0; i < n; ++i){
		cin >> arr[i];
	}
	ll ans = 0, sum = 0;
	for(ll i = 0; i < n; ++i){
		cin >> arr1[i];
		if(arr[i] > arr1[i]){
			v.push_back(arr[i] - arr1[i]);
		}else if (arr1[i] > arr[i]){
			ans++;
			sum += (arr1[i] - arr[i]);
		}
	}
	if(sum > accumulate(v.begin(), v.end(), ll(0))){
		cout << -1;
	}else if(sum == 0){
		cout << 0;
	}else{
		ll cur = 0;
		sort(v.begin(), v.end(), greater<ll>());
		while(sum > 0){
			sum -= v[cur];
			cur++;
			ans++;
		}
		cout << ans;
	}
    return 0;
}
