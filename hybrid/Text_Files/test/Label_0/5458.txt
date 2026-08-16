#include <iostream>
#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stdlib.h>
#include <string>
#include <utility>
#include <vector>

#define INF 1000000000
#define MOD 1000000007
#define rep(i,a,b) for(uint32 i = (a); i < (b); ++i)
#define bitget(a,b) (((a) >> (b)) & 1)
#define ALL(x) (x).begin(),(x).end()
#define C(x) std::cout << #x << " : " << x << std::endl
#define scanf scanf_s

using int32 = std::int_fast32_t;
using int64 = std::int_fast64_t;
using uint32 = std::uint_fast32_t;
using uint64 = std::uint_fast64_t;

template<typename T>
class hashmap64 {
	std::vector<std::pair<uint64, T>> map;
	uint64 mask, count, temp;
	uint64 hash64(uint64 key) {
		key = ~key;
		key ^= key << 13;
		key ^= key >> 19;
		return key ^ (key << 17);
	}
public:
	hashmap64() :map(8192, std::make_pair(~static_cast<std::uint_fast64_t>(0), T())) {
		mask = 8191; count = 0;
	}
	hashmap64(size_t s) {
		s |= s << 1;
		s |= s >> 2;
		s |= s >> 4;
		s |= s >> 8;
		s |= s >> 16;
		s |= s >> 32;
		mask = s;
		count = 0;
		map.resize(s + 1, std::make_pair(~static_cast<std::uint_fast64_t>(0), T()));
	}
	T &operator[](uint64 suf) {
		temp = mask&hash64(suf);
		while (map[temp].first != suf) {
			temp = mask&(temp + 1);
		}
		return map[temp].second;
	}
	void insert(uint64 key, const T &value) {
		temp = mask&hash64(key);
		while (~map[temp].first) {
			if (map[temp].first == key) {
				map[temp].second = value;
				return;
			}
			temp = mask&(temp + 1);
		}
		map[temp] = std::make_pair(key, value);
		++count;
		if ((count << 1) > mask) {
			std::pair<uint64, T> mkey;
			mask = mask << 1 | 1;
			map.resize(mask + 1, std::make_pair(~static_cast<std::uint_fast64_t>(0), T()));
			for (uint64 t = 0;t <= mask >> 1;++t) {
				if (~map[t].first) {
					mkey = map[t];
					map[t].first = ~static_cast<std::uint_fast64_t>(0);
					temp = mask&hash64(mkey.first);
					while (~map[temp].first) {
						temp = mask&(temp + 1);
					}
					map[temp] = mkey;
				}
			}
		}
		return;
	}
	bool find(uint64 key) {
		temp = mask&hash64(key);
		while (~map[temp].first) {
			if (map[temp].first == key) {
				return true;
			}
			temp = mask&(temp + 1);
		}
		return false;
	}
	bool empty(void) {
		return !count;
	}
	size_t size(void) {
		return count;
	}
};

int main(void) {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	hashmap64<uint32> map(250);
	uint32 n;
	std::cin >> n;
	int64 a, sum = 1e15;
	uint32 ans = 0;
	map.insert(sum, 0);
	rep(i, 0, n) {
		std::cin >> a;
		sum += a;
		if (map.find(sum)) {
			ans = std::max(ans, i + 1 - map[sum]);
		}
		else {
			map.insert(sum, i + 1);
		}
	}
	std::cout << ans << "\n";
	return 0;
}