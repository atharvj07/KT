import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
 
public class Main {
    private static final int MOD = (int) 1e9 + 7;
 
    public static void main(String[] args) throws FileNotFoundException {
        //Scanner in = new Scanner(new File(args[0]));
        //PrintWriter out = new PrintWriter(new File(args[1]));
        Scanner in = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
 
        int t = in.nextInt(), d = in.nextInt(), l = in.nextInt();
        while (t != 0 && d != 0 && l != 0) {
            long ans = 0;
            long last = Integer.MIN_VALUE;
            for (int i = 1; i <= t; i++) {
                if (in.nextInt() >= l) {
                    if (i <= last) {
                        ans += i + d - 1 - last;
                    } else {
                        ans += d;
                    }
                    last = i + d - 1;
                }
            }
          	if (last != Integer.MIN_VALUE && last > t) {
              ans -= last - t;
            }
            out.println(ans == 0 ? 0 : ans - 1);
 
            t = in.nextInt();
            d = in.nextInt();
            l = in.nextInt();
        }
 
 
        out.close();
    }
 
    private static class Task {
        int d, p;
 
        public Task(int d, int p) {
            this.d = d;
            this.p = p;
        }
    }
}
