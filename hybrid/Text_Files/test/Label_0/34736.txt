import java.util.*;
import java.util.function.*;
import java.lang.*;
import java.io.*;

class MathLib{
    static long gcd(long a, long b){
        if(a<0) a = -a;
        if(b<0) b = -b;
        if(a>b){
            long t = a;
            a = b;
            b = t;
        }
        while(a>0){
            long r = b%a;
            b = a;
            a = r;            
        }
        return b;
    }
    
    static boolean isPrime(long N){
        if(N%2==0) return false;
        for(long i=3; i*i<=N; i+=2){
            if(N%i==0) return false;
        }
        return true;
    }
    static Counter<Long> factorize(long N){
        Counter<Long> ans = new Counter<>();
        while(N%2==0){
            ans.addOne(2L);
            N /= 2;
        }
        for(long i=3; i*i<=N; i+=2){
            while(N%i==0){
                ans.addOne(i);
                N /= i;
            }
        }
        if(N>1) ans.addOne(N);
        return ans;
    }
    static List<Integer> primeList(int max){
        boolean[] prime = new boolean[max+1];
        Arrays.fill(prime, true); prime[0]=false; prime[1]=false;
        ArrayList<Integer> list = new ArrayList<>();
        for(int n=2; n<=max; n++) if(prime[n]){
            list.add(n);
            if(n*n<=max) for(int m=2*n; m<=max; m+=n) prime[m]=false;
        }
        return list;
    }
}
class Counter<T> extends TreeMap<T,Long>{
    public Counter(){
        super();
    }
    public Counter(List<T> list){
        super();
        for(T e: list) this.addOne(e);
    }
    public Long count(Object elm){
        return getOrDefault(elm,0L);
    }
    public void add(T elm, long amount){
        if(!this.containsKey(elm)) put(elm, amount);
        else replace(elm, get(elm)+amount);
        if(this.count(elm)==0) this.remove(elm);
    }
    public void addOne(T elm){
        this.add(elm, 1);
    }
    public void removeOne(T elm){
        this.add(elm, -1);
    }
    public void removeAll(T elm){
        this.add(elm, this.count(elm));
    }
    public static<T> Counter<T> merge(Counter<T> a, Counter<T> b){
        Counter<T> c = new Counter<>();
        for(T x: a.keySet()) c.add(x, a.count(x));
        for(T y: b.keySet()) c.add(y, b.count(y));
        return c;
    }
}

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        Counter<Long> factorize = MathLib.factorize(N);
        long ans = 0;
        for(long d: factorize.keySet()){
            long k = factorize.count(d);
            for(int i=1;;i++){
                if(k<i) break;
                k -= i;
                ans++;                
            }
        }
        System.out.println(ans);
    }
}
