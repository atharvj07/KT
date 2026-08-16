import java.io.*;
import java.util.*;
public class c{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		long s = sc.nextLong();
		long[][] factors = getFactors(s);
		long tot = 0;
		for(int i = 0; i < factors.length; i++){
			tot += factors[i][1];
		}
		
		boolean res = isWinner(tot);
		if(res){
			System.out.println("1");
			if(tot<=1){
				System.out.println("0");
			}
			else{
				System.out.println(getMove(factors,memoRes.get(tot)));
			}
		}
		else{
			System.out.println("2");		
		}
	}
	
	public static long getMove(long[][] fact, long num){
		int ptr = 0;
		long res = 1;
		while(num>0){
			while(fact[ptr][1]>0 && num > 0){
				res *= fact[ptr][0];
				num--;
				fact[ptr][1]--;
			}
			ptr++;
		}
		return res;
	}
	
	public static HashMap<Long,Boolean> memo = new HashMap<Long,Boolean>();
	public static HashMap<Long,Long> memoRes = new HashMap<Long,Long>();
	public static boolean isWinner(long s){
		if(memo.containsKey(s)){
			return memo.get(s).booleanValue();
		}
		
		if(s==1) return true;
		if(s==0) return true;
		
		boolean hasLosingState = false;
		for(long ns = 1; ns < s; ns++){
			if(!isWinner(ns)){
				hasLosingState = true;
				memoRes.put(s,ns);
			}
		}
		//System.out.println(s + ": " + hasLosingState);
		memo.put(s,hasLosingState);
		return hasLosingState;
	}
	
	public static long[][] getFactors(long n){
		HashMap<Long,Long> map = new HashMap<Long,Long>();
		
		long d = 2;
		while(n%d==0){ incMap(map,d); n/=d;}
		long end = (long)Math.sqrt(n);
		for(d = 3l; d <= end; d += 2){
			while(n%d==0){ incMap(map,d); n/=d;}		
		}
		if(n!=1)
			incMap(map,n);		
		long[][] ret = new long[map.size()][2];
		int ptr = 0;
		for(Long k:map.keySet()){
			ret[ptr][0] = k.longValue();
			ret[ptr++][1] = map.get(k).longValue();
			//System.out.println(Arrays.toString(ret[ptr-1]));
		}
		return ret;
	}
	public static void incMap(HashMap<Long,Long> map,long d){
		if(map.containsKey(new Long(d))){
			Long r = map.get(new Long(d));
			map.remove(new Long(d));
			map.put(new Long(d),new Long(r.longValue()+1));
		}
		else{
			map.put(new Long(d),new Long(1));
		}
	}
}

//n** {{6}}
//n** {{16}}
//n** {{30}}
//n** {{1}}
//n** {{2}}
//n** {{3}}
//n** {{4}}
//n** {{5}}
