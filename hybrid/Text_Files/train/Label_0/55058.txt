import java.io.*;
import java.util.*;

public class CF_mahmoud_and_dictionary {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        PrintWriter out = new PrintWriter(System.out);
        StringBuilder sb = new StringBuilder("");
        int n=sc.nextInt();
        int m=sc.nextInt();
        int q=sc.nextInt();
        TreeMap<String,Integer> names=new TreeMap<>();
        String []s=sc.nextLine().split(" ");
        for (int i = 0; i < n; i++) {
            names.put(s[i],i);
        }
        UnionFind sets=new UnionFind(n);
        int opposite[]=new int[n];
        Arrays.fill(opposite,-1);
        for (int i = 0; i <m ; i++) {
            s=sc.nextLine().split(" ");
            int first=sets.findSet(names.get(s[1]));
            int last=sets.findSet(names.get(s[2]));
            if(s[0].equals("1")){

                if(opposite[first]==last||opposite[last]==first){
                    out.println("NO");
                }else
                {
                    sets.unionSet(first,last);
                    out.println("YES");
                    if(opposite[first]!=-1&&opposite[last]!=-1)
                    {
                        sets.unionSet(opposite[first],opposite[last]);
                        opposite[sets.findSet(opposite[first])]=sets.findSet(first);
                        continue;

                    }
                    if(opposite[first]==-1&&opposite[last]!=-1){
                        opposite[last]=sets.findSet(opposite[last]);
                        opposite[first]=opposite[last];
                        opposite[opposite[last]]=sets.findSet(last);
                        continue;
                    }
                    if(opposite[last]==-1&&opposite[first]!=-1){
                        opposite[first]=sets.findSet(opposite[first]);
                        opposite[last]=opposite[first];
                        opposite[opposite[first]]=sets.findSet(first);
                    }

                }


            }else {

                if(sets.isSameSet(first,last)){
                    out.println("NO");
                }else {

                    if(opposite[first]==-1)opposite[first]=sets.findSet(last);
                    if(opposite[last]==-1)opposite[last]=sets.findSet(first);
                    sets.unionSet(first,opposite[last]);
                    sets.unionSet(last,opposite[first]);
                    opposite[sets.findSet(first)]=sets.findSet(last);
                    opposite[sets.findSet(last)]=sets.findSet(first);
                    out.println("YES");
                }

            }
        }
        //System.out.println(Arrays.toString(opposite));
        for (int i = 0; i <q ; i++) {
            s=sc.nextLine().split(" ");
            int first=names.get(s[0]);
            int last=names.get(s[1]);
            if(sets.isSameSet(first,last)){
                out.println(1);
            }else{
                int s1=sets.findSet(first);
                int s2=sets.findSet(last);
                if (opposite[s1]==s2||opposite[s2]==s1) 
                        out.println(2);
                    else
                        out.println(3);
            }


        }
        out.flush();
    }






    static class UnionFind {
        int[] p, rank, setSize;
        int numSets;

        public UnionFind(int N)
        {
            p = new int[N];
            rank = new int[N];
            setSize = new int[N];
            numSets = N;
            for (int i = 0; i < N; i++) {  p[i] = i; setSize[i] = 1; }
        }

        public int findSet(int i)
        {
            if (p[i] == i) return i;
            else return p[i] = findSet(p[i]);
        }

        public Boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

        public void unionSet(int i, int j)
        {
            if (isSameSet(i, j))
                return;
            numSets--;
            int x = findSet(i), y = findSet(j);
            // rank is used to keep the tree short
            if (rank[x] > rank[y]) { p[y] = x; setSize[x] += setSize[y]; }
            else
            {	p[x] = y; setSize[y] += setSize[x];
                if(rank[x] == rank[y]) rank[y]++;
            }
        }

        public int numDisjointSets() { return numSets; }

        public int sizeOfSet(int i) { return setSize[findSet(i)]; }
    }
    static class Scanner {
        StringTokenizer st;
        BufferedReader br;

        public Scanner(InputStream s) {
            br = new BufferedReader(new InputStreamReader(s));
        }

        public String next() throws IOException {
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public String nextLine() throws IOException {
            return br.readLine();
        }

        public double nextDouble() throws IOException {
            String x = next();
            StringBuilder sb = new StringBuilder("0");
            double res = 0, f = 1;
            boolean dec = false, neg = false;
            int start = 0;
            if (x.charAt(0) == '-') {
                neg = true;
                start++;
            }
            for (int i = start; i < x.length(); i++)
                if (x.charAt(i) == '.') {
                    res = Long.parseLong(sb.toString());
                    sb = new StringBuilder("0");
                    dec = true;
                } else {
                    sb.append(x.charAt(i));
                    if (dec)
                        f *= 10;
                }
            res += Long.parseLong(sb.toString()) / f;
            return res * (neg ? -1 : 1);
        }

        public boolean ready() throws IOException {
            return br.ready();
        }


    }
}