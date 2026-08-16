import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Collections;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
*/public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		Scanner in = new Scanner(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskD solver = new TaskD();
		solver.solve(1, in, out);
		out.close();
	}
static class TaskD   {
public void solve(int testNumber, Scanner in, PrintWriter out) {

        PriorityQueue<int[]> all = new PriorityQueue<>((array1,array2)->-array1[0]+array2[0]);
        HashSet<Integer> kindset = new HashSet<>();
        PriorityQueue<Integer> next = new PriorityQueue<>();
        PriorityQueue<Integer> newkind = new PriorityQueue<>(Collections.reverseOrder());

        int N = in.nextInt();
        int K = in.nextInt();

        for (int i=0; i<N; i++) {
            int[] temp = new int[2];
            temp[1] = in.nextInt();
            temp[0] = in.nextInt();
            all.add(temp);

        }

        long dsum = 0;
        for (int i=0; i<=K-1; i++) {
            int[] temp = new int[2];
            temp = all.poll();

            dsum+=temp[0];

            if(kindset.contains(temp[1])){
                next.add(temp[0]);
            } else {
                kindset.add(temp[1]);
            }
        }
        long knum = kindset.size();

        for (int i=K; i<=N-1; i++) {
            int[] temp = new int[2];
            temp = all.poll();

            if(!kindset.contains(temp[1])){
                kindset.add(temp[1]);
                newkind.add(temp[0]);
            }
        }

        long ans = dsum + knum*knum;
        long temp = ans;
        while (newkind.size() != 0 && next.size() != 0){
            int p = newkind.poll();
            int m = next.poll();
            knum++;
            temp = temp + p - m + 2*knum - 1;
            ans = Math.max(ans, temp);
        }
        out.println(ans);
    }

}
}

