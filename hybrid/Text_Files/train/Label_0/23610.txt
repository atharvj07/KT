#define _CRT_SECURE_NO_WARNINGS
#define _SCL_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <algorithm>
#include <functional>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <limits>
#include <numeric>
#include <valarray>
#include <fstream>

using namespace std;
typedef unsigned int uint;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<LL, LL> PP;
#define REP(i, a, n) for(LL i = (a), i##_max = (n); i < i##_max; ++i)
#define REM(i, a, n) for(LL i = (LL)(n) - 1, i##min = (a); i >= i##min; --i)
#define ALL(arr) (arr).begin(), (arr).end()
#define FLOAT fixed << setprecision(16)
#define SPEEDUP {cin.tie(NULL); ios::sync_with_stdio(false);}
const int INF = 0x3FFFFFFF;
const LL INFLL = 0x3FFFFFFF3FFFFFFF;
const double INFD = 1.0e+308;
const double EPS = 1.0e-9;

void YesNo(bool b) { cout << (b ? "Yes" : "No") << endl; }
void YESNO(bool b) { cout << (b ? "YES" : "NO") << endl; }
template <class T, class U>
istream& operator >> (istream& ist, pair<T, U>& right) { return ist >> right.first >> right.second; }
template <class T, class U>
ostream& operator<<(ostream& ost, const pair<T, U>& right) { return ost << right.first << ' ' << right.second; }
template <class T, class TCompatible, size_t N>
void Fill(T(&dest)[N], const TCompatible& val) { fill(dest, dest + N, val); }
template <class T, class TCompatible, size_t M, size_t N>
void Fill(T(&dest)[M][N], const TCompatible& val) { for (int i = 0; i < M; ++i) Fill(dest[i], val); }
template<class T>
T Compare(T left, T right) { return left > right ? 1 : (left < right ? -1 : 0); }
istream& Ignore(istream& ist) { string s; ist >> s; return ist; }
bool Inside(int i, int j, int h, int w) { return i >= 0 && i < h && j >= 0 && j < w; }
template <class T>
T Next() { T buf; cin >> buf; return buf; }

#ifdef ONLY_MY_ENVIR
#include "IntMod.h"
#include "Graph.h"
#include "Math.h"
#include "Matrix.h"
#include "MinMax.h"
#include "Range.h"
#include "Tree.h"
#include "Union_Find.h"
#endif

#ifdef __GNUC__
typedef __int128 LLL;
istream& operator >> (istream& ist, __int128& val) { LL tmp;  ist >> tmp; val = tmp; return ist; }
ostream& operator<< (ostream& ost, __int128 val) { LL tmp = val; ost << tmp; return ost; }
#endif

#if 1234567891
#include <array>
#include <random>
#include <unordered_set>
#include <unordered_map>
template<typename T>
using PriorityQ = priority_queue<T, vector<T>, greater<T> >;
// template <class T>
// auto Is(const T& value) { return [value](const auto& comparand) -> bool { return comparand == value; }; }
#endif

const int M = 4064;
using Bits = bitset<M>;
const int MOD = 998244353;

int Digit(const Bits& a) {
	REM(i, 0, M) {
		if (a[i]) {
			return i + 1;
		}
	}
	return 0;
}

Bits GCD(Bits a, Bits b) {
	Bits* p = &a;
	Bits* q = &b;
	int as = Digit(a) - 1;
	int bs = Digit(b) - 1;

	while (bs >= 0) {
		while (as >= bs) {
			*p ^= *q << (as - bs);
			while (as >= 0 && (*p)[as] == 0) {
				--as;
			}
		}
		swap(p, q);
		swap(as, bs);
	}
	return *p;
}

bool Less(const Bits& a, const Bits& b) {
	REM(i, 0, M) {
		if (a[i] < b[i]) return true;
		if (a[i] > b[i]) return false;
	}
	return false;
}

Bits Inc(const Bits& a) {
	Bits ret(a);

	REP(i, 0, M) {
		if (ret[i]) {
			ret[i] = 0;
		} else {
			ret[i] = 1;
			return ret;
		}
	}
}

int N;
Bits X;
Bits A[6];
int P[M];
int main() {
	cin >> N >> X;
	REP(i, 0, N) {
		cin >> A[i];
	}
	X = Inc(X);

	P[0] = 1;
	REP(i, 1, M) {
		P[i] = P[i - 1] * 2;
		if (P[i] >= MOD) P[i] -= MOD;
	}

	Bits gcd = 0;
	REP(i, 0, N) {
		gcd = GCD(gcd, A[i]);
	}
	
	int xs = Digit(X);
	int gs = Digit(gcd);

	int sum = 0;
	REM(i, gs - 1, xs) {
		if (X[i]) {
			sum += P[i - gs + 1];
			if (sum >= MOD) sum -= MOD;
		}
	}

	Bits Y = 0;
	REM(i, gs - 1, xs) {
		if (Y[i] != X[i]) {
			Y ^= gcd << (i - gs + 1);
		}
	}

	cout << sum + Less(Y, X) << endl;
	return 0;
}
