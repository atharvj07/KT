#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	while(cin >> n){
		int p[n];
		int sum=0;
		int time=0;
		for(int i=0;i<n;i++){
			cin >> p[i];
		}
		sort(p,p+n);
		for(int i=0;i<n;i++){
			sum+=time+p[i];
			time+=p[i];
		}


		cout << sum << endl;
	}
}