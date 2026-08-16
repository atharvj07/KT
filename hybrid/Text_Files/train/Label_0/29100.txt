#include<bits/stdc++.h>
using namespace std;
int main() {
	unsigned long long int i, n, k, j, x, gcount = 0;
	//double x;

	cin>>n>>k>>x;
	vector<unsigned long long int> a(n), b;
	for(int i=0;i<n;i++) 
		cin>>a[i];
	
	sort(a.begin(), a.end());
	
	
	for(int i=1;i<n;i++) {
		if(a[i]-a[i-1]>x) {
			gcount++;
			b.push_back(((a[i]-a[i-1]+x-1)/x)-1);
		}	
	}	
	gcount++;
	//cout<<gcount<<endl;
	sort(b.begin(), b.end());
	
	/*for(i=0;i<b.size();i++)
		cout<<b[i]<<" ";
	cout<<endl;*/
	
	
	for(i=0;i<b.size();i++) {
		if(b[i]<=k)
			k-=b[i];
		else
			break;
	}
	cout<<gcount-i<<endl;
	
}