import java.io.*;
import java.util.*;
import static java.util.Collections.*;
import static java.lang.Math.*;
import java.util.stream.*;

@SuppressWarnings("unchecked")
public class Main {
    public static PrintWriter out;
    public static InputReader in;
    public static long MOD = (long)1e9+7;
    static class tnode{
        public tnode[] nex;
        public boolean isLast;
        public tnode(){
            nex = new tnode[26];
            for(int i=0;i<26;i++) nex[i]=null;
            isLast = false;
        }
    }
    public static void insert(tnode node, String s){
        int n = s.length();
        for(int i=0;i<n;i++){
            char c = s.charAt(i);
            int pos = c-'a';
            if(node.nex[pos]==null) node.nex[pos] = new tnode();
            node = node.nex[pos];
        }
        node.isLast = true;
    }
    public static void main(String[] args)throws IOException {
        in = new InputReader(System.in);
        out = new PrintWriter(System.out);
        
        int n = in.nextInt();
        tnode root = new tnode();
        var arr = new ArrayList<String>();
        for(int t = 0; t < n; t++){
            String s = in.next();
            s = new StringBuilder(s).reverse().toString();
            arr.add(s);
            insert(root,s);
        }
        long ans = 0l;
        for(int i=0;i<n;i++){
            String s = arr.get(i);
            char c[] = s.toCharArray();
            int ln = s.length();
            tnode node = root;
            int pos[] = new int[26];
            Arrays.fill(pos,-1);
            for(int j=0;j<ln;j++){
                pos[c[j]-'a'] = j;
            }
            // out.println("ln="+ln);
            for(int j=-1;j<ln;j++){
                if(j!=-1){
                    node = node.nex[c[j]-'a'];
                }
                // if(node.isLast) ans++;
                for(int k=0;k<26&&j!=ln-2;k++){
                    if(pos[k]>j && node.nex[k]!=null && node.nex[k].isLast) {ans++;}
                        // out.println("j="+j+",k="+k);}; 
                }
            }
            // out.println("i="+i+",ans="+ans);
        }
        out.println(ans);
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

        public int[] nextArrI(int n) {
            int[] a=new int[n];
            for(int i=0; i<n; i++) a[i]=nextInt();
            return a;
        }
        
        public long[] nextArrL(int n) {
            long[] a=new long[n];
            for (int i=0; i<n; i++) a[i]=nextLong();
            return a;
        }
    }

}