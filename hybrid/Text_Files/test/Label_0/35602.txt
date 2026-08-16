import java.io.*;
import java.lang.annotation.ElementType;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;


public class  Main{
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        FastInput input = new FastInput(inputStream);
        FastOutput out = new FastOutput(outputStream);
        int n= input.scanInt();
        long a[]=new long [n];
        long many[]=new long [11];
        for(int i=0;i<n;i++){
            a[i]=input.scanInt();

            if(a[i]==1000000000){
                many[10]++;
            }
            for(int j=10,k=1;j<=1000000000;j*=10,k++){
                    if(a[i]==(a[i]%j)) {
                        many[k]++;
                        break;
                    }
            }
        }
        long sum=0,sum1=0;
        for(int i=0;i<n;i++){
            for(long j=1,k=1;j<=1000000000;j*=10,k++){
                long x=  (a[i]%(j*10)-a[i]%j)/j;
                int l=1;
                long time=j;
                for(;l<k;l++){
                    sum+=((x*time*2)%998244353)*many[l]*10;
                    sum=sum%998244353;
                    time*=10;
                }
                for(;l<11;l++){
                    sum+=((x*time)%998244353)*many[l]*10;
                    sum=sum%998244353;
                    sum+=((x*time)%998244353)*many[l];
                    sum=sum%998244353;
                }
            }
            sum=sum%998244353;
        }
        System.out.println(" "+sum);
        out.close();
    }
    static class FastInput {
        private final InputStream is;
        private StringBuilder defaultStringBuf = new StringBuilder(1 << 13);
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;
        public FastInput(InputStream is) {
            this.is = is;
        }
        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }
        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }
        public String next() {
            return readString();
        }
        public int scanInt() {
            int sign = 1;
            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }
            int val = 0;
            while (next >= '0' && next <= '9') {
                val = val * 10 + next - '0';
                next = read();
            }
            return (sign*val);
        }

        public String readString(StringBuilder builder) {
            skipBlank();
            while (next > 32) {
                builder.append((char) next);
                next = read();
            }
            return builder.toString();
        }

        public String readString() {
            defaultStringBuf.setLength(0);
            return readString(defaultStringBuf);
        }

    }
    static class FastOutput implements AutoCloseable, Closeable, Appendable {
        private StringBuilder cache = new StringBuilder(1 << 20);
        private final Writer os;

        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }

        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }

        public FastOutput(Writer os) {
            this.os = os;
        }

        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }

        public FastOutput append(char c) {
            cache.append(c);
            return this;
        }

        public FastOutput append(String c) {
            cache.append(c);
            return this;
        }
        public FastOutput append(int c) {
            cache.append(c);
            return this;
        }
        public FastOutput println(int c) {
            return append(c).println();
        }
        public FastOutput println(String c) {
            return append(c).println();
        }

        public FastOutput println() {
            cache.append(System.lineSeparator());
//            flush();
            return this;
        }

        public FastOutput flush() {
            try {
                os.append(cache);
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }

        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }

        public String toString() {
            return cache.toString();
        }
    }
}