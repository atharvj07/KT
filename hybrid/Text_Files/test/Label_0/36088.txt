import java.util.Scanner;
import java.io.OutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Evgeniy Kiselev
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		Scanner in = new Scanner(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskA solver = new TaskA();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskA {
    public void solve(int testNumber, Scanner in, PrintWriter out) {
        int N = in.nextInt();

//        char[] rooms = new char[N];
        int[] keys = new int[29];
        String data = in.next();
        int res = 0;
        for (int i = 0; i < data.length(); i++) {
            boolean isKey = i % 2 == 0;
            char c = data.charAt(i);
            if (isKey) {
                keys[c - 'a']++;
            } else {
                int index = c - 'A';
                if (keys[index] > 0) {
                    keys[index]--;
                } else {
                    res++;
                }
            }

        }
        out.println(res);
    }
}
