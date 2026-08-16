/*
 * http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_D&lang=jp
 */

import java.util.*;

class Lake {
	int rpos, lpos, area;
	Lake(int lpos, int rpos, int areaOfChilds) {
		this.rpos = rpos;
		this.lpos = lpos;
		this.area = rpos - lpos - 1 + areaOfChilds;
	}
	void print() {
		System.out.println("lpos:" + lpos + ", rpos:" + rpos + ", area:" + area);
	}
}
public class Main {

	void printArray(int[] a) {
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i] + " ");
		}
		System.out.println();
	}

	void update(LinkedList<Lake> lakes, int l, int r) {
		LinkedList<Lake> childs = new LinkedList<Lake>();
		int areaOfChilds = 0;
		int i = 0, idx = -1;
		for (Lake lake : lakes) {
			if (l < lake.lpos && lake.rpos < r) {
				childs.addLast(lake);
				areaOfChilds += lake.area;
				if (idx == -1) idx = i;
			} else if (idx == -1 && r <= lake.lpos) {
				idx = i;
			}
			i++;
		}
		lakes.removeAll(childs);
		lakes.add((idx == -1 ? lakes.size() : idx), new Lake(l, r, areaOfChilds));
	}

	void debugPrint(LinkedList<Lake> lakes) {
		for (Lake lake : lakes) {
			lake.print();
		}
		System.out.println();
	}

	void solve(int[] a, int level, int cap, LinkedList<Lake> lakes) {
		//System.out.println("solve: " + level + ", " + cap);
		do {
			//System.out.println("solve: " + level + ", " + cap);
		for (int i = 0; i < a.length;) {
			int l = -1, r = -1;
			if (a[i] == level && i+1 < a.length && a[i+1] == (level-1)) {
				l = i;
				for (i += 2; i < a.length; i++) {
					if (a[i] == level && a[i-1] == (level-1)) {
						r = i;
						break;
					}
				}
				if (r != -1) {
					update(lakes, l, r);
				}
			}
			if (r == -1) i++;
		}
		} while (cap > level++);
		//System.out.println(level);
		//debugPrint(lakes);
		//if (cap <= level) return;
		//solve(a, level+1, cap, lakes);
	}

	void run() {
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine();
		char[] chars = line.toCharArray();
		int[] heights = new int[chars.length + 1];
		heights[0] = 0;  // 基準にする
		int bottom = 0;
		int top = 0;
		for (int i = 1; i < heights.length; i++) {
			int diff = 0;
			switch (chars[i-1]) {
			case '\\':
				diff = -1;
				break;
			case '/':
				diff = +1;
				break;
			case '_':
				diff = 0;
				break;
			}
			heights[i] = heights[i-1] + diff;
			bottom = Math.min(heights[i], bottom);
			top = Math.max(heights[i], top);
		}
		//printArray(heights);
		LinkedList<Lake> lakes = new LinkedList<Lake>();
		solve(heights, bottom+1, top, lakes);

		int sum = 0;
		for (Lake lake : lakes) {
			sum += lake.area;
		}

		System.out.println(sum);
		System.out.print(lakes.size());
		for (Lake lake : lakes) {
			System.out.print(" " + lake.area);
		}
		System.out.println();
	}

	public static void main(String[] args) {
		new Main().run();
	}

}

