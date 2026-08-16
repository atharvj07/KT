#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
int main(){
	int n,t;	cin>>n>>t;
	vector<int> a(n);
	for(int i=0;i<n;i++)	cin>>a[i];
	int profit=0,sml=a[0],pattern=0;
	for(int i=1;i<n;i++){
		if(sml>a[i]){
			sml=a[i];
		}
		else if(a[i]-sml>profit){
			profit=a[i]-sml;
			pattern=1;
		}
		else if(a[i]-sml==profit){
			pattern++;
		}
	}
	cout<<pattern<<endl;
	return 0;
}
