import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static ArrayList<Item> items;

	public static void main(String[] args) throws Exception {
		while (true) {
			int N = sc.nextInt();
			int U = sc.nextInt();
			if (N == 0 && U == 0) break;
			items = new ArrayList<Item>();
			ArrayList<ArrayList<Integer>> c = new ArrayList<ArrayList<Integer>>();
			for (int i = 0; i < N; ++i) {
				Item item = new Item(sc.nextInt());
				items.add(item);
				ArrayList<Integer> cs = new ArrayList<Integer>();
				int k = sc.nextInt();
				for (int j = 0; j < k; ++j) {
					int r = sc.nextInt();
					cs.add(r);
				}
				c.add(cs);
			}
			for (int i = 0; i < N; ++i) {
				for (int j : c.get(i)) {
					items.get(i).parent.add(items.get(j));
					items.get(j).child.add(items.get(i));
				}
			}
			ArrayList<Item> sorted = sort();
			for (int i = 0; i < N; ++i) {
				sorted.get(i).index = i;
			}
			int ans = N;
			int[] units = new int[1 << N];
			Arrays.fill(units, -1);
			units[0] = 0;
			for (int i = 0; i < N; ++i) {
				int mask = sorted.get(i).mask() - (1 << i);
				for (int j = 0; j < (1 << i); ++j) {
					if (units[j] == -1 || (j & mask) != mask) continue;
					int newUnits = units[j] + sorted.get(i).unit;
					units[j + (1 << i)] = newUnits;
					int count = Integer.bitCount(j) + 1;
					if (newUnits >= U && count < ans) {
						ans = count;
					}
				}
			}
			System.out.println(ans);
		}
	}

	static ArrayList<Item> sort() {
		ArrayList<Item> sorted = new ArrayList<Item>();
		for (int i = 0; i < items.size(); ++i) {
			dfs(sorted, items.get(i));
		}
		Collections.reverse(sorted);
		return sorted;
	}

	static void dfs(ArrayList<Item> sorted, Item cur) {
		if (cur.visited) return;
		cur.visited = true;
		for (Item c : cur.child) {
			dfs(sorted, c);
		}
		sorted.add(cur);
	}

	static class Item {
		int unit;
		ArrayList<Item> child = new ArrayList<Item>();
		ArrayList<Item> parent = new ArrayList<Item>();
		boolean visited = false;
		int index;

		Item(int c) {
			this.unit = c;
		}

		int mask() {
			int ret = 1 << index;
			for (Item p : parent) {
				ret |= p.mask();
			}
			return ret;
		}

		public String toString() {
			return this.index + " " + this.unit + " " + this.child;
		}

	}

}