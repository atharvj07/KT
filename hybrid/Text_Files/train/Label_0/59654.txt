import java.util.*;

public class Main {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arrS = new int[n];
		int[] arrT = new int[n];
		TreeMap<Integer, Integer> map = new TreeMap<>();
		for (int i = 0; i < n; i++) {
		    arrS[i] = sc.nextInt();
		    map.put(arrS[i], null);
		    arrT[i] = sc.nextInt();
		    map.put(arrT[i], null);
		}
		int idx = 1;
		for (int x : map.keySet()) {
		    map.put(x, idx);
		    idx++;
		}
		int[] imos = new int[idx + 1];
		for (int i = 0; i < n; i++) {
		    imos[map.get(arrS[i])]++;
		    imos[map.get(arrT[i]) + 1]--;
		}
		int max = 0;
		for (int i = 1; i < idx; i++) {
		    imos[i] += imos[i - 1];
		    max = Math.max(max, imos[i]);
		}
		System.out.println(max);
	}
}

