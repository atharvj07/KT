import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class CandidateCode {
    public static void main(String[] args) throws IOException {
        FastReader sc = new FastReader();
        root=new TrieNode();
        addDelete(0,false);
        int q=sc.nextInt();
        StringBuilder sb=new StringBuilder();
        while (q-->0){
            char x=sc.next().charAt(0);
            int y=sc.nextInt();
            if (x=='+'){
                addDelete(y,false);
            }else if (x=='-'){
                addDelete(y,true);
            }else {
                int ans=max(y);
                sb.append((ans^y)+"\n");
            }
        }
        System.out.print(sb);
    }
    static TrieNode root;
    static class TrieNode{
        TrieNode next[];
        int cnt;
        TrieNode(){
            next=new TrieNode[2];
            cnt=0;
        }
    }
    static void addDelete(int x,boolean delete){
        TrieNode tmp=root;
        for (int i=30;i>=0;i--){
            int bit=0;
            if ((x&(1<<i))!=0)bit++;
            if (tmp.next[bit]==null){
                tmp.next[bit]=new TrieNode();
            }
            tmp=tmp.next[bit];
            if (delete){
                tmp.cnt--;
            }else {
                tmp.cnt++;
            }
        }
    }
    static int max(int x){
        int max=0;
        TrieNode tmp=root;
        for (int i=30;i>=0;i--){
            int bit=0;
            if ((x&(1<<i))!=0){
                bit++;
            }
            if (tmp.next[bit^1]!=null && tmp.next[bit^1].cnt>0){
                tmp=tmp.next[bit^1];
                bit^=1;
                max=(max|(bit<<i));
            }else {
                tmp=tmp.next[bit];
                max=(max|(bit<<i));
            }
        }
        return max;
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}