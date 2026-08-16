import java.util.*;

public class Main {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);

		Map<String,Integer> map = new TreeMap<>();

		int n = scan.nextInt();

		for(int i=0; i<n; i++) {

			int query = scan.nextInt();
			String key = scan.next();

			switch(query) {

			case 0:
				int value = scan.nextInt();
				map.put(key, value);
				break;

			case 1:
				System.out.println(map.get(key));
				break;
			}
		}
	}
}

