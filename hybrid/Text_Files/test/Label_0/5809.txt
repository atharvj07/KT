#include <iostream>
#include <vector>
#include <string.h>
using namespace std;

typedef long long ll;
int N,M,P;
ll D[2510];
bool negative[2510];
ll inf = 1e18;
struct edge {int from,to; ll cost;};

vector<edge> v;

void shortest_path(int s){
	for(int i=1;i<=N;i++) D[i] = inf;
	D[s] = 0;
	for(int j=0;j<N-1;j++){
		for(int i=0;i<v.size();i++){
			edge e = v[i];
			if(D[e.from] != inf && D[e.to] > D[e.from] + e.cost){
				D[e.to] = D[e.from] + e.cost;
			}
		}
	}
}

void find_negative_loop(){
	for(int i=1;i<=N;i++) negative[i] = false;
	for(int i=1;i<=N;i++){
		for(int j=0;j<v.size();j++){
			edge e = v[j];
			if(D[e.to]!=inf && D[e.to] > D[e.from] + e.cost){
				D[e.to] = D[e.from] + e.cost;
				negative[e.to] = true;
			}
			if(negative[e.from]) negative[e.to] = true;
		}
	}
}

int main(){
	cin >> N >> M >> P;
	for(int i=0;i<M;i++){
		int a,b,c;
		cin >> a >> b >> c;
		v.push_back((edge{a,b,P-c}));
	}
	shortest_path(1);
	ll ans = max(-D[N],0LL);
	find_negative_loop();
    cout << (negative[N]? -1:ans) << endl;
}