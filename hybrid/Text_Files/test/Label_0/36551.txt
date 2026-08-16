

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    static final int MAX = 1001;
    static final long MOD = (long) 1e9 + 7;
    static boolean[] isPrime;
    static ArrayList<Integer> primes;
    static long[] cnt;

    static void sieve() {
	isPrime = new boolean[MAX];
	Arrays.fill(isPrime, true);
	isPrime[0] = isPrime[1] = false;
	primes = new ArrayList<>();
	for (int i = 2; i < MAX; i++)
	    if (isPrime[i]) {
		for (int j = i * i; j < MAX; j += i)
		    isPrime[j] = false;
		primes.add(i);
	    }
    }

    static void f(int N) {
	int idx = 0;
	int pf = primes.get(idx);
	while (pf * pf <= N) {
	    int power = 0;
	    while (N % pf == 0) {
		N /= pf;
		power++;
	    }
	    cnt[pf] += power;
	    pf = primes.get(++idx);
	}
	if (N != 1)
	    cnt[N]++;
    }

    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	sieve();
	cnt = new long[MAX];
	for (int i = 2; i <= n; i++)
	    f(i);
	long ans = 1;
	for (int i = 2; i <= n; i++)
	    if (cnt[i] != 0)
		ans = (ans * (cnt[i] + 1)) % MOD;
	System.out.println(ans);
    }

}
