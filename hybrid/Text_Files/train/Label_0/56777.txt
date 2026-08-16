import java.util.Scanner;
import java.math.BigInteger;

class Main{
    static long lmod = 4294967311L;
    static final BigInteger mod = BigInteger.valueOf(4294967311L);
    static BigInteger mypow(BigInteger n,long p){
	if (p == 1)return n;
	BigInteger ret = mypow(n,p/2);
	ret = ret.multiply(ret).mod(mod);
	if (p%2 == 1)ret = ret.multiply(n).mod(mod);
	return ret;
    }
    static BigInteger getinv(BigInteger a){
	return mypow(a,lmod-2);
    }
    static long solve(int n,int op[],int val[]){
	long ret = 0;
	for(int i=0;i<n;i++){
	    if (op[i] == 1){//+
		ret = (ret + val[i])%lmod;
	    }else if (op[i] == 2){//-
		ret = (ret - val[i])%lmod;
		ret = (ret + lmod)%lmod;
	    }else if (op[i] == 3){//*
		BigInteger tval = BigInteger.valueOf(val[i]);
		ret = tval.multiply(BigInteger.valueOf(ret)).mod(mod).longValue();
	    }else if (op[i] == 4){///
		BigInteger tval = BigInteger.valueOf(val[i]);
		BigInteger inv = getinv(tval);
		ret = inv.multiply(BigInteger.valueOf(ret)).mod(mod).longValue();
	    }
	}
	return ret;
    }
    public static void main(String[] args){
	long maxi = BigInteger.valueOf(2147483648L).longValue();
	int n;
	Scanner in = new Scanner(System.in);
	while(true){
	    if (in.hasNextInt());
	    else break;
	    n = in.nextInt();
	    if (n == 0)break;
	    int op[] = new int[n],val[] = new int[n];
	    for(int i=0;i<n;i++){
		op[i] = in.nextInt();
		val[i] = in.nextInt();
	    }
	    long ret = solve(n,op,val);
	    if (ret < maxi){
	    }else {
		ret = ret-lmod;
	    }
	    System.out.println(ret);
	}
    }
}