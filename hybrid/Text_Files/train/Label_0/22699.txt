#include <iostream>
using namespace std;
int h, w, fl=1, a[55][55];
string s;
int main() {
	int i, j;
	cin>>h>>w;
	for(i=1; i<=h; i++) {
		cin>>s;
		for(j=1; j<=w; j++) a[i][j] = s[j-1]=='.' ? 0:1;
	}
	for(i=1; i<=h; i++) for(j=1; j<=w; j++) {
		if(a[i][j]==1 && a[i-1][j] + a[i+1][j] + a[i][j-1] + a[i][j+1] == 0) fl=0;
	}
	cout<<(fl ? "Yes":"No");
	return 0;
}