#include <bits/stdc++.h>
using namespace std;

int main() {
	int n,m;
	cin>>n>>m;
	vector<int> v[m];
	for(int i=0;i<m;i++){
		int k;
		cin>>k;
		for(int j=0;j<k;j++){
			int z;
			cin>>z;
			v[i].push_back(z);
		}
	}
	int p[m];
	for(int i=0;i<m;i++) cin>>p[i];
	int ans2=0;
	for(int i=0;i<(1<<n);i++){
		int big=0;
		for(int j=0;j<m;j++){
			int ans=0;
			for(int z=0;z<v[j].size();z++){
				if((1<<(v[j][z]-1))&i) ++ans;
			}
			if(ans%2==p[j]) ++big;
		}
		if(big==m) ++ans2;
	}
	cout<<ans2;
}