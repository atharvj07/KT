/*
String[]の初期化、整数の型がlongになっているか
関数（splitとかcontainsとか）内では"+"とかは正規表現となされるので"\\+"とする
配列のコピーはarr1=arr.clone()
HashSet<>[]はおのおの初期化した？？？？？
負の数の割り算は絶対値が小さいほうに切り捨てられるex.-1/2=0ので、ある値>kみたいな式だとバグらせやすいので注意
ある値>=kとして、切り上げた値をとるべき
toLowerCase()はアルファベット以外に対して行ってもエラーにはならない
ArrayDequeではpopとpushはStackと同じ操作になる
 */
//入力終了→Ctrl+D
//https://onlinejudge.u-aizu.ac.jp/#/problems/1257
import java.util.*;
import java.awt.*;
import java.awt.geom.Point2D;
import static java.lang.System.*;
import static java.lang.Math.*;
public class Main {
    public static void main(String[] $) {
        Scanner sc = new Scanner(in);
        int[] prime=Generate_prime(1000000);
        int m=prime.length;
        while (sc.hasNext()) {
            int n = sc.nextInt();
            if(n==0)exit(0);
            int ans = 0, sum = 0, right = 0;
            for (int left = 1; left < m + 1; left++) {
                while (right<m&&sum+prime[right]<n){
                    sum+=prime[right];
                    right++;
                }
                if(right<m&&sum+prime[right]==n){
                    ans++;
                }
                if(right==left)right++;
                else sum-=prime[left];
            }
            out.println(ans);
        }
    }
    static int[] Generate_prime(int n) {
        ArrayList<Integer> prime = new ArrayList<>();
        prime.add(2);
        prime.add(3);
        for (int i = 6; i <= n; i += 6) {
            int p1 = i - 1, p2 = i + 1;
            if (isPrime(p1)) prime.add(p1);
            if (isPrime(p2)) prime.add(p2);
        }
        int t=prime.size();
        int[] Generated_prime=new int[t+1];
        //Iteratorでもよい
        for (int i=1;i<=t;i++){
            Generated_prime[i]=prime.get(i-1);
        }
        return Generated_prime;
    }
    static boolean isPrime(int p){
        if(p==1)return false;
        int t= (int) (sqrt(p)+1);
        boolean f=true;
        for (int i = 5; i <= t && f; i++) if(p%i==0) f=false;
        return f;
    }
}
