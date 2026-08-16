import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Set<Integer> set = new HashSet<>();
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
			}
		}
	}
}

