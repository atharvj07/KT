#include<bits/stdc++.h>
#include<iostream>
#include<functional>
using namespace std;

#define int long long
#define pi pair<int, int>
#define pii pair<pi, int>
const int N = 2e5, M = 1e16;

signed main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int t;
	cin>>t;
	while(t--){
		int n,m;
		cin>>n>>m;
		int A[n], B[n], C[m];
		vector<int> D[n];
		for(int i=0;i<n;i++)
			cin>>A[i];
		for(int i=0;i<n;i++)
			cin>>B[i];
		for(int i=0;i<m;i++)
			cin>>C[i];
		int last = -1;
		for(int i=0;i<n;i++){
			if(C[m-1] == B[i] && A[i] != B[i]){
				last = i;
				break;
			}
		}
		if(last == -1){
			for(int i=0;i<n;i++){
				if(C[m-1] == B[i])
					last = i;
			}
		}
		if(last == -1)
			cout<<"NO\n";
		else{
			for(int i=0;i<n;i++){
				if(A[i] != B[i])
					D[B[i]-1].push_back(i);
			}
			bool val = true;
			vector<int> U;
			for(int i=0;i<m;i++){
				if(D[C[i]-1].size()){
					U.push_back(D[C[i]-1].back());
					D[C[i]-1].pop_back();
				}
				else
					U.push_back(last);
			}
			for(int i=0;i<n;i++){
				if(D[i].size())
					val = false;
			}
			if(val){
				cout<<"YES\n";
				for(auto x: U)
					cout<<x+1<<" ";
				cout<<"\n";
			}
			else
				cout<<"NO\n";
		}
	}

	return 0;
}