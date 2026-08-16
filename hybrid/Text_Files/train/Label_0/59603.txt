

import java.io.*;
import java.util.*;


/**
 * AIZU ONLINE JUDGE ddd
 * 3121
 *  2020/5/3
 */
public class Main {


    class ABCD {
        int a;
        int b;
        int c;
        int d;
        public ABCD(int a, int b, int c, int d) {
            this.a = a;
            this.b = b;
            this.c = c;
            this.d = d;
        }
        public ABCD(int a) {
            this.a = a;
        }
    }

    boolean main() throws IOException {

        Scanner sc = new Scanner(systemin);

        int N = sc.nextInt();
        int Q = sc.nextInt();

        List<ABCD> list = new ArrayList<>();

        loop:
        for(int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int d = sc.nextInt();
            if (list.size() < 100) {
                for(ABCD t : list) {
                    if (a == t.a && b == t.b && c == t.c && d == t.d)
                        continue loop;
                }
            }
            list.add(new ABCD(a, b, c, d));
        }

        // aの昇順
        Comparator<ABCD> comp = (s, t) -> s.a - t.a;
        Collections.sort(list, comp);

        for(int j = 0; j < Q; j++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            int w = sc.nextInt();
            boolean yes = false;

            int k = Collections.binarySearch(list, new ABCD(x - 1), comp);
            if (k < 0)
                k = -k - 1;

            for(int i = k; i < list.size(); i++) {
                ABCD a = list.get(i);
                if (a.a >= y)
                    break;
                if (x < a.a && a.a < y && y < a.b &&
                    z < a.c && a.c < w && w < a.d) {
                    yes = true;
                    break;
                }
            }
            System.out.printf("%s\n", yes ? "Yes" : "No");
        }

        sc.close();
        return false;
    }



    PrintStream log;
    PrintStream result = System.out;
    BufferedReader systemin;

    static Main instance = new Main();

    Main() {
        systemin = new BufferedReader(new InputStreamReader(System.in));
        log = new PrintStream(new OutputStream() { public void write(int b) {} } );
    }

    public static void main(String[] args) throws IOException {

        instance.main();
        instance.systemin.close();
    }


}


