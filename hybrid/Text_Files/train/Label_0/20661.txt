#include <iostream>
#include <algorithm>
#define INT_MIN 2147483648

using namespace std;

int main(void){
	int *a,maxi;
	for(int n;cin >> n,n;){
		maxi = INT_MIN;
		a = new int[n];
		for(int i=0;i<n;i++)
			cin >> a[i];

		for(int i=0;i<n;i++)
			for(int j=i,sum=0;j<n;j++)
				maxi=max(maxi,sum+=a[j]);
		delete [] a;

		cout << maxi << endl;
	}
	return 0;
}