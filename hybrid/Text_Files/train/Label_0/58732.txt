
import java.util.HashSet;
import java.util.Set;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Set<String> set = new HashSet<String>();
		int n = sc.nextInt();
		for (int i = 0; i < n; i++) {
			String cmd = sc.next();
			String str = sc.next();
			switch (cmd) {
			case "insert":
				set.add(str);
				break;
			case "find":
				if (set.contains(str)) System.out.println("yes");
				else System.out.println("no");
				break;
			}
		}
	}
}

