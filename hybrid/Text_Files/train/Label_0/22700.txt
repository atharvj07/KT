#include<bits/stdc++.h>
using namespace std;

#define i64 long long int
#define ran 202202

int n;
int a[ran];
int s[ran];

int main() {
	scanf("%d", &n);
	for(int i=0;i<n;i++) {
		scanf("%d", &a[i]);
		s[a[i]]++;
	}
	i64 ans = 0;
	for(int i=0;i<ran;i++)
		ans += 1LL*s[i]*(s[i]-1)/2;
	
	for(int i=0;i<n;i++) {
		printf("%lld\n", ans - (s[a[i]]-1));
	}
	
	return 0;
}