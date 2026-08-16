import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args){
        FastScanner fsc=new FastScanner();
        int n=fsc.nextInt();
        long[][] ab=new long[2*n][3];
        long[] a=new long[n];
        for(int i=0;i<n;i++) a[i]=fsc.nextLong();
        long[] b=new long[n];
        for(int i=0;i<n;i++) b[i]=fsc.nextLong();
        fsc.close();
        for(int i=0;i<n;i++){
            ab[i][0]=a[i];
            ab[i][1]=0;
            ab[i][2]=i;
        }
        for(int i=0;i<n;i++){
            ab[n+i][0]=b[i];
            ab[n+i][1]=1;
            ab[n+i][2]=i;
        }
        Arrays.sort(ab, (u, v)->u[0]>v[0]?1:u[0]<v[0]?-1:u[1]>v[1]?1:u[1]<v[1]?-1:0);
        int ac=0, bc=0;
        boolean flg=false;
        int[] aind=new int[n];
        int[] bind=new int[n];
        int[] arev=new int[n];
        int i1=0, i2=0;
        for(int i=0;i<2*n;i++){
            if(ab[i][1]==0){
                aind[i1]=(int) ab[i][2];
                arev[aind[i1]]=i1;
                i1++;
            }
            else{
                bind[i2]=(int) ab[i][2];
                i2++;
            }
        }
        for(int i=0;i<2*n;i++){
            if(ab[i][1]==0) ac++;
            else bc++;
            if(ac>bc+1) flg=true;
            if(ac<bc){
                System.out.println("No");
                return;
            }
        }
        if(flg) System.out.println("Yes");
        else{
            int tm=0;
            for(int i=0;i<n;i++){
                if(aind[i]!=bind[i]){
                    swap(aind, i, arev[bind[i]]);
                    swap(arev, aind[i], aind[arev[bind[i]]]);
                    tm++;
                }
            }
            if(tm<=n-2) System.out.println("Yes");
            else System.out.println("No");
        }
    }
    static void swap(int[] array, int u, int v){
        int tmp=array[u];
        array[u]=array[v];
        array[v]=tmp;
    }
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1024];
        private int ptr = 0;
        private int buflen = 0;
        private boolean hasNextByte(){
            if(ptr<buflen) return true;
            else{
                ptr = 0;
                try{
                    buflen = in.read(buffer);
                }
                catch(IOException e){
                    e.printStackTrace();
                }
                if(buflen<=0) return false;
            }
        return true;
        }
        private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
        private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
        public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
        public String next() {
            if (!hasNext()) throw new NoSuchElementException();
            StringBuilder sb = new StringBuilder();
            int b = readByte();
            while(isPrintableChar(b)) {
                sb.appendCodePoint(b);
                b = readByte();
            }
            return sb.toString();
        }
        public long nextLong() {
            if (!hasNext()) throw new NoSuchElementException();
            long n = 0;
            boolean minus = false;
            int b = readByte();
            if (b == '-') {
                minus = true;
                b = readByte();
            }
            if (b < '0' || '9' < b) throw new NumberFormatException();
            while(true){
                if ('0' <= b && b <= '9') {
                    n *= 10;
                    n += b - '0';
                }
                else if(b == -1 || !isPrintableChar(b)) return minus ? -n : n;
                else throw new NumberFormatException();
                b = readByte();
            }
        }
        public int nextInt() {
            long nl = nextLong();
            if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
            return (int) nl;
        }
        public double nextDouble() { return Double.parseDouble(next());}
        public void close(){
            try{in.close();}
            catch(IOException e){e.printStackTrace();}
        }
    }
}