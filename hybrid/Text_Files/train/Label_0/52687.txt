
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static class DisjointUnionSets {
        int[] rank, parent;
        int n;

        // Constructor
        public DisjointUnionSets(int n)
        {
            rank = new int[n];
            parent = new int[n];
            this.n = n;
            makeSet();
        }

        // Creates n sets with single item in each
        void makeSet()
        {
            for (int i = 0; i < n; i++) {
                // Initially, all elements are in
                // their own set.
                parent[i] = i;
            }
        }

        // Returns representative of x's set
        int find(int x)
        {
            // Finds the representative of the set
            // that x is an element of
            if (parent[x] != x) {
                // if x is not the parent of itself
                // Then x is not the representative of
                // his set,
                parent[x] = find(parent[x]);

                // so we recursively call Find on its parent
                // and move i's node directly under the
                // representative of this set
            }

            return parent[x];
        }

        // Unites the set that includes x and the set
        // that includes x
        void union(int x, int y)
        {
            // Find representatives of two sets
            int xRoot = find(x), yRoot = find(y);

            // Elements are in the same set, no need
            // to unite anything.
            if (xRoot == yRoot)
                return;

            // If x's rank is less than y's rank
            if (rank[xRoot] < rank[yRoot])

                // Then move x under y  so that depth
                // of tree remains less
                parent[xRoot] = yRoot;

                // Else if y's rank is less than x's rank
            else if (rank[yRoot] < rank[xRoot])

                // Then move y under x so that depth of
                // tree remains less
                parent[yRoot] = xRoot;

            else // if ranks are the same
            {
                // Then move y under x (doesn't matter
                // which one goes where)
                parent[yRoot] = xRoot;

                // And increment the result tree's
                // rank by 1
                rank[xRoot] = rank[xRoot] + 1;
            }
        }
    }
    static class MyScanner {
        BufferedReader br;
        StringTokenizer st;

        public MyScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

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

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine(){
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }

    }
    static class HashMultiSet<T> implements Iterable<T>
    { private final HashMap<T,Integer> map;
        private int size;
        public HashMultiSet(){map=new HashMap<>(); size=0;}
        public void clear(){map.clear(); size=0;}
        public int size(){return size;}
        public int setSize(){return map.size();}
        public boolean contains(T a){return map.containsKey(a);}
        public boolean isEmpty(){return size==0;}
        public Integer get(T a){return map.getOrDefault(a,0);}
        public void add(T a, int count)
        {
            int cur=get(a);map.put(a,cur+count); size+=count;
            if(cur+count==0) map.remove(a);
        }
        public void addOne(T a){add(a,1);}
        public void remove(T a, int count){add(a,Math.max(-get(a),-count));}
        public void removeOne(T a){remove(a,1);}
        public void removeAll(T a){remove(a,Integer.MAX_VALUE-10);}

        public Iterator<T> iterator()
        {
            return new Iterator<>()
            {
                private final Iterator<T> iter = map.keySet().iterator();
                private int count = 0; private T curElement;

                public boolean hasNext(){return iter.hasNext()||count>0;}
                public T next()
                {
                    if(count==0)
                    {
                        curElement=iter.next();
                        count=get(curElement);
                    }
                    count--; return curElement;
                }
            };
        }
    }
    private  static long abs(long x){ if(x < 0) x*=-1l;return x; }
    private  static int abs(int x){ if(x < 0) x*=-1;return x; }

//    public static int get(HashMap<Integer, Deque<Integer> > a, int key ){
//        return a.get(key).getLast();
//    }
//    public  static  void removeLast (HashMap<Integer,Deque<Integer> > a, int key){
//        if(a.containsKey(key)){
//            a.get(key).removeLast();
//            if(a.get(key).size() == 0) a.remove(key);
//        }
//    }
//    public  static  void add(HashMap<Integer,Deque<Integer>> a, int key, int val){
//        if(a.containsKey(key)){
//            a.get(key).addLast(val);
//        }else{
//            Deque<Integer> b = new LinkedList<>();
//            b.addLast(val);
//            a.put(key,b);
//        }
//    }

    private static void dp(int a[] , int acc[],int n){
        for(int i = n-1;i>=0;i--){
            if(a[i] > 1) acc[i] =1;
            int y =0;
            if(a[i] +i <= n-1) acc[i] += acc[a[i] + i];
        }
    }
    private static void jump(int a[],int index,int n){
        while (index < n){
            int temp = a[index];
            if(a[index] > 1)a[index]--;
            index += temp;
            if(index >= n) break;
        }
    }
    public static void main(String[] args) {
        MyScanner sc = new MyScanner();
        int t =sc.nextInt();
        while (t-- != 0){
           int n = sc.nextInt();
           long a[] = new long[n];
           for(int i=0;i<n;i++){
               a[i] = sc.nextInt();
           }
            long curr[]  = new long[n];
           long ans =0;
           for(int i =0;i<n;i++){
               if(curr[i] < a[i] - 1){
                   ans += (a[i] - 1 - curr[i]);
                   curr[i] = a[i] -1;
               }
               if(i +1 < n)curr[i+1] += curr[i] - a[i] +1;
               for(int j = i+2;j<n && j <= i + a[i];j++){
                   curr[j]++;
               }
           }
           System.out.println(ans);
        }
    }
}