#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

struct V{
	int v;
	double t;
	V (int a = 0, double b = 0.0):v(a), t(b) {}
	V operator +(V o) { return V(v + o.v, (v * t + o.v * o.t) / (v + o.v)); }
	bool R(V o) { return t <= o.t; }
};

int main(){
	int n, l;
	scanf("%d%d", &n, &l);
	deque<V> T;
	T.push_back(V(l));
	double h = 0.0;
	f(i, 0, n){
		int a, b;
		scanf("%d%d", &a, &b);
		V c(b, a);
		int need = c.v;
		while (need){
			if (need >= T.back().v)need -= T.back().v, h -= T.back().v * T.back().t, T.pop_back();
			else h -= need * T.back().t, T.back().v -= need, need = 0;
		}
		h += c.v * c.t;
		while (!T.empty() && c.R(T.front()))c = c + T.front(), T.pop_front();
		T.push_front(c);
		printf("%.7lf\n", h / l);
	}
}