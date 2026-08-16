//なんで遅いんだろ
//#include<bits/stdc++.h>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define co(x) cout << (x) << "\n"
#define cosp(x) cout << (x) << " "
#define ce(x) cerr << (x) << "\n"
#define cesp(x) cerr << (x) << " "
#define pb push_back
#define mp make_pair
#define Would
#define you
#define please

const int cm = 1 << 17;
char ci[cm];
char* cn = ci + cm;
inline char getcha() {
	if (cn - ci == cm) { fread(ci, 1, cm, stdin); cn = ci; }
	return *cn++;
}

inline int getint() {
	char C = getcha();
	int A = C - '0';
	while ((C = getcha()) >= '0') A = A * 10 + C - '0';
	return A;
}

int main() {
	//cin.tie(0);
	//ios::sync_with_stdio(false);


	int N;
	N = getint();
	int A[200000];
	ll B[200001], C;
	B[0] = 0;
	C = 0;

	vector<int> V;
	V.pb(0);
	rep(i, N) A[i] = getint();
	ll mae = A[0];
	rep(i, N) {
		ll a = A[i];
		B[i + 1] = B[i];
		if (mae >= a) {
			a *= 4;
			while (mae >= a) {
				V.pb(0);
				a *= 4;
			}
			V.back()++;
		}
		else {
			while (mae < a) {
				int kari = V.back();
				B[i + 1] += kari;
				if (V.size() > 1) {
					V.pop_back();
					V.back() += kari;
				}
				mae *= 4;
			}
			V.back()++;
		}
		mae = A[i];
	}
	V.clear();
	mae = A[N - 1];
	V.pb(0);
	ll kotae = 2 * B[N] + N;
	for (int i = N - 1; i >= 0; i--) {
		ll a = A[i];
		if (mae >= a) {
			a *= 4;
			while (mae >= a) {
				V.pb(0);
				a *= 4;
			}
			V.back()++;
		}
		else {
			while (mae < a) {
				int kari = V.back();
				C += kari;
				if (V.size() > 1) {
					V.pop_back();
					V.back() += kari;
				}
				mae *= 4;
			}
			V.back()++;
		}
		mae = A[i];
		kotae = min(kotae, B[i] + B[i] + C + C + i);
	}

	printf("%lld", kotae);

	Would you please return 0;
}