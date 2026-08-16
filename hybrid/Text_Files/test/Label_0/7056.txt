#include<bits/stdc++.h>
using namespace std;
using P = pair<double, double>;

const double eps = 1e-6;

bool equal(P a, P b) {
    return max(abs(a.first - b.first), abs(a.second - b.second)) < eps;
}

bool tan_equal(P a1, P a2, P b1, P b2) {
    return abs((a2.first - a1.first) * (b2.second - b1.second) - (b2.first - b1.first) * (a2.second - a1.second)) < eps;
}

bool move(vector<P>& a, int ai, const P& b) {
    if (tan_equal(a[ai], b, a[(ai + 1) % 3], a[(ai + 2) % 3])) {
        a[ai] = b;
        return true;
    }
    return false;
}

bool move(vector<P>& A, int ai1, int ai2, const P& B) {
    double a = A[ai1].first, b = A[ai1].second;
    double c = A[(ai1 + 2) % 3].first - A[(ai1 + 1) % 3].first, d = A[(ai1 + 2) % 3].second - A[(ai1 + 1) % 3].second;
    double e = A[3 - ai1 - ai2].first, f = A[3 - ai1 - ai2].second;
    double g = B.first - A[ai2].first, h = B.second - A[ai2].second;

    if (abs(d * g -  c * h) < eps) return false;

    double x = (a * h - b * g - e * h + f * g) / (d * g -  c * h);
    A[ai1].first += c * x;
    A[ai1].second += d * x;
    return true;
}


int main() {
    vector<vector<int>> va, vb;
    {
        vector<int> v = { 0, 1, 2 };
        do {
            va.push_back({ v[0], v[1], v[0], v[2] });
            va.push_back({ v[0], v[1], v[2], v[0] });
            va.push_back({ v[0], v[1], v[2], v[1] });
        } while (next_permutation(v.begin(), v.end()));
    }
    {
        vector<int> v = { 0, 1, 2, 3 };
        do {
            vb.push_back(v);
        } while (next_permutation(v.begin(), v.end()));
    }

    while (true) {
        vector<P> a(3), b(3);
        for (auto& i : a) cin >> i.first >> i.second;
        for (auto& i : b) cin >> i.first >> i.second;
        if (!cin) return 0;

        vector<P> tmp = a;
        int ans = 5;
        for (auto& ai : va) {
            for (auto& bi : vb) {
                a = tmp;
                for (int i = 0; i < 4; ++i) {
                    if (bi[i] == 3) {
                        if (i == 3) {
                            ans = 3;
                            goto B;
                        }
                        if (!move(a, ai[i], ai[i + 1], b[bi[i + 1]])) goto A;
                    }
                    else if (!move(a, ai[i], b[bi[i]])) goto A;
                }
                ans = 4;
                A: continue;
            }
        }
        B:
        if (ans == 5) cout << "Many\n";
        else cout << ans << "\n";
    }
    return 0;
}

