//package com.company;
import java.util.*;
import java.lang.*;
import java.io.*;
//****Use Integer Wrapper Class for Arrays.sort()****
public class Main {
    static PrintWriter out=new PrintWriter(new OutputStreamWriter(System.out));
    public static void main(String[] Args)throws Exception{
        FastReader scan=new FastReader(System.in);
        int t=1;
//        t=scan.nextInt();
        while(t-->0){
            long n=scan.nextLong();
            long x=scan.nextInt();
            long m=scan.nextInt();
            Set<Long> s=new HashSet<>();
            ArrayList<Long> arr=new ArrayList<>();
            long cur=x;
            s.add(x);
            arr.add(x);
            long rep=-1;
            long sum=0;
            while(true){
                cur=(cur*(cur%m))%m;
                if(s.contains(cur)){
                    rep=cur;
                    break;
                }
                s.add(cur);
                arr.add(cur);
            }
            long ans=0;
            int ri=-1;
            for(int i=0;i<arr.size();i++){
                if(arr.get(i)==rep){
                    ri=i;
                }
            }
            for(int i=0;i<ri&&n>0;i++){
                ans+=arr.get(i);
                n--;
            }
            for(int i=ri;i<arr.size();i++){
                sum+=arr.get(i);
            }
            int size=arr.size()-ri;
            ans+=(n/size)*sum;
            long rem=n%size;
            for(int i=0;i<(int)rem;i++){
                ans+=arr.get(ri+i);
            }
            out.println(ans);
        }
        out.flush();
        out.close();
    }
    static class FastReader {

        byte[] buf = new byte[2048];
        int index, total;
        InputStream in;

        FastReader(InputStream is) {
            in = is;
        }

        int scan() throws IOException {
            if (index >= total) {
                index = 0;
                total = in.read(buf);
                if (total <= 0) {
                    return -1;
                }
            }
            return buf[index++];
        }

        String next() throws IOException {
            int c;
            for (c = scan(); c <= 32; c = scan()) ;
            StringBuilder sb = new StringBuilder();
            for (; c > 32; c = scan()) {
                sb.append((char) c);
            }
            return sb.toString();
        }

        int nextInt() throws IOException {
            int c, val = 0;
            for (c = scan(); c <= 32; c = scan()) ;
            boolean neg = c == '-';
            if (c == '-' || c == '+') {
                c = scan();
            }
            for (; c >= '0' && c <= '9'; c = scan()) {
                val = (val << 3) + (val << 1) + (c & 15);
            }
            return neg ? -val : val;
        }
        long nextLong() throws IOException {
            int c;
            long val = 0;
            for (c = scan(); c <= 32; c = scan()) ;
            boolean neg = c == '-';
            if (c == '-' || c == '+') {
                c = scan();
            }
            for (; c >= '0' && c <= '9'; c = scan()) {
                val = (val << 3) + (val << 1) + (c & 15);
            }
            return neg ? -val : val;
        }
    }
}
