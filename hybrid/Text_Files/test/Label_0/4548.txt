#include <bits/stdc++.h>
using namespace std;
int n,x;
double ans;
int main(){
	cin>>n;
	while(n--){
		cin>>x;
		ans+=1.0/x;
	}
	printf("%.8lf",1.0/ans);
}
