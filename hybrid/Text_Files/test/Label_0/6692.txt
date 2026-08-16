#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cin >> n;
	int s=0,m=0;
	for(int i=0; i<n; i++){
		int l;
		cin >> l;
		s += l;
		m = max(m,l);
	}

	cout << ((s-2*m > 0)?"Yes":"No") << endl;

	return 0;
}