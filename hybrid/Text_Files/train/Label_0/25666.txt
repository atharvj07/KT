#include <bits/stdc++.h>
using namespace std;

void FillStack(stack<pair<int, int>>& st,
               const vector<bool>& r,
               vector<int>& coll,
               const pair<int, int>& robot) {
    int x = robot.first;
    int i = robot.second;
    if (st.empty()) {
        st.push(robot);
    } else {
        if (r[i]) {
            st.push(robot);
        } else {
            int pre_x = st.top().first;
            int pre_i = st.top().second;
            if (r[pre_i]) {
                coll[pre_i] = (x - pre_x) / 2;
                coll[i] = (x - pre_x) / 2;
            } else {
                coll[pre_i] = (x + pre_x) / 2;
                coll[i] = (x + pre_x) / 2;
            }
            st.pop();
        }
    }
}

void ReleaseStack(stack<pair<int, int>>& st,
                  const vector<bool>& r,
                  vector<int>& coll,
                  const int m) {
    while(st.size() > 1) {
        int x = st.top().first;
        int i = st.top().second;
        st.pop();
        int pre_x = st.top().first;
        int pre_i = st.top().second;
        st.pop();
        if (r[pre_i]) {
            coll[i] = m - (pre_x + x) / 2;
            coll[pre_i] = m - (pre_x + x) / 2;
        } else {
            coll[i] = m + (pre_x - x) / 2;
            coll[pre_i] = m + (pre_x - x) / 2;
        }
    }

    if (!st.empty()) {
        int i = st.top().second;
        st.pop();
        coll[i] = -1;
    }
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int t, n ,m;
    char c;
    cin >> t;
    while(t--) {
        cin >> n >> m;

        vector<pair<int, int>> robots(n);       // {xi, i}
        for(int i=0; i<n; i++) {
            int x;
            cin >> x;
            robots[i] = {x, i};
        }
        sort(robots.begin(), robots.end());

        vector<bool> r(n, false);
        for(int i=0; i<n; i++) {
            cin >> c;
            if (c == 'R') { r[i] = true; }
        }

        vector<int> coll(n, 0);
        stack<pair<int, int>> even;
        stack<pair<int, int>> odd;

        for(const auto& robot : robots) {
            int x = robot.first;
            if (x%2 == 1) {
                FillStack(odd, r, coll, robot);
            } else {
                FillStack(even, r, coll, robot);
            }
        }

        ReleaseStack(odd, r, coll, m);
        ReleaseStack(even, r, coll, m);

        for (const auto& ct : coll) {
            cout << ct << " ";
        }
        cout << "\n";
    }

    return 0;
}
