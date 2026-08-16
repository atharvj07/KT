#include <iostream>
#include <queue>
#include <utility>
#define ll long long
using namespace std;

ll A[200010];
priority_queue<pair<ll, int>, vector<pair<ll, int>>, greater<pair<ll, int>>> pq;
bool cd[200010];

int main() {
	int N;
	ll D;
	cin >> N >> D;
	for(int i=0; i<N; ++i){
		cin >> A[i];
		pq.push(make_pair(A[i], i));
	}
	int cnt=0;
	ll ans=0;
	while(cnt<N-1){
		int now=pq.top().second;
		if(now>0){
			if(!cd[now]){
				cd[now]=1;
				ans += A[now]+A[now-1]+D;
				if(A[now]+D<A[now-1]){
					A[now-1]=A[now]+D;
					pq.push(make_pair(A[now-1], now-1));
				}
				++cnt;
			}
		}
		if(now<N-1){
			if(!cd[now+1]){
				cd[now+1]=1;
				ans += A[now]+A[now+1]+D;
				if(A[now]+D<A[now+1]){
					A[now+1]=A[now]+D;
					pq.push(make_pair(A[now+1], now+1));
				}
				++cnt;
			}
		}
		pq.pop();
	}
	cout << ans << endl;
	return 0;
}