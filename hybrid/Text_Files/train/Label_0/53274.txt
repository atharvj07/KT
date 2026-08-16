import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {

		Reader reader = new Reader();

		reader.readLine();
		int n = reader.readInt(0);

		int sum[][] = new int[2][370];

		for (int i = 0; i < n; i++) {

			reader.readLine();
			int gender = reader.readString(0).charAt(0) == 'M' ? 0 : 1;
			int st = reader.readInt(1);
			int ed = reader.readInt(2);

			++sum[gender][st];
			--sum[gender][ed+1];

		}
		reader.close();

		int ans = 0;
		for (int i = 1; i < 367; i++) {
			sum[0][i] += sum[0][i - 1];
			sum[1][i] += sum[1][i - 1];
			int res = Math.min(sum[0][i], sum[1][i]) * 2;

			if (res > ans)
				ans = res;

		}
		System.out.println(ans);

	}
}

class Reader {
	private BufferedReader reader;
	private String line[];

	public Reader() {
		reader = new BufferedReader(new InputStreamReader(System.in));
	}

	public String[] getLine() {
		return line;
	}

	public boolean readLine() throws IOException {
		String str = reader.readLine();
		if (str == null || str.isEmpty())
			return false;
		line = str.split(" ");
		return true;
	}

	public List<Integer> getIntegersList() {
		List<Integer> res = new ArrayList<>();
		for (String str : line)
			res.add(Integer.parseInt(str));
		return res;

	}

	public int readInt(int pos) throws IOException {
		return Integer.parseInt(line[pos]);
	}

	public double readDouble(int pos) throws IOException {
		return Double.parseDouble(line[pos]);
	}

	public long readLong(int pos) throws IOException {
		return Long.parseLong(line[pos]);
	}

	public String readString(int pos) throws IOException {
		return line[pos];
	}

	public void close() throws IOException {
		reader.close();
	}
}
