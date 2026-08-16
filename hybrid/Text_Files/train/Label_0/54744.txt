
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int x = scanner.nextInt();
			int n = scanner.nextInt();
			int e = scanner.nextInt();
			if ((x | n | e) == 0)
				break;
			int[] v = new int[x];
			for (int i = 0; i < x; i++) {
				v[i] = scanner.nextInt();
			}
			int[][] ev = new int[n + 1][2];
			while (e-- > 0) {
				int p = scanner.nextInt();
				int k = scanner.nextInt();
				int val = scanner.nextInt();
				ev[p][0] = k;
				ev[p][1] = val;
			}
			Map<Integer, List<Double>> map = new HashMap<Integer, List<Double>>();

			List<Double> list = new ArrayList<Double>();
			for (int i = 0; i <= n; i++) {
				list.add(0d);
			}
			list.set(0, 1.0);
			map.put(0, list);
			for (int i = 0; i < n; i++) {
				Map<Integer, List<Double>> tmpMap = new HashMap<Integer, List<Double>>();
				tmpMap.putAll(map);
				for (Entry<Integer, List<Double>> entry : map.entrySet()) {
					int j = entry.getKey();
					if (entry.getValue().get(i) == 0)
						continue;
					for (int k = 0; k < x; k++) {
						int np = Math.min(n, i + v[k]);
						int nm = j;
						if (ev[np][0] == 1)
							np = Math.min(n, np + ev[np][1]);
						else if (ev[np][0] == 2)
							nm += ev[np][1];
						else if (ev[np][0] == 3)
							nm = Math.max(0, nm - ev[np][1]);
						List<Double> tmp;
						if (!tmpMap.containsKey(nm)) {
							tmp = new ArrayList<Double>();
							for (int l = 0; l <= n; l++) {
								tmp.add(0d);
							}
						} else {
							tmp = tmpMap.get(nm);
						}
						double t = tmp.get(np);
						tmp.set(np, t + entry.getValue().get(i) / x);
						tmpMap.put(nm, tmp);
					}
					
				}
				map = tmpMap;

			}
			double ans = 0;
			for (Entry<Integer, List<Double>> enty : map.entrySet()) {
				ans += enty.getKey() * enty.getValue().get(n);
			}
			System.out.println((int) ans);
		}
	}
}