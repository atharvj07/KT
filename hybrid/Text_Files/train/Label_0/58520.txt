import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		while (true) {
			int N = nextInt();
			if (N == 0) {
				break;
			}
			int M = nextInt();
			int[] h = new int[N];
			int totalH = 0;// 高さの和を調べておく
			for (int i = 0; i < h.length; i++) {
				h[i] = nextInt();
				totalH += h[i];
			}

			int[] w = new int[M];
			int totalW = 0;// 幅の和も調べておく
			for (int i = 0; i < w.length; i++) {
				w[i] = nextInt();
				totalW += w[i];
			}

			int[] heightType = new int[totalH + 1];// 作りうる高さの種類
			int[] widthType = new int[totalW + 1];// 作りうる幅の種類

			for (int i = 0; i < h.length; i++) {
				int height = h[i];
				heightType[height]++;
				for (int j = i + 1; j < h.length; j++) {
					height += h[j];
					heightType[height]++;
				}
			}

			for (int i = 0; i < w.length; i++) {
				int width = w[i];
				widthType[width]++;
				for (int j = i + 1; j < w.length; j++) {
					width += w[j];
					widthType[width]++;
				}
			}

			int ans = 0;// 解答
			for (int i = 1; i <= Math.min(totalH, totalW); i++) {
				ans += heightType[i] * widthType[i];
			}

			System.out.println(ans);

		}

	}

	static int nextInt() {
		int c;
		try {
			c = System.in.read();
			while (c != '-' && (c < '0' || c > '9'))
				c = System.in.read();
			if (c == '-')
				return -nextInt();
			int res = 0;
			while (c >= '0' && c <= '9') {
				res = res * 10 + c - '0';
				c = System.in.read();
			}
			return res;
		} catch (IOException e) {
			e.printStackTrace();
		}
		return -1;
	}

	static char nextChar() {
		try {
			int b = System.in.read();
			while (b != -1 && (b == ' ' || b == '\r' || b == '\n'))
				;
			if (b == -1)
				return 0;
			return (char) b;
		} catch (IOException e) {
		}
		return 0;
	}

}