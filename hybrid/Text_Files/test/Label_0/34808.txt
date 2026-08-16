import java.io.*;
import java.util.*;

// 3101
public class Main {

    List<Integer> a = new ArrayList<>();


	// メイン return falseでおしまい
	boolean main() throws IOException {

	    int N = readIntArray()[0];
        String S = reader.readLine();

//		if (N == 0)
//			return false; /* おしまい */

        int north = 0;
        int east = 0;
		for(int i = 0; i < N; i++) {
		    int c = S.charAt(i);
		    if ('A' <= c && c <= 'M') {
		        north++;
		    }
		    else if ('N' <= c && c <= 'Z') {
                north--;
            }
		    else if ('a' <= c && c <= 'm') {
                east++;
            }
            else if ('n' <= c && c <= 'z') {
                east--;
            }
		}
		String r = "";
		for(int i = 0; i< Math.abs(north); i++) {
		    if (north > 0) {
		        r += "A";
		    }
		    else {
                r += "N";
		    }
		}
        for(int i = 0; i< Math.abs(east); i++) {
            if (east > 0) {
                r += "a";
            }
            else {
                r += "n";
            }
        }



		System.out.printf("%d\n%s\n", r.length(), r);

		//return true; /* 正常終了 次へ */
		return false;
	}


//	private final static boolean DEBUG = true;  // debug
	private final static boolean DEBUG = false; // release

	public static void main(String[] args) throws IOException {

		if (DEBUG) {
			log = System.out;

			String inputStr = "5\r\n" + 
			        "xUkad\n";
//			String inputStr = "4\n0 0 10 0 10 10 0 10\n10\n12\n0 0\n9 1\n0\n"; // 96.63324958071081
//			String inputStr = "4\n0 0 10 0 10 10 0 10\n10\n12\n0 1\n9 1\n0\n"; // 103.2664991614216
//			String inputStr = "8\n2 0 4 0 6 2 6 4 4 6 2 6 0 4 0 2\n10\n12\n3 0\n3 5\n0\n"; // 60.0

			reader = new BufferedReader(new StringReader(inputStr));

		}
		else {
			log = new PrintStream(new OutputStream() { public void write(int b) {} } ); // 書き捨て
			reader = new BufferedReader(new InputStreamReader(System.in)); // コンソールから
		}

		for(int loop = 0;; loop++) {
			boolean b = new Main().main();
			if (!b)
				break;
		}

		reader.close();
	}


	static PrintStream log;
	static BufferedReader reader;


	// 標準入力より　1行分のスペース区切りの整数値を読む
	private int[] readIntArray() throws IOException {

		String s = reader.readLine();
		String[] sp = s.split(" ");
		int[] a = new int[sp.length];
		for(int i = 0; i < sp.length; i++) {
			a[i] = Integer.parseInt(sp[i]);
		}
		return a;
	}

}



