import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);

        int n = in.nextInt();
        int m = in.nextInt();
        int s = in.nextInt()-1;
        int t = in.nextInt()-1;
        ArrayList<ArrayList<int[]>> edge_yen = new ArrayList<ArrayList<int[]>>();
        ArrayList<ArrayList<int[]>> edge_snuke = new ArrayList<ArrayList<int[]>>();
        for (int i=0;i<n;i++) {
            ArrayList<int[]> add_yen = new ArrayList<int[]>();
            ArrayList<int[]> add_snuke = new ArrayList<int[]>();
            edge_yen.add(add_yen);
            edge_snuke.add(add_snuke);
        }
        for (int i=0;i<m;i++) {
            int u = in.nextInt()-1;
            int v = in.nextInt()-1;
            int a = in.nextInt();
            int b = in.nextInt();
            int[] add_yen_1 = {v, a};
            int[] add_yen_2 = {u, a};
            int[] add_snuke_1 = {v, b};
            int[] add_snuke_2 = {u, b};
            edge_yen.get(u).add(add_yen_1);
            edge_yen.get(v).add(add_yen_2);
            edge_snuke.get(u).add(add_snuke_1);
            edge_snuke.get(v).add(add_snuke_2);
        }

        long[] dijkstra_yen = new long[n];
        Arrays.fill(dijkstra_yen, -1);
        PriorityQueue<long[]> pq_yen = new PriorityQueue<long[]>((o1, o2)->Long.compare(o1[1], o2[1]));
        long[] first_yen = {s, 0};
        pq_yen.add(first_yen);
        while (!pq_yen.isEmpty()) {
            long[] tmp = pq_yen.poll();
            if (dijkstra_yen[(int)tmp[0]]!=-1) continue;
            dijkstra_yen[(int)tmp[0]] = tmp[1];
            for (int[] arr : edge_yen.get((int)tmp[0])) {
                long[] add_arr = {arr[0], arr[1]+tmp[1]};
                pq_yen.add(add_arr);
            }
        }

        long[] dijkstra_snuke = new long[n];
        Arrays.fill(dijkstra_snuke, -1);
        PriorityQueue<long[]> pq_snuke = new PriorityQueue<long[]>((o1, o2)->Long.compare(o1[1], o2[1]));
        long[] first_snuke = {t, 0};
        pq_snuke.add(first_snuke);
        while (!pq_snuke.isEmpty()) {
            long[] tmp = pq_snuke.poll();
            if (dijkstra_snuke[(int)tmp[0]]!=-1) continue;
            dijkstra_snuke[(int)tmp[0]] = tmp[1];
            for (int[] arr : edge_snuke.get((int)tmp[0])) {
                long[] add_arr = {arr[0], arr[1]+tmp[1]};
                pq_snuke.add(add_arr);
            }
        }

        long[] cost = new long[n];
        TreeMap<Long, Long> map = new TreeMap<Long, Long>();
        for (int i=0;i<n;i++) {
            cost[i] = dijkstra_yen[i]+dijkstra_snuke[i];
            if (map.containsKey(cost[i])) {
                map.put(cost[i], map.get(cost[i])+1);
            } else {
                map.put(cost[i], 1L);
            }
        }
        for (int i=0;i<n;i++) {
            out.println(1_000_000_000_000_000L-map.firstKey());
            if (map.get(cost[i])>1) {
                map.put(cost[i], map.get(cost[i])-1);
            } else {
                map.remove(cost[i]);
            }
        }
        out.close();
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
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

    }
}
