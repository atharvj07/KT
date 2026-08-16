import java.util.*;

public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true){
			String s = sc.next();
			if(s.compareTo("#")==0) break;
			
			long p, q, r;
			String[] t = s.split("\\.");
			if(t.length==3){
				long y = Integer.valueOf(t[0]);
				long m = Integer.valueOf(t[1]);
				long d = Integer.valueOf(t[2]);
				
				d += (y*365 + y/4 + y/400 - y/100);
				if(y%400==0 || (y%4==0 && y%100!=0)) d-=366;
				else d-=365;
				
				for(int i=1;i<m;i++){
					if(i==4 || i==6 || i==9 || i==11) d+=30;
					else if(i==2){
						if(y%400==0 || (y%4==0 && y%100!=0)) d+=29;
						else d+=28;
					}
					else d+=31;
				}
				
				d-=734858;
				d %= 1872000;
				p = d/144000;
				System.out.print(p + ".");
				d %= 144000;
				p = d/7200;
				System.out.print(p + ".");
				d %= 7200;
				p = d/360;
				System.out.print(p + ".");
				d %= 360;
				p = d/20;
				d %= 20;
				System.out.println(p + "." + d);
				
			}else{
				p = Integer.valueOf(t[4]) + 734858;
				p += Integer.valueOf(t[3]) * 20;
				p += Integer.valueOf(t[2]) * 360;
				p += Integer.valueOf(t[1]) * 7200;
				p += Integer.valueOf(t[0]) * 144000;
				
				q = p/146097;
				q *= 400;
				p %= 146097;
				
				for(int i=1;;i++){
					if(i%400==0 || (i%4==0 && i%100!=0)) r=366;
					else r=365;
					
					if(p<=r){
						q += i;
						break;
					}
					else p -= r;
				}
				
				for(int i=1;;i++){
					if(i==4 || i==6 || i==9 || i==11) r=30;
					else if(i==2){
						if(q%400==0 || (q%4==0 && q%100!=0)) r=29;
						else r=28;
					}
					else r=31;
					
					if(p<=r){
						System.out.println(q + "." + i + "." + p);
						break;
					}
					else p -= r;
				}
				
			}
		}	
	}	
}