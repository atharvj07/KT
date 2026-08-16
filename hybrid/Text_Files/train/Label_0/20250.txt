#include <cstdio>
#include <vector>
using namespace std;

#define MOD 1000000007

typedef long long int LLI;
typedef vector<vector<LLI> > Mat;
typedef vector<vector<Mat> > MatMat;

int n;
int k;
int c;
int T;
Mat one;
Mat zero;
Mat G[7];
MatMat m;
MatMat m_zero;
MatMat ans;

Mat mul(Mat &a, Mat &b) {
    Mat ret(zero);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            for (int k=0; k<n; k++) {
                ret[i][j] += a[i][k] * b[k][j] % MOD;
                ret[i][j] %= MOD;
            }
        }
    }
    return ret;
}

Mat add(Mat &a, Mat &b) {
    Mat ret(zero);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            ret[i][j] = (a[i][j] + b[i][j]) % MOD;
        }
    }
    return ret;
}

MatMat mul(MatMat &a, MatMat &b) {
    MatMat ret(m_zero);
    for (int i=0; i<5; i++) {
        for (int j=0; j<5; j++) {
            for (int k=0; k<5; k++) {
                Mat s = mul(a[i][k], b[k][j]);
                ret[i][j] = add(ret[i][j], s);
            }
        }
    }
    return ret;
}

int main() {
    scanf("%d%d%d%d", &n, &k, &c, &T);
    zero = Mat(n, vector<LLI>(n));
    one = Mat(zero);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            zero[i][j] = 0;
            one[i][j] = 0;
        }
        one[i][i] = 1;
    }

    for (int i=0; i<7; i++) {
        G[i] = Mat(zero);
    }

    for (int i=0; i<k; i++) {
        int a, b, t;
        scanf("%d%d%d", &a, &b, &t);
        --a;
        for (int j=0; j<a; j++) {
            G[t][j][b+j]++;
        }

        for (int j=0; j<b; j++) {
            G[t][a+j][j]++;
        }

        for (int j=a+b; j<n; j++) {
            G[t][j][j]++;
        }
    }

    m_zero = vector<vector<Mat> >(5, vector<Mat>(5, zero));
    ans = vector<vector<Mat> >(m_zero);
    m = vector<vector<Mat> >(m_zero);
    for (int i=0; i<5; i++) {
        m[0][i] = G[i+1];
        if (i < 4) m[i+1][i] = one;
        ans[i][i] = one;
    }

    while (T > 0) {
        if (T&1) {
            ans = mul(ans, m);
        }
        m = mul(m, m);
        T >>= 1;
    }
    printf("%lld\n", ans[0][0][c-1][0]);
}