import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author Vadim
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskC solver = new TaskC();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskC {
    public void solve(int testNumber, InputReader in, PrintWriter out) {
        int n = in.nextInt();
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        int median = 1002;
        byte b[][] = new byte[2014][1012];
        int x = 0;
        int y = median;
        int newX = x;
        int newY = median;
        int minY = median;
        int maxY = median;

        for (int i = 0; i < n; i++) {
            x = newX;
            y = newY;
            newX = newX + a[i];
            newY = newY - (a[i]-1) * (i%2==0?1:-1);
            minY = Math.min(minY, newY);
            maxY = Math.max(maxY, newY);
            boolean up = i%2==0;
            for (; x < newX; x++) {
                if(up) {
                    b[y][x] = 1;
                    y--;
                } else  {
                    b[y][x] = -1;
                    y++;
                }
            }

        }
        int maxX = x;
        StringBuilder sb = new StringBuilder();
        for (int i = minY; i <=maxY; i++) {
            for (int j = 0; j < maxX; j++) {
                switch(b[i][j]) {
                    case 0:
                        sb.append(' ');
                        break;
                    case 1:
                        sb.append('/');
                        break;
                    case -1:
                        sb.append('\\');

                        break;
                }
            }
            sb.append('\n');
        }
        out.println(sb);



    }
}

class InputReader  extends BufferedReader {
    public InputReader(InputStream st) {
        super(new InputStreamReader(st));
    }

    public int nextInt() {
        try {
            int c = read();

            while (isWhiteSpace(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int ret = 0;
            while (c >= 0 && !isWhiteSpace(c)) {
                if (c < '0' || c > '9') {
                    throw new RuntimeException();
                }
                ret = ret * 10 + c - '0';
                c = read();
            }
            return ret * sgn;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public String readLine() {
        try {
            return super.readLine();
        } catch (IOException e) {
            return null;
        }
    }


    static boolean isWhiteSpace(int c) {
        return c >= 0 && c <= 32;
    }



}
