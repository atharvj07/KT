import java.util.Scanner;

//Revenge of Champernowne Constant
public class Main{

	long DIGIT_LIMIT = 1000000000000000000L;
	long MAX_NUMBER = 59477124183006535L;
	long[] endK;
	long[] ten;
	
	void init(){
		endK = new long[20];
		endK[0] = 0;
		long num = 9;
		for(int k=1;k<=17;k++,num*=10){
			endK[k] = endK[k-1]+k*num;
		}
		endK[18] = DIGIT_LIMIT;
		endK[0] = -1;
		ten = new long[20];
		ten[0] = 0;
		ten[1] = 10;
		for(int k=2;k<=17;k++)ten[k]=ten[k-1]*10;
	}
	
	long findNumber(long x){
		if(x<=0||MAX_NUMBER<x)return DIGIT_LIMIT;
		if(x<10)return x;
		int k = (x+"").length()-1;
		return endK[k]+1+(k+1)*(x-ten[k]);
	}
	
	long findString(String target){
		boolean allzero = true;
		for(char ch:target.toCharArray())allzero&=ch=='0';
		if(allzero)return findNumber(Long.parseLong("1"+target))+1;
		int len = target.length();
		if(len==1){
			return findNumber(Long.parseLong(target));
		}
		long res = DIGIT_LIMIT;
		int lenMax = Math.min(17, len);
		for(int h=0;h<lenMax;h++)for(int k=1;k<=lenMax;k++)res = Math.min(res, findStringSub(target, h, k));
		return res;
	}
	
	long findStringSub(String target, int h, int k){
		if(target.charAt(h)=='0')return DIGIT_LIMIT;
		String sub = target.substring(0, h);
		String s = "";
		for(int i=h;i<h+k;i++){
			if(i<target.length())s+=target.charAt(i);
			else {
				int L = h+k-i;
				String r = (Long.parseLong(sub.substring(sub.length()-L))+1)+"";
				while(r.length()-L<0)r="0"+r;
				s+=r.substring(r.length()-L); break;
			}
		}
		long base = Long.parseLong(s);
		if(MAX_NUMBER<base)return DIGIT_LIMIT;
		String match = base+"";
		int pos = h, addLen = 0;
		long b = base-1;
		while(pos>0){
			if(b<=0)return DIGIT_LIMIT;
			String add = b-- +"";
			pos-=add.length();
			addLen+=add.length();
			match = add+match;
		}
		b = base+1;
		pos = h+k;
		while(pos < target.length()){
			String add = b++ +"";
			pos+=add.length();
			match+=add;
		}
		for(int i=0;i<target.length();i++)if(target.charAt(i)!=match.charAt(addLen-h+i))return DIGIT_LIMIT;
		return findNumber(base)-h;
	}
	
	void run(){
		init();
		Scanner sc = new Scanner(System.in);
		for(;;){
			String s = sc.next();
			if("#".equals(s))break;
			System.out.println(findString(s));
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}