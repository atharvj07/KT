import java.util.*;
import java.io.*;


public class ProbC {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Task solver = new Task();
        solver.solve(in, out);
        out.close();
    }
    // main solver
    static class Task{
        static ArrayList<Integer> e[] = new ArrayList[26];
        public void solve(InputReader in, PrintWriter out) {
            int test = Integer.parseInt(in.nextToken());
            for (int i = 0; i < test; i++) {
                String s = in.nextToken();
                String t = in.nextToken();
                int ls = s.length();
                int lt = t.length();
                int j;
                for (j = 0; j < 26; j++){
                    e[j] = new ArrayList<>();
                }
                for (j = 0; j < ls; j++){
                    e[s.charAt(j) - 'a'].add(j);
                }
                j = 0;
                int cnt = 0;
                while (j < lt){
                    int ch = t.charAt(j) - 'a';
                    if (e[ch].size() == 0){
                        cnt = -1;
                        break;
                    }
                    else{
                        int idx = e[ch].get(0);
                        j++;
                        cnt++;
                        while (j < lt){
                            ch = t.charAt(j) - 'a';
                            idx =  binarySearch(e[ch], idx + 1);
                            if (idx == -1){
                                break;
                            }
                            else{
                                j++;
                            }
                        }
                    }
                }
                out.println(cnt);
            }
        }

        private int binarySearch(ArrayList<Integer> l, int t) {
            int beg = 0;
            int end = l.size() - 1;
            if (beg > end){
                return -1;
            }
            while(beg < end - 1){
                int mid = (beg + end) / 2;
                if (l.get(mid) >= t){
                    end = mid;
                }
                else{
                    beg = mid + 1;
                }
            }
            if (l.get(beg) >= t){
                return l.get(beg);
            }
            else if (l.get(end) >= t){
                return l.get(end);
            }
            else{
                return -1;
            }
        }
    }
    // fast input reader class;
    static class InputReader {
        BufferedReader br;
        StringTokenizer st;

        public InputReader(InputStream stream) {
            br = new BufferedReader(new InputStreamReader(stream));
        }

        public String nextToken() {
            while (st == null || !st.hasMoreTokens()) {
                String line = null;
                try {
                    line = br.readLine();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
                if (line == null) {
                    return null;
                }
                st = new StringTokenizer(line);
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(nextToken());
        }
        public long nextLong(){
            return Long.parseLong(nextToken());
        }
    }
}

