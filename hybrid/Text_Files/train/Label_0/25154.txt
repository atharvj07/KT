#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
using namespace std;

typedef istringstream ISS;
typedef ostringstream OSS;
typedef vector<string> VS;
typedef int INT;
typedef vector<INT> VI;
typedef vector<VI> VVI;
typedef pair <INT, INT> II;
typedef vector <II> VII;

template<class T> ostream& operator << ( ostream& os, vector<T> v ) {
    for ( typename vector<T>::iterator it_i = v.begin(); it_i != v.end(); ++it_i ) {
        os << *it_i << ", ";
    }
    return os;
}


typedef long long LL;

const int MOD = 1000000;
const int SIZE = 1001;

const string utf8[4][4] = {
    { "0xxxxxxx" },
    { "110yyyyx", "10xxxxxx" },
    { "1110yyyy", "10yxxxxx", "10xxxxxx" },
    { "11110yyy", "10yyxxxx", "10xxxxxx", "10xxxxxx" }
};
int n;
LL dp[SIZE];

// DESC: Lのk番目にlenバイトのUTF-8バイト列があるときの個数
LL calc( VS& L, int k, int len ) {
    // MEMO: sが試すビット列
    // utfのビット列に対してsをテストするイメージ
    // utf[i] == '0' or '1'のときs[i] != utf[i]だったらsは不正なビット列
    // utf[i] == 'x' のときs[i]が数字だったら1通り、'x'だったら2通りとして数える
    // utf[i] == 'y' のときs[i]が'1'だったら全部0はチェック不要
    //   s[i] == 'x'の個数をカウントしておき、1<<cnt、上の条件で1減らすことがある（yが全て0）
    // cout << k << ", " << len << ": " << "hoge1" << endl;
    LL res = 1;
    int y1 = 0, yx = 0;
    for ( int i = 0; i < len; ++ i ) {
        const string& s = L[k+i];
        const string& u = utf8[len-1][i];
        // cout << "s: " << s << ", " << "u: " << u << endl;
        LL ret = ([&]( const string& s, const string& u ) -> LL {
                // DESC: sがUTF-8なバイト列のとき、何通り
                LL res = 1;
                auto isNumber = []( const char c ) -> bool { return c == '0' || c == '1'; };
                for ( int i = 0; i < 8; ++ i ) {
                    if ( isNumber( u[i] ) ) {
                        // cout << "check nn: " << s[i] << ", " << u[i] << " / " << ( s[i] != 'x' && s[i] != u[i] ) << endl;
                        if ( s[i] != 'x' && s[i] != u[i] ) return 0;
                    
                    } else if ( u[i] == 'x' ) {
                        // cout << "check xx: " << s[i] << ", " << u[i] << endl;
                        if ( s[i] == 'x' ) {
                            res *= 2;
                        }
                    } else if ( u[i] == 'y' ) {
                        if ( s[i] == 'x' ) {
                            yx ++;
                        } else if ( s[i] == '1' ) {
                            y1 ++;
                        }
                    }
                }
                return res;
            })( s, u );
        if ( ret == 0 ) return 0;
        res *= ret;
        res %= MOD;
    }

    if ( len == 1 ) {
        return res;
    }
    if ( y1 == 0 && yx == 0 ) return 0;
    if ( y1 > 0 ) {
        res *= 1 << yx;
    } else {
        res *= ( 1 << yx ) - 1;
    }
    res %= MOD;
    
    // cout << "test Y: " << y1 << ", " << yx << endl;
    // cout << "L: " << L << endl;
    // cout << k << ", " << len << ": " << "hoge2" << endl;
    return res;
}

// DESC: UTF-8での表し方が何通りあるか
LL solve( VS L ) {
    // MEMO: 入力のビット列と、UTF-8のビット列を混同しない
    bool flag = true;
    fill( dp, dp + SIZE, 0 );
    dp[0] = 1;
    for ( int i = 1; i <= n; ++ i ) {
        // cout << i << ": " << L[i-1] << endl;
        for ( int j = 1; j <= 4; ++ j ) {
            if ( i - ( j - 1 ) - 1 < 0 ) continue;
            LL ret = calc( L, i - ( j - 1 ) - 1, j );
            // cout << "calc: " << i - ( j - 1 ) - 1 << ", " << j << ", " << ret << endl;
            if ( ret == 0 ) continue;
            flag = false;
            // cout << "ret: " << ret << ", UTF-8 length: " << j << ", index = " << i - ( j - 1 ) - 1 << endl;
            dp[i] += ( dp[i-j] * ret ) % MOD;
            dp[i] %= MOD;
            // cout << "dp[i] = " << i << ":" << dp[i] << ", " << dp[i-j] << ", " << ret << endl;
        }
    }
    
    return flag ? 0 : dp[n];
}

int main() {
    while ( cin >> n && n ) {
        VS lines(n);
        for ( int i = 0; i < n; ++ i ) cin >> lines[i];
        cout << solve( lines ) << endl;
    }
    return 0;
}