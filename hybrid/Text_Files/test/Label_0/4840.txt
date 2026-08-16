#include<bits/stdc++.h>
using namespace std;
int n,a[205];
vector<int> ans;
int main(){
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		scanf("%d",&a[i]);
	}
	for(int i=0;i<n;i++){
		for(int j=1;j<n;j++){
			ans.push_back(1);
			for(int i=1;i<n;i++) swap(a[i],a[i-1]);
			if(a[0]<a[n-1]){
				ans.push_back(n-1);
				swap(a[n-1],a[0]);
			}
		}
		ans.push_back(1);
		for(int i=1;i<n;i++) swap(a[i],a[i-1]);
	}
	printf("%d\n",ans.size());
	for(int i=0;i<ans.size();i++){
		printf("%d\n",ans[i]);
	}
}