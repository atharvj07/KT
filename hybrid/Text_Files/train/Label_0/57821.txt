import java.io.IOException;

public class Test {

    int readInt() {
        int ans = 0;
        try {
            boolean start = false;
            for (int c = 0; (c = System.in.read()) != -1; ) {
                if (c >= '0' && c <= '9') {
                    start = true;
                    ans = ans * 10 + c - '0';
                } else if (start) break;
            }
        } catch (IOException e) {
        }
        return ans;
    }

    void start() {
        int n = readInt(), k = readInt();
        while(true) {
            if (k == 1) break;
            if (k == 2) {
                if (n <= 4) break;

                System.out.println(4 + (n - 4) * 2);
                int[][] es = {
                        {1, 2},
                        {2, 3},
                        {2, 4},
                        {3, 4}
                };
                for (int[] e : es)
                    System.out.println(e[0] + " " + e[1]);
                for (int i = 5; i <= n; i++) {
                    System.out.println(1 + " " + i);
                    System.out.println(3 + " " + i);
                }
                return;
            }
            if (k == 3) {
                if (n <= 3) break;
                System.out.println(n - 1);
                int[][] es = {
                        {1, 2},
                        {2, 3},
                        {3, 4}
                };
                for (int[] e : es)
                    System.out.println(e[0] + " " + e[1]);
                for (int i = 5; i <= n; i++)
                    System.out.println(2 + " " + i);
                return;
            }
            break;
        }
        System.out.println(-1);
    }

    public static void main(String[] args) {
        new Test().start();
    }
}
