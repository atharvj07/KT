import java.util.*;

class Main {
	static final Integer ZERO = Integer.valueOf(0);
	Scanner sc;
	int N, K;
	HashMap<Integer, Integer> h;
	int[] S;
	
	private void calc() {
		sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		S = new int[N+1];
		h = new HashMap<>(N*4/3);
		
		S[0] = 0;
		for (int i = 1; i < N+1; i++)
			S[i] = (int)(((long)S[i-1] + (sc.nextInt() - 1))%K);
		long cnt = 0;
		for (int i = 1; i < N+1; i++) {
			h.put( S[i-1], h.getOrDefault(S[i-1], ZERO) + 1);
			if (i >= K) {
				int v = h.get(S[i-K]);
				if (v > 1) h.put(S[i-K], v-1);
				else h.remove(S[i-K]);
			}
			cnt += h.getOrDefault(S[i], ZERO);
		}
		System.out.println(cnt);
	}
	
	public static void main(String[] args) {
		new Main().calc();
	}
}
