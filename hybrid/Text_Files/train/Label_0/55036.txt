import java.io.*;
import java.math.*;
import java.util.*;

// printArr() - prints the array
// intList, doubleList, longList
// nextIntArray

/* stuff you should look for
 * int overflow, array bounds
 * special cases (n=1?)
 * do smth instead of nothing and stay organized
 * WRITE STUFF DOWN
 */

public class current {
    public static void main(String[] args) {
        FastReader fr = new FastReader();
        // DO NOT FORGET TO REMOVE WHILE LOOP!!!!!!!!!!!!!!!
        //while (true) {
            int[] arr = fr.nextIntArray();
            solve(arr[0], arr[1], fr.nextIntArray());
        //}
    }

    static void solve(int cities, int roads, int[] arr) {
        if (roads < cities+1 || cities<5) {
            System.out.println(-1);
            return;
        }
        System.out.print(arr[0] + " " + arr[2] + " ");
        for (int i = 1; i<=cities; i++) {
            if (i != arr[0] && i != arr[1] && i != arr[2] && i != arr[3]) {
                System.out.print(i + " ");
            }
        }
        System.out.print(arr[3] + " " + arr[1]);
        System.out.println();
        System.out.print(arr[2] + " " + arr[0] + " ");
        for (int i = 1; i <= cities; i++) {
            if (i != arr[0] && i != arr[1] && i != arr[2] && i != arr[3]) {
                System.out.print(i + " ");
            }
        }
        System.out.print(arr[1] + " " + arr[3]);
        System.out.println();
    }

    static int max(Map<Integer, Integer> map) {
        int max = Integer.MIN_VALUE;
        int index = -1;
        for (int i : map.keySet()) {
            if (map.get(i) >= max) {
                max = map.get(i);
                index = Math.min(index, i);
            }
        }
        return index;
    }

    static void shuffleArray(int[] arr){
        int n = arr.length;
        Random rnd = new Random();
        for(int i=0; i<n; ++i){
            int tmp = arr[i];
            int randomPos = i + rnd.nextInt(n-i);
            arr[i] = arr[randomPos];
            arr[randomPos] = tmp;
        }
    }

    static class Coord {
        public int x;
        public int y;

        public Coord (int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Coord coord = (Coord) o;
            return x == coord.x &&
                    y == coord.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static Set<Integer> get(List<Set<Integer>> graph, int i) {
        try {
            return graph.get(i);
        } catch (IndexOutOfBoundsException e) {
            return new HashSet<>();
        }
    }

    public static void printArr(int[] a) {
        System.out.println(Arrays.toString(a));
    }

    public static int[] bfs(List<Set<Integer>> graph, int v) {
        int l = graph.size();
        Deque<Integer> list = new ArrayDeque<>();
        list.add(v);
        boolean[] seen = new boolean[l];
        int distance = 0;
        int node = v;
        int size = 1;
        int index = 0;
        // Iterate over every single vertice and edge
        // O(V+E) -> O(V) for trees
        while (!list.isEmpty()) {
            int cur = list.poll();
            seen[cur] = true;
            node = cur;

            index++;
            if (index > size) {
                distance++;
                size = list.size();
                index = 0;
            }

            for (int i : graph.get(cur)) {
                if (!seen[i]) {
                    seen[i] = true;
                    list.add(i);
                }
            }
        }
        return new int[]{node, distance};
    }

    static class SegTree {
        int startIndex, endIndex;
        long sum;
        SegTree lchild, rchild;

        SegTree(int[] arr) {this(0, arr.length-1, arr);}

        SegTree(int startIndex, int endIndex, int[] arr) {
            this.startIndex = startIndex;
            this.endIndex = endIndex;
            if (startIndex == endIndex) sum = arr[startIndex];
            else {
                int mid = (startIndex + endIndex) / 2;
                lchild = new SegTree(startIndex, mid, arr);
                rchild = new SegTree(mid + 1, endIndex, arr);
                sum = lchild.sum + rchild.sum;
                recalc();
            }
        }

        void recalc() {
            if (startIndex == endIndex) return; sum = lchild.sum + rchild.sum;
        }

        public void valueUpdate(int index, int value) {
            if (startIndex == endIndex) {sum = value; return;}
            if (index > lchild.endIndex) rchild.valueUpdate(index, value); else lchild.valueUpdate(index, value); recalc();
        }

        public long rangeSum(int startIndex, int endIndex) {
            if (endIndex < this.startIndex || startIndex > this.endIndex) return 0;
            if (startIndex <= this.startIndex && endIndex >= this.endIndex) return sum;
            return lchild.rangeSum(startIndex, endIndex) + rchild.rangeSum(startIndex, endIndex);
        }
    }

    public static double sum(List<Long> n) {
        double a = 0;
        for (long i : n) {
            a += i;
        }
        return a;
    }

    public static int toInt(String n) {
        return Integer.parseInt(n);
    }

    public static double toDouble(String n) {
        return Double.parseDouble(n);
    }

    public static long toLong(String n) {
        return Long.parseLong(n);
    }

    static class FastReader {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        String nextLine() {
            String a = "";
            try {
                a = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return a;
        }

        int[] nextIntArray() {
            return intArray(nextLine().split(" "));
        }

        long[] nextLongArray() {
            return longArray(nextLine().split(" "));
        }

        double[] nextDoubleArray() {
            return doubleArray(nextLine().split(" "));
        }

        public int getInt(int index) {
            String[] arr = nextLine().split(" ");
            return Integer.parseInt(arr[index]);
        }

        public long getLong(int index) {
            String[] arr = nextLine().split(" ");
            return Long.parseLong(arr[index]);
        }

        public double getDouble(int index) {
            String[] arr = nextLine().split(" ");
            return Double.parseDouble(arr[index]);
        }

        public List<String> stringList() {
            String[] arr = nextLine().split(" ");
            return Arrays.asList(arr);
        }

        public List<Integer> intList() {
            String[] arr = nextLine().split(" ");
            List<Integer> a = new ArrayList<>();
            for (String i : arr) {
                a.add(Integer.parseInt(i));
            }
            return a;
        }

        public List<Double> doubleList() {
            String[] arr = nextLine().split(" ");
            List<Double> a = new ArrayList<>();
            for (String i : arr) {
                a.add(Double.parseDouble(i));
            }
            return a;
        }

        public List<Long> longList() {
            String[] arr = nextLine().split(" ");
            List<Long> a = new ArrayList<>();
            for (String i : arr) {
                a.add(Long.parseLong(i));
            }
            return a;
        }
    }


    public static int[] intArray(String[] arr) {
        int l = arr.length;
        int[] a = new int[l];
        for (int i = 0; i < l; i++) {
            a[i] = Integer.parseInt(arr[i]);
        }
        return a;
    }

    public static long[] longArray(String[] arr) {
        int l = arr.length;
        long[] a = new long[l];
        for (int i = 0; i < l; i++) {
            a[i] = Long.parseLong(arr[i]);
        }
        return a;
    }

    public static double[] doubleArray(String[] arr) {
        int l = arr.length;
        double[] a = new double[l];
        for (int i = 0; i < l; i++) {
            a[i] = Double.parseDouble(arr[i]);
        }
        return a;
    }
}