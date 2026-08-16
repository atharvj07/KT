#include <bits/stdc++.h>
int cur_room_num[100000];
int main() {
  int num_room, d, room_num;
  std::cin >> num_room >> d >> room_num;
  for (int i = 0; i < num_room; ++i) {
    std::cin >> cur_room_num[i];
  }
  int max_l = -1, min_r = num_room, left_stud = 0, right_stud = 0, left_cnt = 0,
      right_cnt = 0;
  for (int l = 0, r = num_room - 1; l < r; ++l, --r) {
    for (int t = max_l + 1; t <= max_l + d + 1 && t < num_room; ++t) {
      left_stud += cur_room_num[t];
    }
    if (max_l < num_room) {
      max_l += d + 1;
    }
    for (int t = min_r - 1; t >= min_r - d - 1 && t >= 0; --t) {
      right_stud += cur_room_num[t];
    }
    if (min_r >= 0) {
      min_r -= d + 1;
    }
    if (room_num <= left_stud) {
      left_stud -= room_num;
    } else {
      left_cnt += 1;
    }
    if (room_num <= right_stud) {
      right_stud -= room_num;
    } else {
      right_cnt += 1;
    }
  }
  if (left_cnt <= right_cnt) {
    std::cout << right_cnt << std::endl;
  } else {
    std::cout << left_cnt << std::endl;
  }
  return 0;
}
