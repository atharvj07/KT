import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while(true) {
			final int N = sc.nextInt();
			if(N == 0) break;

			Map<String, Long> cost = new HashMap<String, Long>();
			for(int i = 0; i < N; i++) {
				cost.put(sc.next(), sc.nextLong());
			}

			final int M = sc.nextInt();

			Map<String, List<String> > recipe = new HashMap<String, List<String> >();
			for(int i = 0; i < M; i++) {
				String name = sc.next();
				int k = sc.nextInt();

				ArrayList<String> al = new ArrayList<String>();
				for(int j = 0; j < k; j++)
					al.add(sc.next());

				recipe.put(name, al);
			}

			while(true) {
				boolean f = false;
				for(String to : recipe.keySet()) {
					long sum = 0L;
					for(String from : recipe.get(to)) {
						if(cost.get(from) == null) {
							sum += (int)1e9;
						}
						else {
							sum += cost.get(from);
						}
					}


					if(cost.get(to) == null || cost.get(to) > sum) {
						cost.put(to, sum);
						f = true;
					}
				}
				if(f == false) break;
			}

			String want = sc.next();
			System.out.println(cost.get(want));
		}
	}
}