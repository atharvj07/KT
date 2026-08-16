import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] heishts = new int[n];
		for (int i = 0; i < n; i++) {
		    heishts[i] = sc.nextInt();
		}
		long total = 0;
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = n - 1; i > 0; i--) {
		    int x = i + 1 - heishts[i];
		    if (map.containsKey(x)) {
		        map.put(x, map.get(x) + 1);
		    } else {
		        map.put(x, 1);
		    }
		    int y = heishts[i - 1] + i;
		    if (map.containsKey(y)) {
		        total += map.get(y);
		    }
		}
		System.out.println(total);
	}
}
