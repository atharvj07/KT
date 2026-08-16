import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.TreeMap;

public class Main {

	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		TreeMap<String, Integer> map = new TreeMap<>();
		HashSet<String> set = new HashSet<>();
		int max = 0;
		for (int i = 0; i < n; i++) {
			String str = br.readLine();
			if (map.containsKey(str)) {
				map.put(str, map.get(str) + 1);
				max = Math.max(max, map.get(str));
			} else {
				map.put(str, 1);
				max = Math.max(max, map.get(str));
			}
		}

		for (String s : map.keySet()) {
			if (map.get(s) == max) {
				System.out.println(s);
			}
		}
	}
}
