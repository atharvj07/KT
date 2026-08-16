import java.io.*;
import java.util.*;
import java.math.*;

public class utkarsh {

    InputStream is;
    PrintWriter out;
    
    long maxl = 4L * (long)1e18, mod = (long)1e9 + 7L;
    int p[], maxi = 2 * (int)1e9, sz, np = 15485900, modi = (int)1e9 + 7;
    boolean b[];    // = isPrime();
    
    class pair{
        int F, S;
        pair(int a, int b){
            F = a;
            S = b;
        }
    }
    
    void solve(){
        //Enter code here utkarsh
        //sz=sieve(); //sz = 1000001;
        //out.println(sz);
        int i, j, n, k;
        n = ni();
        k = ni();
        int a[] = na(n);
        int b[] = na(n);
        long ans = 0;
        pair d[] = new pair[n];
        j = 0;
        for(i = 0; i < n; i++){
            if(a[i] <= b[i]){
                k--;
                ans += a[i];
            }else{
                d[j++] = new pair(a[i], b[i]);
            }
        }
        if(k <= 0){
            for(i = 0; i < j; i++){
                ans += d[i].S;
            }
        }else{
            Arrays.sort(d, 0, j, (pair u, pair v) -> ((u.F - u.S) - (v.F - v.S)));
            for(i = 0; i < k; i++){
                ans += d[i].F;
            }
            for( ; i < j; i++){
                ans += d[i].S;
            }
        }
        out.println(ans);
    }
    
    int sieve(){ int i, j, n = np; b = new boolean[n]; for(i = 3; i < n; i += 2){ b[i] = true; } b[2] = true; for(i = 3; i * i <= n; i += 2){ if(b[i]){ for(j = i * i; j < n; j += i){ b[j] = false; } } } p = new int[n]; p[0] = 2; j = 1; for(i = 3; i < n; i += 2){ if(b[i]){ p[j++] = i; } } p=Arrays.copyOf(p,j); return j;
    }
    long modpow(long base, long exp, long modulus) { base %= modulus; long result = 1L; while (exp > 0) { if ((exp & 1)==1) result = (result * base) % modulus; base = (base * base) % modulus; exp >>= 1; } return result;
    }
    
    public static void main(String[] args) { new utkarsh().run();
    }
    void run(){ is = System.in; out = new PrintWriter(System.out); solve(); out.flush();
    }
    
    byte input[] = new byte[1024];
    int len = 0, ptr = 0;
    
    int readByte(){ if(ptr >= len){ ptr = 0; try{ len = is.read(input); }catch(IOException e){ throw new InputMismatchException(); } if(len <= 0){ return -1; } } return input[ptr++];
    }
    boolean isSpaceChar(int c){ return !( c >= 33 && c <= 126 ); 
    }
    int skip(){ int b = readByte(); while(b != -1 && isSpaceChar(b)){ b = readByte(); } return b;
    }
    
    char nc(){ return (char)skip();
    }
    String ns(){ int b = skip(); StringBuilder sb = new StringBuilder(); while(!isSpaceChar(b)){ sb.appendCodePoint(b); b=readByte(); } return sb.toString();
    }
    int ni(){ int n = 0,b = readByte(); boolean minus = false; while(b != -1 && !( (b >= '0' && b <= '9') || b == '-')){ b = readByte(); } if(b == '-'){ minus = true; b = readByte(); } if(b == -1){ return -1; } while(b >= '0' && b <= '9'){ n = n * 10 + (b - '0'); b = readByte(); } return minus ? -n : n;
    }
    long nl(){ long n = 0L; int b = readByte(); boolean minus = false; while(b != -1 && !( (b >= '0' && b <= '9') || b == '-')){ b = readByte(); } if(b == '-'){ minus = true; b = readByte(); } while(b >= '0' && b <= '9'){ n = n * 10 + (b - '0'); b = readByte(); } return minus ? -n : n;
    }
    double nd(){ return Double.parseDouble(ns());
    }
    float nf(){ return Float.parseFloat(ns());
    }
    int[] na(int n){ int a[] = new int[n]; for(int i = 0; i < n; i++){ a[i] = ni(); } return a;
    }
    char[] ns(int n){ char c[] = new char[n]; int i,b = skip(); for(i = 0; i < n; i++){ if(isSpaceChar(b)){ break; } c[i] = (char)b; b = readByte(); } return i == n ? c : Arrays.copyOf(c,i);
    }
}