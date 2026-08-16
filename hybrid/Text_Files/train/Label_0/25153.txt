#include "bits/stdc++.h"
#include<unordered_map>
#include<unordered_set>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;
template<class T>
using Table = vector<vector<T>>;



const int mod = 1000000;
struct Mod {
public:
	int num;
	Mod() : Mod(0) { ; }
	Mod(long long int n) : num((n % mod + mod) % mod) {
		static_assert(mod<INT_MAX / 2, "mod is too big, please make num 'long long int' from 'int'");
	}
	Mod(int n) : Mod(static_cast<long long int>(n)) { ; }
	operator int() { return num; }
};

Mod operator+(const Mod a, const Mod b) { return Mod((a.num + b.num) % mod); }
Mod operator+(const long long int a, const Mod b) { return Mod(a) + b; }
Mod operator+(const Mod a, const long long int  b) { return b + a; }
Mod operator++(Mod &a) { return a + Mod(1); }
Mod operator-(const Mod a, const Mod b) { return Mod((mod + a.num - b.num) % mod); }
Mod operator-(const long long int a, const Mod b) { return Mod(a) - b; }
Mod operator--(Mod &a) { return a - Mod(1); }
Mod operator*(const Mod a, const Mod b) { return Mod(((long long)a.num * b.num) % mod); }
Mod operator*(const long long int a, const Mod b) { return Mod(a)*b; }
Mod operator*(const Mod a, const long long int b) { return Mod(b)*a; }
Mod operator*(const Mod a, const int b) { return Mod(b)*a; }
Mod operator+=(Mod &a, const Mod b) { return a = a + b; }
Mod operator+=(long long int &a, const Mod b) { return a = a + b; }
Mod operator-=(Mod &a, const Mod b) { return a = a - b; }
Mod operator-=(long long int &a, const Mod b) { return a = a - b; }
Mod operator*=(Mod &a, const Mod b) { return a = a * b; }
Mod operator*=(long long int &a, const Mod b) { return a = a * b; }
Mod operator*=(Mod& a, const long long int &b) { return a = a * b; }
Mod operator^(const Mod a, const int n) {
	if (n == 0) return Mod(1);
	Mod res = (a * a) ^ (n / 2);
	if (n % 2) res = res * a;
	return res;
}
Mod mod_pow(const Mod a, const int n) {
	if (n == 0) return Mod(1);
	Mod res = mod_pow((a * a), (n / 2));
	if (n % 2) res = res * a;
	return res;
}
Mod inv(const Mod a) { return a ^ (mod - 2); }
Mod operator/(const Mod a, const Mod b) {
	assert(b.num != 0);
	return a * inv(b);
}
Mod operator/(const long long int a, const Mod b) {
	assert(b.num != 0);
	return Mod(a) * inv(b);
}
Mod operator/=(Mod &a, const Mod b) {
	assert(b.num != 0);
	return a = a * inv(b);
}

#define MAX_MOD_N 1024000

Mod fact[MAX_MOD_N], factinv[MAX_MOD_N];
void init() {
	fact[0] = Mod(1); factinv[0] = 1;
	for (int i = 0; i < MAX_MOD_N - 1; ++i) {
		fact[i + 1] = fact[i] * Mod(i + 1);
		factinv[i + 1] = factinv[i] / Mod(i + 1);
	}
}
Mod comb(const int a, const int b) {
	return fact[a] * factinv[b] * factinv[a - b];
}
int main() {
	while (1) {
		int N; cin >> N;
		if (!N)break;
		Mod dp[1001][7][2];
		for (int i = 0; i < 1001; ++i) {
			for (int j = 0; j < 7; ++j) {
				for (int k = 0; k < 2; ++k) {
					dp[i][j][k] = 0;
				}
			}
		}
		dp[0][0][0] = 1;
		for (int i = 0; i < N; ++i) {
			string st; cin >> st; 
			for (int b = 0; b < 256; ++b) {
				bitset<8>bs(b);
				bool ok = true;
				for (int n = 0; n < 8; ++n) {
					if (st[n] == '0'&&bs[7-n] == 1)ok = false;
					if (st[n] == '1'&&bs[7-n] == 0)ok = false;
				}
				if (!ok)continue;
				for (int j = 0; j < 7; ++j) {
					for (int k = 0; k< 2; ++k) {
						bool valid = true;
						switch (j)
						{
						case 0:
							if (!((b ^ 0b00000000) & 0b10000000)) {
								dp[i + 1][0][0] += dp[i][j][k];
							}
							if (!((b ^ 0b11000000) & 0b11100000)) {
								if (b & 0b00011110) {
									dp[i + 1][1][1] += dp[i][j][k];
								}
							}
							if (!((b ^ 0b11100000) & 0b11110000)) {
								if (b & 0b00001111) {
									dp[i + 1][2][1] += dp[i][j][k];
								}
								else {
									dp[i + 1][2][0] += dp[i][j][k];
								}
							}
							if (!((b ^ 0b11110000) & 0b11111000)) {
								if (b & 0b00000111) {
									dp[i + 1][4][1] += dp[i][j][k];
								}
								else {
									dp[i + 1][4][0] += dp[i][j][k];
								}
							}
							break;
						case 1:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								dp[i + 1][0][0] += dp[i][j][k];
							}
							break;
						case 2:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								if (k || (b & 0b00100000)) {
									dp[i + 1][3][1] += dp[i][j][k];
								}
							}
							break;
						case 3:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								dp[i + 1][0][0] += dp[i][j][k];
							}
							break;
						case 4:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								if (k || (b & 0b00110000)) {
									dp[i + 1][5][1] += dp[i][j][k];
								}
							}
							break;
						case 5:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								dp[i + 1][6][1] += dp[i][j][k];
							}
							break;
						case 6:
							if (!((b ^ 0b10000000) & 0b11000000)) {
								dp[i + 1][0][0] += dp[i][j][k];
							}
							break;
						}
					}
				}
			}
		}
		Mod ans = dp[N][0][0];
		cout << ans << endl;
	}
	return 0;
}