
import java.util.*;
public class May {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		long n = sc.nextLong();
		long q = sc.nextLong();
		while(q-->0) {
			long u = sc.nextLong();
			long h = level(u);
		//	System.out.println(h);
			char[] s = sc.next().toCharArray();
			for(char c : s) {
				if(c == 'L') {
					if(h>0) {
					--h;
					u-=pow(2, h);
					}
				}else if(c == 'R') {
					if(h>0) {
					--h;
					u+=pow(2, h);
					}
				}else if(h<level((n+1)/2)){
					long temp = pow(2, h);
					if(u+temp>0 && u+temp<=n) {
						if(h+1 == level(u+temp)) {
							++h;
							u+=temp;
						}else {
							++h;
							u-=temp;
						}
							
					}else if(u-temp>0 && u-temp<=n) {
						if(h+1 == level(u-temp)) {
							++h;
							u-=temp;
						}else {
							++h;
							u+=temp;
						}
					}
				}
				//System.out.println(u);
			}
		System.out.println(u);
		}
		
	}
	private static long level(long u) {
		long ans = 0;
		long temp = 1,i=0;
		while(u>=temp) {
			if(u%temp == 0) {
				ans = i;
			}
			temp*=2; ++i;
		}
		return ans;
	}
	private static long pow(long x, long h) {
	    long res = 1;        
        while (h > 0) { 
            
            if((h & 1)==1) 
                res = (res * x); 
      
            h = h >> 1;  
            x = (x * x);  
        } 
        return res;
}
	
}