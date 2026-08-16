#include<bits/stdc++.h>
#define  INF 1100000000
#define	 MOD 1000000007
using namespace std;

int main(){
	int N;
	cin >> N;
	int members[110000];
	for(int i=0;i<110000;i++){
		members[i] = 0;
	}
	members[0]++;//私
	for(int i=0;i<N;i++){
		int a, b;
		cin >> a >> b;
		members[a]++;
		members[b+1]--;
	}
	int max = members[0];
	for(int i=1;i<=N+1;i++){
		members[i] += members[i-1];
		if(members[i] >= i){
			max = i;
		}
	}
	
	max--;
	
	cout << max << endl;
	return 0;
	
	
}
