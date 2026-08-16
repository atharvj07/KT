import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;

public class Main {

	public static void main(String[] args) {
		// TaskA mSol = new TaskA();
		// TaskB mSol = new TaskB();
		// TaskC mSol = new TaskC();
		// TaskD mSol = new TaskD();
		// TaskE mSol = new TaskE();
		TaskF mSol = new TaskF();
		mSol.solve();
		mSol.flush();
		mSol.close();
	}

}

class TaskF {

	public FasterScanner mFScanner;
	public PrintWriter mOut;

	public TaskF() {
		mFScanner = new FasterScanner();
		mOut = new PrintWriter(System.out);
	}

	public void solve() {
		int i, j, k;
		int hpY, atkY, defY;
		int hpM, atkM, defM;
		int h, a, d;
		int nY, nM;
		int res = Integer.MAX_VALUE;
		int temp;
		int hitpoints;
		boolean win;
		
		hpY = mFScanner.nextInt();
		atkY = mFScanner.nextInt();
		defY = mFScanner.nextInt();
		hpM = mFScanner.nextInt();
		atkM = mFScanner.nextInt();
		defM = mFScanner.nextInt();
		h = mFScanner.nextInt();
		a = mFScanner.nextInt();
		d = mFScanner.nextInt();
		
		
		int ratkY = Math.max(0, atkY - defM);
		int ratkM = Math.max(0, atkM - defY);
		
		for (int attack = 0; attack <= 200; attack++) {
			
			for (int defence = 0; defence <= 200; defence++) {
				
				win = false;
				
				ratkY = Math.max(0, atkY - defM + attack);
				ratkM = Math.max(0, atkM - defY - defence);
				
				if (ratkY == 0) {
					continue;
				}
				
				if (ratkM == 0) {
					temp = attack * a + defence * d;
					res = Math.min(res, temp);
					continue;
				}
				
				nM = (hpM / ratkY) + (hpM % ratkY != 0 ? 1 : 0);
				nY = (hpY / ratkM) + (hpY % ratkM != 0 ? 1 : 0);
				
				if (nY > nM) {
					temp = attack * a + defence * d;
					res = Math.min(res, temp);
					continue;
				}
				
				nY = nM * ratkM - hpY;
				nY++;
				
				temp = nY * h + attack * a + defence * d;
				res = Math.min(res, temp);
			}
			
		}
		
//		if (res == Integer.MAX_VALUE)
//			res = 0;
		
		mOut.println(res);
		

	}

	public void flush() {
		mOut.flush();
	}

	public void close() {
		mOut.close();
	}
}

class FasterScanner {
	private InputStream mIs;
	private byte[] buf = new byte[1024];
	private int curChar;
	private int numChars;

	public FasterScanner() {
		this(System.in);
	}

	public FasterScanner(InputStream is) {
		mIs = is;
	}

	public int read() {
		if (numChars == -1)
			throw new InputMismatchException();
		if (curChar >= numChars) {
			curChar = 0;
			try {
				numChars = mIs.read(buf);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
			if (numChars <= 0)
				return -1;
		}
		return buf[curChar++];
	}

	public String nextLine() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isEndOfLine(c));
		return res.toString();
	}

	public String nextString() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		StringBuilder res = new StringBuilder();
		do {
			res.appendCodePoint(c);
			c = read();
		} while (!isSpaceChar(c));
		return res.toString();
	}

	public long nextLong() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		long res = 0;
		do {
			if (c < '0' || c > '9')
				throw new InputMismatchException();
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}

	public int nextInt() {
		int c = read();
		while (isSpaceChar(c))
			c = read();
		int sgn = 1;
		if (c == '-') {
			sgn = -1;
			c = read();
		}
		int res = 0;
		do {
			if (c < '0' || c > '9')
				throw new InputMismatchException();
			res *= 10;
			res += c - '0';
			c = read();
		} while (!isSpaceChar(c));
		return res * sgn;
	}

	public boolean isSpaceChar(int c) {
		return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
	}

	public boolean isEndOfLine(int c) {
		return c == '\n' || c == '\r' || c == -1;
	}

}