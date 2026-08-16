import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		Solver solver = new Solver();
		solver.init();
		solver.readHead(in.readLine());
		// for (; solver.hasNext();) {
		// solver.readBody(in.readLine());
		// }
		// solver.solve();
	}
}

class Solver {
	int N;
	int cnt;

	public void init() {
		N = 0;
		cnt = 0;
	}

	public void readHead(String str) {
		String[] strArr = str.split(" ");
		// N = Integer.parseInt(strArr[0]);
		// System.out.println(N);
		int R = Integer.parseInt(strArr[0]);
		int G = Integer.parseInt(strArr[1]);
		int B = Integer.parseInt(strArr[2]);
		N = Integer.parseInt(strArr[3]);
		int cnt = 0;
		for (int r = 0; r <= 3000 && r * R <= N; r++) {
			for (int g = 0; g <= 3000 && r * R + g * G <= N; g++) {
				if (r * R + g * G > N)
					continue;
				if ((N - r * R - g * G) % B == 0) {
					cnt++;
				}
			}
		}
		System.out.println(cnt);
	}

	public boolean hasNext() {
		return cnt < N;
	}

	public void readBody(String str) {
		// System.out.println(str);
		cnt++;
	}

	public void solve() {

	}
}
