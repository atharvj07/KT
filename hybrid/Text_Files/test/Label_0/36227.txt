import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	static List<List<Integer>> fullLIst;
	
	static void perm(List<Integer> seed) {
		List<Integer> list = new ArrayList<>(seed);
		boolean[] used = new boolean[seed.size()];
		build(seed, list, used, 0);
	}
	
	static void build(List<Integer> seed, List<Integer> list, boolean[] used, int index) {
		if (index == seed.size()) {
			fullLIst.add(new ArrayList<>(list));
			return;
		}
		
		for (int i = 0; i < seed.size(); i++) {
			if (used[i]) {
				continue;
			} else {
				list.set(index, seed.get(i));
				used[i] = true;
				build(seed, list, used, index + 1);
				used[i] = false;
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<Integer> sortedList = new ArrayList<>();
		int n = sc.nextInt();
		for (int i = 1; i <= n; i++) {
			sortedList.add(i);
		}
		fullLIst = new ArrayList<>();
		Collections.sort(sortedList);
		perm(sortedList);
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < fullLIst.size(); i++) {
			for (int j = 0; j < fullLIst.get(i).size() - 1; j++) {
				sb.append(fullLIst.get(i).get(j));
				sb.append(' ');
			}
			
			sb.append(fullLIst.get(i).get(fullLIst.get(i).size() - 1));
			sb.append('\n');
		}
		System.out.print(sb.toString());
	}
}

