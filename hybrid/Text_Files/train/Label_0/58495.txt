import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		List<Integer> list = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			list.add(sc.nextInt());
		}
		int q = sc.nextInt();
		for (int i = 0; i < q; i++) {
			switch (sc.nextInt()) {
				case 0:
					int b  = sc.nextInt();
					int e = sc.nextInt();
					System.out.println(Collections.min(list.subList(b, e)));
					break;
				case 1:
					b  = sc.nextInt();
					e = sc.nextInt();
					System.out.println(Collections.max(list.subList(b, e)));
					break;
			}
		}
	}
}


