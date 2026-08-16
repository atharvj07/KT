#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstring>
#include <set>
#include <utility>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <map>
#include <cmath>
#include <deque>
#include <bitset>
#include <unordered_map>
#define ll long long
#define PI 3.1415926535897932384626433832795
#define read(x) scanf("%d",&x);
#define readll(x) cin>>x;
#define FOR(x,a,b) for(int x=a;x<b;x++)
#define MP make_pair
#define PB push_back
#define pii pair<int,int>
#define readN(N,X) for(int i=0;i<N;i++) cin>>X[i];
#define pff pair<double,double>
using namespace std;

int N,M;
pair<int,int> a[200005];
priority_queue<int, vector<int>, greater<int> > pq;
bool cmp(pii A, pii B){
	if (A.first == B.first)
		return (A.second > B.second);
	return A.first < B.first;
}

int main(){
	std::ios::sync_with_stdio(false); 
	cin>>N>>M;
	FOR(i,0,N){
		cin>>a[i].first>>a[i].second;
	}
	sort(a,a+N, cmp);
	int j =0;
	int ans=0;
	//for (int i=0;i<N;i++) cout<<a[i].first<<" "<<a[i].second<<endl;
	for (int i=1;i<=M;i++){
		
		while (j < N && a[j].first < i) {pq.push(a[j++].second);};
		if (j < N && a[j].first >= i) {j++; continue;}
		if (pq.size() && pq.top() <= i) pq.pop();
	}
	while (j < N) {j++; ans++;}
	cout<<ans + pq.size()<<endl;
}
