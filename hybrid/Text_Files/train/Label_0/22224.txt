#include <bits/stdc++.h>
using namespace std;

int main() {
	long n,z,w,k;
	cin>>n>>z>>w;
	vector<long>v(n);
	vector<long>e(n);
	for(int i=0;i<n;i++)cin>>v.at(i);
	for(int i=0;i<n;i++){
		e.at(i)=max(v.at(i)-v.at(n-1),v.at(n-1)-v.at(i));
		
	}
	k=max(w-v.at(n-1),v.at(n-1)-w);
	if(n>=2){
		
	
	cout<<max(k,e.at(n-2))<<endl;
	}
	else{
		cout<<k<<endl;
	}
	return 0;
}