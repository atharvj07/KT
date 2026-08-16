import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		SortedSet<Integer> set = new TreeSet<>();
		int q = sc.nextInt();
		for (int i = 0; i < q; i++) {
			int op = sc.nextInt();
			int y = sc.nextInt();
			switch (op) {
				case 0:
					set.add(y);
					System.out.println(set.size());
					break;
				case 1:
					if (set.contains(y)) {
						System.out.println(1);
					} else {
						System.out.println(0);
					}
					break;
				case 2:
					set.remove(y);
					break;
				case 3:
					int z = sc.nextInt() + 1;
					Set<Integer> subset = set.subSet(y, z);
					for (int num : subset) {
						System.out.println(num);
					}
					break;
			}
		}
	}
}

