import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main{

	public static void main(String[] args) {
		Map<String, Integer> sales = new HashMap<>();
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			int a = sc.nextInt();
			if (a == 0) {
				String k = sc.next();
				int x = sc.nextInt();
				sales.put(k, x);
			}
			if (a == 1) {
				String y = sc.next();
				if (sales.get(y) == null) {
					System.out.println(0);
				} else {
					System.out.println(sales.get(y));
				}

			}
			if(a==2) {
				String z=sc.next();
				sales.remove(z);
			}
		}
	}
}
