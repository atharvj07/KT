#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <unordered_map>
#include <set>
#include <tuple>
#include <bitset>
#include <memory>
#include <cmath>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <numeric>
#include <climits>
#include <cfloat>


class SegNearTree {
	std::vector<std::vector<std::vector<int>>> vec;
	int inner_find(int depth, int from, int until, const int target) const {
		if (from >= until) return INT_MAX;
		auto length = 1 << depth;
		auto mid = (from + length - 1) / length * length;
		if (mid + length <= until) {
			return std::min({ inner_find(depth, from, mid, target), inner_find(depth, mid + length, until, target), take_nearest(depth, mid / length, target) });
		}
		else if (mid < until) {
			return std::min(inner_find(depth - 1, from, mid, target), inner_find(depth - 1, mid, until, target));
		}
		else {
			return inner_find(depth - 1, from, until, target);
		}
	}

	int take_nearest(int depth, int position, const int target) const {
		auto upper = std::lower_bound(vec[depth][position].begin(), vec[depth][position].end(), target);
		if (upper == vec[depth][position].begin()) return std::abs(target - *upper);
		if (upper == vec[depth][position].end()) return std::abs(target - *std::prev(upper));
		return std::min(std::abs(target - *upper), std::abs(target - *std::prev(upper)));
	}
public:
	SegNearTree(const std::vector<int>& state) :vec{ std::vector<std::vector<int>>() } {
		for (const auto a : state) vec.back().push_back({ a });
		while (vec.back().size() > 1) {
			std::vector<std::vector<int>> last;
			for (auto i = 0; i * 2 + 1 < vec.back().size(); ++i) {
				std::vector<int> v; v.reserve(vec.back()[i * 2].size() + vec.back()[i * 2 + 1].size());
				std::copy(vec.back()[i * 2].begin(), vec.back()[i * 2].end(), std::back_inserter(v));
				std::copy(vec.back()[i * 2 + 1].begin(), vec.back()[i * 2 + 1].end(), std::back_inserter(v));
				std::sort(v.begin(), v.end());
				last.push_back(std::move(v));
			}
			vec.push_back(std::move(last));
		}
	}
	int find_nearest(int from, int until, const int target) { return inner_find(vec.size() - 1, from, until, target); }
};

int main() {
	int n; std::cin >> n;
	std::vector<int> beans(n); for (auto& b : beans) std::cin >> b;
	SegNearTree seg(beans);
	int q; std::cin >> q;
	for (auto i = 0; i < q; ++i) {
		int l, r, d; std::cin >> l >> r >> d;
		std::cout << seg.find_nearest(l, r + 1, d) << '\n';
	}
}

