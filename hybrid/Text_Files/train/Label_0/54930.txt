import java.io.*;
import java.util.*;

public class Solution670C {
    public static void main(String... bob) throws Exception {
        FAST in = new FAST();
        WriteMe out = new WriteMe();
        int N = in.nextInt();
        final Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < N; i++) {
            int tmp = in.nextInt();
            int count = map.containsKey(tmp) ? map.get(tmp) : 0;
            map.put(tmp, count + 1);
        }
        int M = in.nextInt();
        int[] audio = new int[M];
        for (int i = 0; i < M; i++) {
            audio[i] = in.nextInt();
        }
        int[] subtitle = new int[M];
        for (int i = 0; i < M; i++) {
            subtitle[i] = in.nextInt();
        }
        List<int[]> data = new ArrayList<int[]>();
        for (int i = 0; i < M; i++) {
            data.add(new int[]{i, audio[i], subtitle[i]});
        }
//        System.out.println(map);
//        for (int[] ints : data) {
//            System.out.println(Arrays.toString(ints));
//        }
//        System.out.println();
        Collections.sort(data, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                int aAudio = map.containsKey(a[1]) ? map.get(a[1]) : -1;
                int bAudio = map.containsKey(b[1]) ? map.get(b[1]) : -1;
                int aSubtitle = map.containsKey(a[2]) ? map.get(a[2]) : -1;
                int bSubtitle = map.containsKey(b[2]) ? map.get(b[2]) : -1;
                if (aAudio != -1 && bAudio != -1) {
                    if (aAudio == bAudio) {
                        return -(aSubtitle - bSubtitle);
                    } else {
                        return -(aAudio - bAudio);
                    }
                } else {
                    return bAudio;
                }
            }
        });
//        for (int[] ints : data) {
//            System.out.println(Arrays.toString(ints));
//        }
        System.out.println(data.get(0)[0] + 1);

        out.close();
    }

    static class WriteMe {
        private PrintWriter out;

        public WriteMe() {
            try {
                out = new PrintWriter(new BufferedWriter(new FileWriter("Solution670C.out")));
            } catch (Exception e) {

            }
        }

        public void caseInt(int num, int ans) {
            caseStr(num, String.valueOf(ans));
        }

        public void caseStr(int num, String ans) {
            out.printf("Case #%d: %s\n", num, ans);
        }

        public void writeln(String str) {
            out.println(str);
        }

        public void write(String str) {
            out.print(str);
        }

        public void close() {
            out.close();
        }
    }

    static class FAST {
        private BufferedReader in;
        private StringTokenizer str;

        public FAST() {
            in = new BufferedReader(new InputStreamReader(System.in));
            // in = new BufferedReader(new FileReader("Solution670C.in"));
        }

        private String next() {
            while (str == null || !str.hasMoreElements()) {
                try {
                    str = new StringTokenizer(in.readLine());
                } catch (IOException e) {
                }
            }
            return str.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public String nextLine() throws Exception {
            return in.readLine();
        }
    }
}
