import java.io.*;
import java.util.*;

public class b {
	public static void main(String[] args) throws Exception {
		
		BufferedReader f = new BufferedReader(new InputStreamReader(System.in));	
		PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
		StringTokenizer st = new StringTokenizer(f.readLine());

		int T = Integer.parseInt(st.nextToken());
		
		for (int t = 0; t < T; t++) {
			int n = Integer.parseInt(f.readLine());
			st = new StringTokenizer(f.readLine());
			HashMap<Integer, Integer> index = new HashMap<Integer, Integer>();
			HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();
			for (int i = 0; i < n; i++) {
				int curr = Integer.parseInt(st.nextToken());
				hm.put(curr, hm.getOrDefault(curr,0)+1);
				index.put(curr, i+1);
			}
			int ans = -1;
			for (int key : hm.keySet()) {
				if (hm.get(key) == 1) {
					if (ans == -1 || key < ans) {
						ans = key;
					}
				}
			}
			if (ans == -1) {
				out.println(-1);
			} else {
				out.println(index.get(ans));
			}
		}

		out.close();
	}
}
