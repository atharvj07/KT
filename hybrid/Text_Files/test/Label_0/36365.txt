import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class packages {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int cases = scan.nextInt();
        for(int i = 0; i < cases; i++) {
            int n = scan.nextInt();
            pair[] xy = new pair[n];
            for(int j = 0; j < n; j++)
                xy[j] = new pair(scan.nextInt(), scan.nextInt());
            Arrays.sort(xy);
            solve(xy, n);
        }
        scan.close();
    }

    public static void solve(pair[] xy, int n) {
        int x = 0;
        int y = 0;
        String ans = "";
        boolean possible = true;
        for(int j = 0; j < n; j++) {
            if(xy[j].y < y) {
                System.out.println("NO");
                possible = false;
                j = n;
            }   
            else {
                int right = xy[j].x - x;
                int up = xy[j].y - y;
                for(int r = 0; r < right; r++) {
                    ans+="R";
                }
                for(int u = 0; u < up; u++) {
                    ans+="U";
                }
                x = xy[j].x;
                y = xy[j].y;
            }
        }
        if(possible) {
            System.out.println("YES");
            System.out.println(ans);
        }
    }

    static class pair implements Comparable<pair> {
        int x, y;
        public pair(int a, int b) {
            x = a;
            y = b;
        }
        public int compareTo(pair p) {
            if(x == p.x)
                return y - p.y;
            return x - p.x;
        }
    }

}
