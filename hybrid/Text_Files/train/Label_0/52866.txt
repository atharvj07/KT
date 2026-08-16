import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class E {

    final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;

    StringTokenizer tok = new StringTokenizer("");

	void solve() throws IOException {
            solveTest();
	}

    Scanner sc = new Scanner(System.in);

    int setWhen(int[] arr, int index) {
        return index == arr.length ? -1 : (arr[index] = sc.nextInt());
    }

    int[] readArr(int[] arr, int index) {
        int z = setWhen(arr, index);
        return z == -1 ? arr : readArr(arr, index+1);
    }

    int[] setArr(int[][] arr, int index) {
        return index == arr.length ? null : (arr[index] = readArr(arr[index], 0));
    }

    int[][] readArrArr(int[][] arr, int index) {
        int[] cur = setArr(arr, index);
        return cur == null ? arr : readArrArr(arr, index+1);
    }

    int last(int x, int n) {
        return x == n ? -1 : x;
    }

    int kCycle(int k) {
        int x = last(k, n);
        int z = x == -1 ? -1 : (iCycle(k, 0) + 1);
        return x == -1 ? 0 : kCycle(k+1);
    }

    int iCycle(int k, int i) {
        int x = last(i, n);
        int z = x == -1 ? -1 : (jCycle(k, i, 0));
        return x == -1 ? 0 : iCycle(k, i+1);
    }

    int jCycle(int k, int i, int j) {
        int x = last(j, n);
        int z = x == -1 ? -1 : move(k, i, j);
        return x == -1 ? 0 : (jCycle(k, i, j + 1));
    }

    int move(int k, int i, int j) {
        return g[i][j] > g[i][k] + g[k][j] ? (g[i][j] = g[i][k] + g[k][j]) : g[i][k];
    }

    int max = 0;
    int n;
    int[][] g;

    int iC(int i) {
        int x = last(i, n);
        int z = x == -1 ? -1 : jC(i, 0);
        return x == -1 ? 0 : iC(i+1);
    }

    int jC(int i, int j) {
        int x = last(j, n);
        int z = x == -1 ? -1 : (max = max > g[i][j] ? max : g[i][j]);
        return x == -1 ? 0 : jC(i, j+1);
    }


    void solveTest() throws IOException {
        n = sc.nextInt();
        g = new int[n][n];
        readArrArr(g, 0);

        kCycle(0);
        iC(0);
        System.out.println(max);
    }

    void init() throws FileNotFoundException {

    }

    public static void main(String[] args) {
        new E().run();
    }

    public void run() {
        try {
            solve();
        } catch (Exception e) {
            e.printStackTrace(System.err);
            System.exit(-1);
        }
    }
}