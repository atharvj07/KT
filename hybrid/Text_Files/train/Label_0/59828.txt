import java.util.*;
import static java.lang.Math.*;
import static java.lang.System.out;

public class Main {
	Scanner sc = new Scanner(System.in);
	public static void main(String[] args) {
		new Main().AOJ0161();
	}
	
	void AOJ0161(){	// Sport Meet
		while(sc.hasNext()){
			int n=sc.nextInt();
			if(n==0)	break;
			Time161[] times = new Time161[n];
			for(int i=0; i<n; i++)	times[i] = new Time161(sc.nextInt(), (sc.nextInt()*60+sc.nextInt() + sc.nextInt()*60+sc.nextInt() + sc.nextInt()*60+sc.nextInt() + sc.nextInt()*60+sc.nextInt()));
			Arrays.sort(times);
			out.println(times[0].num);	out.println(times[1].num);	out.println(times[times.length-2].num);
		}
	}
	class Time161 implements Comparable<Time161>{
		int num, time;
		Time161(int num, int time){
			this.num=num;	this.time=time;
		}
		@Override
		public int compareTo(Time161 o) {
			if(this.time<o.time)	return -1;
			if(this.time>o.time)	return 1;
			return 0;
		}
	}
	
	void AOJ0138(){	// Track and Field Competition
		Time138[] times1st = new Time138[8];
		Time138[] times2nd = new Time138[8];
		Time138[] times3rd = new Time138[8];
		for(int i=0; i<8; i++)	times1st[i] = new Time138(sc.nextInt(), sc.nextDouble());
		for(int i=0; i<8; i++)	times2nd[i] = new Time138(sc.nextInt(), sc.nextDouble());
		for(int i=0; i<8; i++)	times3rd[i] = new Time138(sc.nextInt(), sc.nextDouble());
		Arrays.sort(times1st);	Arrays.sort(times2nd);	Arrays.sort(times3rd);
		for(int i=0; i<2; i++)	out.println(times1st[i].num+" "+times1st[i].time);
		for(int i=0; i<2; i++)	out.println(times2nd[i].num+" "+times2nd[i].time);
		for(int i=0; i<2; i++)	out.println(times3rd[i].num+" "+times3rd[i].time);
		Time138[] times = new Time138[6];
		times[0]=times1st[2]; times[1]=times1st[3];	times[2]=times2nd[2]; times[3]=times2nd[3];	times[4]=times3rd[2]; times[5]=times3rd[3];
		Arrays.sort(times);
		for(int i=0; i<2; i++)	out.println(times[i].num+" "+times[i].time);
	}
	class Time138 implements Comparable<Time138>{
		int num;	double time;
		Time138(int num, double time){
			this.num=num;	this.time=time;
		}
		@Override
		public int compareTo(Time138 o) {
			if(this.time<o.time)	return -1;
			if(this.time>o.time)	return 1;
			return 0;
		}
	}
	
	void AOJ0005(){	// GCD and LCM
		while(sc.hasNext()){
			int a=sc.nextInt(), b=sc.nextInt();
			int temp=gcd(max(a,b), min(a,b));
			out.println(temp+" "+max(a,b)/temp*min(a,b));
		}
	}
	int gcd(int x, int y){
		if(y==0)	return x;
		else	return gcd(y, x%y);
	}
	
	int c197=0;
	void AOJ0197(){	// Greatest Common Divisor: Euclidean Algorithm
		while(sc.hasNext()){
			int x=sc.nextInt(), y=sc.nextInt();
			if(x<2)	break;
			c197=0;
			out.println(gcd197(max(x,y), min(x,y))+" "+c197);
		}
	}
	int gcd197(int x, int y){
		if(y==0)	return x;
		c197++;
		return gcd197(y, x%y);
	}
	
	void AOJ0001(){	// List of Top 3 Hills
		int[] m = new int[10];
		for(int i=0; i<10; i++)	m[i]=sc.nextInt();
		Arrays.sort(m);
		for(int i=9; i>=7; i--)	out.println(m[i]);
	}
	
	void AOJ10029(){	// Sort II
		int n=sc.nextInt();
		int[] ans = new int[n];
		for(int i=0; i<n; i++)	ans[i]=sc.nextInt();
		Arrays.sort(ans);
		out.print(ans[0]);
		for(int i=1; i<n; i++)	out.print(" "+ans[i]);
		out.println();
	}
	
	int[][] p26 = new int[10][10];
	int c26=100;
	void AOJ0026(){	// Dropping Ink
		int ans=0;
		while(sc.hasNext()){
			Scanner sc2 = new Scanner(sc.nextLine()).useDelimiter(",");
			int x=sc2.nextInt(), y=sc2.nextInt(), s=sc2.nextInt();
			// out.println("x"+x+" y"+y+" s"+s);
			ans=max(solve26(x,y),ans);
			ans=max(solve26(x-1,y),ans);	ans=max(solve26(x+1,y),ans);
			ans=max(solve26(x,y-1),ans);	ans=max(solve26(x,y+1),ans);
			if(s>=2){
				ans=max(solve26(x-1,y-1),ans);	ans=max(solve26(x-1,y+1),ans);
				ans=max(solve26(x+1,y-1),ans);	ans=max(solve26(x+1,y+1),ans);
			}
			if(s>=3){
				ans=max(solve26(x-2,y),ans);	ans=max(solve26(x+2,y),ans);
				ans=max(solve26(x,y-2),ans);	ans=max(solve26(x,y+2),ans);
			}
		}
		out.println(c26);
		out.println(ans);
	}
	int solve26(int x, int y){
		int r=-1;
		if(0<=x && x<=9 && 0<=y && y<=9){
			c26 -= p26[x][y]==0? 1: 0;
			p26[x][y]++;
			r=p26[x][y];
		}
		return r;	// RA
	}
	
	void AOJ0008(){	//Sum of 4 Integers
		while(sc.hasNext()){
			int ans=0, n=sc.nextInt();
			for(int a=0; a<10; a++){
				for(int b=0; b<10; b++){
					for(int c=0; c<10; c++){
						for(int d=0; d<10; d++)		if((a+b+c+d)==n)	ans++;
					}
				}
			}
			out.println(ans);
		}
	}
	
	void AOJ0055(){	// Sequence
		while(sc.hasNext()){
			double last=sc.nextDouble(), ans=last;
			for(int i=2; i<=10; i++){
				ans+= i%2==0? last*2: last/3;
				last = i%2==0? last*2: last/3;
				// out.println(last);
			}
			out.println(ans);
		}
	}
}