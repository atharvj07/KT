#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using RoomInfo = std::pair<long long, long long>; //どの部屋に残っているか
using Node = std::pair<RoomInfo, int>; // first, second:cost

namespace std {
    template <>
    class hash<std::pair<long long, long long>> {
    public:
        size_t operator()(const std::pair<long long, long long>& x) const {
            return hash<long long>()(x.first) ^ hash<long long>()(x.second);
        }
    };

    template <>
    class hash<std::pair<RoomInfo, int>> {
    public:
        size_t operator()(const std::pair<RoomInfo, int>& x) const {
            return hash<RoomInfo>()(x.first) ^ hash<int>()(x.second);
        }
    };
}


int main() {
    int n, m, k;
    std::vector<int> d; // is darkroom
    int e[100][100];
    std::queue<Node> q;
    std::unordered_map<RoomInfo, std::vector<RoomInfo>> g; //from, to
    std::unordered_set<RoomInfo> visited;

    std::cin >> n >> m >> k;
    if (m == 0) {
        std::cout << 0 << std::endl; // すべて明るい
        return 0;
    }

    d.resize(n, 0);
    for (int i = 0; i < m; i++) {
        int a;
        std::cin >> a;
        d[a-1] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            int a;
            std::cin >> a;
            e[i][j] = a-1; // i番目の部屋からj番目の道でaに行く
        }
    }

    // グラフを作成


    RoomInfo node;
    for (int i = 0; i < n; i++) {
        if (d[i]) {
            if (i < 64) {
                node.first |= 1ull << i;
            }
            else {
                node.second |= 1ull << (i - 64);
            }
        }
    }

    q.push(std::make_pair(node, 0));
    visited.insert(node);

    while (!q.empty()) {
        auto node = q.front(); q.pop();
        node.second++;

        // i番目の道を使用
        for (int i = 0; i < k; i++) {
            RoomInfo next = std::make_pair(0, 0);
            // j番目の部屋から移動
            for (int j = 0; j < n; j++) {
                // 居なければcontinue;
                if (j < 64) {
                    if (!(node.first.first & 1ull << j)) continue;
                }
                else {
                    if (!(node.first.second & 1ull<< (j - 64))) continue;
                }
                int to = e[j][i];
                // 移動先も暗い部屋
                if (d[to]) {
                    if (to < 64) next.first |= 1ull << to;
                    else next.second |= 1ull << (to - 64);
                }
            }

            if (!next.first && !next.second) {
                std::cout << node.second << std::endl;
                return 0;
            }
            if (!visited.count(next)) {
                q.push(std::make_pair(next, node.second));
                visited.insert(next);
            }
        }
    }

    return 0;
}
