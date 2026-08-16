import java.awt.Point;
import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;

import static java.lang.Math.*;
import static java.lang.Integer.*;

public class C {

    public static boolean [] generate_primes2(int MAX) { 
        boolean [] isPrime = new boolean [MAX + 1];
        Arrays.fill(isPrime, true);
        int i,j; 
        isPrime[0] = isPrime[1] = false;
        for( i = 2 ; i*i <= MAX ; i++) 
            if (isPrime[i]) 
                for( j = i ; j*i <= MAX ;j++ )
                    isPrime[i*j] = false;
        return isPrime;  
    }
    public static int gcd(int x, int y){
        if(x < y)
            return gcd(y, x);
        if(y == 0)
            return x;
        return gcd(y, x % y);
    }
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        boolean [] isP = generate_primes2(s.length());
        LinkedList<Integer> primes = new LinkedList<Integer>();
        for(int i = 0 ; i < isP.length ; ++i){
            if(!isP[i])continue;
            primes.addLast(i);
        }
        int [] count = new int [26];
        for(int i = 0 ; i < s.length() ; ++i){
            count[s.charAt(i) - 'a']++;
        }
        boolean [] vis = new boolean [primes.size()];
        char [] ans = new char [s.length()];
        for(int i = 0 ; i < primes.size() ; ++i){
            if(vis[i])continue;
            vis[i] = true;
            int cur = primes.get(i);
            LinkedList<Integer> sharing = new LinkedList<Integer>();
            sharing.addLast(cur);
            for(int j = i + 1 ; j < primes.size() ; ++j){
                if(vis[j])continue;
                int cur2 = primes.get(j);
                int lcm = (cur * cur2) / gcd(cur, cur2);
                if(lcm <= s.length()){
                    vis[j] = true;
                    sharing.addLast(cur2);
                }
            }
            LinkedList<Integer> tmp = new LinkedList<Integer>();
            for(int j = 0 ; j < sharing.size() ; ++j){
                int curPrime = sharing.get(j);
                for(int k = 1 ; k <= s.length() / curPrime ; ++k){
                    int t = curPrime * k;
                    if(!tmp.contains(t))tmp.addLast(t);
                }
            }
            int need = tmp.size();
            int min = (int)1e9;
            int best = -1;
            for(int j = 0 ; j < 26 ; ++j){
                if(count[j] >= need && count[j] < min){
                    min = count[j];
                    best = j;
                }
            }
            if(best == -1 || min == (int)1e9){
                System.out.println("NO");
                return;
            }else{
                char correct = (char)('a' + best);
                for(int k = 0 ; k < tmp.size() ; ++k){
                    ans[tmp.get(k) - 1] = correct;
                }
                count[best] -= need;
            }
        }
        boolean f = false;
        for(int i = 0 ; i < count.length ; ++i){
            if(count[i] > 0 ){
                char c = (char)('a' + i);
                ans[0] = c;
                f = true;
                break;
            }
        }
        if(!f){
            System.out.println("NO");
            return;
        }
        System.out.println("YES");
        for(int i = 0 ; i < ans.length ; ++i)
            System.out.print(ans[i]);
    }
}