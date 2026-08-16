import java.util.*;
import java.util.stream.Collectors;
import java.io.*;
import java.nio.charset.StandardCharsets;

/**
 * 実装方針:
 * 
 * @author glycine
 *
 */
public class Main {
	int M;
	List<Pair> pairs = new ArrayList<>();
	long result = 0;

	static class Pair {
		long c;
		int d;

		Pair(String line) {
			String[] tokens = line.split(" ");
			this.d = Integer.parseInt(tokens[0]);
			this.c = Long.parseLong(tokens[1]);
		}
	}

	void calc() {
		// 桁の合計値を求める
		long ketaSum = 0;
		for (Pair pair : pairs) {
			ketaSum += pair.c;
		}
		ketaSum--;

		// 出現する値の合計値を求める
		long valSum = 0;
		for (Pair pair : pairs) {
			valSum += pair.c * pair.d;
		}
		// System.out.println(ketaSum + ", " + valSum);
		valSum = (valSum - 1) / 9;
		result = ketaSum + valSum;

	}

	void showResult() {
		System.out.println(result);
	}

	Main(BufferedReader in) throws IOException {
		this.M = Integer.parseInt(in.readLine());
		for (int i = 0; i < M; ++i) {
			this.pairs.add(new Pair(in.readLine()));
		}
	}

	public static void main(String[] args) throws IOException {
		InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
		BufferedReader in = new BufferedReader(reader);
		Main ins = new Main(in);
		ins.calc();
		ins.showResult();
	}

}