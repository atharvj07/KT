import java.io.*;
import java.util.*;

public class E {

    static class InputReader {
        BufferedReader reader;
        StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }
    }

    static InputReader r = new InputReader(System.in);
    static PrintWriter pw = new PrintWriter(System.out);

    public static void main(String[] args) {

        long n = r.nextLong();
        if(n == 0){
            System.out.println("0 0");
            return;
        }

        long ring = search(n);
        long prev = gg(ring - 1);
        long section = (n - prev) / ring;
        long rem = n - (prev + (ring * section));
        long x, y;
        

        if(section == 6){
            section = 0;
        }

        if(section == 0){
            x = 2 * ring; y = 0;
            x -= rem; y += (2 * rem);
        } else if(section == 1){
            x = 1 * ring; y = 2 * ring;
            x -= (2 * rem);
        } else if(section == 2){
            x = -1 * ring; y = 2 * ring;
            x -= rem; y -= (2 * rem);
        } else if(section == 3){
            x = -2 * ring; y = 0;
            x += rem; y -= (2 * rem);
        } else if(section == 4){
            x = -1 * ring; y = -2 * ring;
            x += 2 * rem;
        } else{ // (section == 5)
            x = 1 * ring; y = -2 * ring;
            x += rem; y += (2 * rem);
        }
        pw.println(x + " " + y + " ");
        pw.close();
    }

    static long search(long n) {
        long left = 0;
        long right = (int) 6E8;
        while (left < right) {
            long mid = left + (right - left) / 2;
            if (gg(mid) < n && gg(mid + 1) > n) {
                return 1 + mid;
            } else if(gg(mid) == n){
                return mid;
            }
            else if (gg(mid) > n) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }

    static long gg(long n) {
        return (3 * n * (n + 1));
    }
}

/**
 * _ _ _ | | | | | | ___ ___ __| | ___ | |__ _ _ __| | __ _ _ __ _ __ ___ _ __ _
 * _ __ _ ___ / __/ _ \ / _` |/ _ \ | '_ \| | | | / _` |/ _` | '__| '__/ _ \ '_
 * \ | | | |/ _` |/ _ \ | (_| (_) | (_| | __/ | |_) | |_| | | (_| | (_| | | | |
 * | __/ | | | | |_| | (_| | (_) | \___\___/ \__,_|\___| |_.__/ \__, |
 * \__,_|\__,_|_| |_| \___|_| |_| \__, |\__,_|\___/ __/ | ______ __/ | |___/
 * |______|___/
 */