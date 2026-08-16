import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		TreeMap<String, List<Integer>> map = new TreeMap<>();
		int q = sc.nextInt();
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < q; i++) {
			int op = sc.nextInt();
			String key = sc.next();
			switch (op) {
				case 0:
					if (map.get(key) == null) {
						map.put(key, new ArrayList<>());
					}
					map.get(key).add(sc.nextInt());
					break;
				case 1:
					if (!Objects.isNull(map.get(key))) {
						for (int num : map.get(key)) {
							sb.append(num);
							sb.append('\n');
						}
					}
					break;
				case 2:
					map.remove(key);
					break;
				case 3:
					String r = sc.next();
					Map<String, List<Integer>> submap = map.subMap(key, r);
					int count = 0;
					for (String str : submap.keySet()) {
						List<Integer> list = map.get(str);
						for (int num : list) {
							sb.append(str);
							sb.append(' ');
							sb.append(map.get(str).get(count++));
							sb.append('\n');
						}
						count = 0;
					}
					count = 0;
					if (map.get(r) != null) {
						for (int num : map.get(r)) {
							sb.append(r);
							sb.append(' ');
							sb.append(map.get(r).get(count++));
							sb.append('\n');
						}
					}
					break;
			}
		}
		System.out.print(sb.toString());
	}
}

