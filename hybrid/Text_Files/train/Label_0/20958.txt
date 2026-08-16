#include <bits/stdc++.h>
using namespace std;
vector<int>v;

int euclid(int x, int y){
	if(x < y) swap(x, y);
	while(y!=0){
		int p = x%y;
		x=y;
		y=p;
	}
        return x;
}

int main(){
	int ans = 0;
	int n = 0;
	cin >> n;
	for(int i =0; i < n;i++){
		int tmp;
		cin >> tmp;
		v.push_back(tmp);
	}
	sort(v.begin(), v.end());
	vector<int>b;
	for(int i = 1; i<=v[n-1]; i++){
		if(v[n-1]%i==0) b.push_back(i);
	}
	for(int i = 0; i < n-1;i++){
		auto it = lower_bound(b.begin(),b.end(),v[i]);
		ans +=*it - v[i];
	}
	cout << ans << endl;
	return 0;
}


