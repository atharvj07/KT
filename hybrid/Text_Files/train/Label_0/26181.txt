#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops, no-stack-protector")
#pragma GCC target("avx,avx2,fma")

#include <bits/stdc++.h>

using namespace std;
inline void prep ()
{
  cin.tie (0);
  cin.sync_with_stdio (0);
};
// 32 mil = ~1 sec 
long long mod = 1e9+9; //998244353;
const int biggg = 1000000001;
const long long bigggest = 1000000000000000000LL;
const double eps = .0000000001;
const double pi = acos(-1.);

int min2;
const int N = 2e5+5;
int a[N];
int b[N];
int a1[N];
int b1[N];
int a2[N];
int b2[N];

int main(){
    prep();
	int n;
	cin >> n;
	int cnt1 = 0;
	int cnt2 = 0;
	
	for (int i=0; i<n; i++) cin >> a[i];
	for (int i=0; i<n; i++) cin >> b[i];
	
	long long summ = 0;
	for (int i=0; i<n; i++){
	    if (a[i] > b[i]){
	        a1[cnt1] = a[i];
	        b1[cnt1] = b[i];
	        cnt1++;
	    }else if (a[i] < b[i]){
	        a2[cnt2] = a[i];
	        b2[cnt2] = b[i];
	        cnt2++;
	    }
	    summ += abs(a[i]-b[i]);
	}
	int minnest = 0;
	int a11, b11;
	for (int i=0; i<cnt1; i++){
	    min2=0;
	    a11 = a1[i];
	    b11 = b1[i];
        for (int j=0; j<cnt2; j++){
            min2 = max(min2, min(a11, b2[j])-max(a2[j], b11));
        }
	    minnest = max(minnest, min2);
	}
	cout << summ-2*minnest;
    return 0;
}
