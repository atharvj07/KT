import java.io.*;
import java.util.*;
public class DominoPrinciple {
	static class Domino implements Comparable<Domino>{
		int ind;
		int x; int h;
		int dp;
		public Domino(int x, int h, int i){
			this.x=x;
			this.h=h;
			ind=i;
			dp=1;
		}

		public int compareTo(Domino o){
			if (x==o.x) return o.h-h;
			return o.x-x;
		}
	}
    public static void main(String[] args)throws IOException{
    	BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
    	int N=Integer.parseInt(in.readLine());
    	Domino[] dom=new Domino[N];
    	for (int i=0; i<N; i++){
    		String[] str=(in.readLine()).split(" ");
    		int x=Integer.parseInt(str[0]);
    		int h=Integer.parseInt(str[1]);
    		dom[i]=new Domino(x, h, i);
    	}
    	Arrays.sort(dom);
    	int num=0;
		//dom[0] has highest x
		for (int i=0; i<N; i++) dom[i].dp=1;
		for (int i=1; i<N; i++){

			for (int j=i-1; j>=0; j-=dom[j].dp){
				if (dom[j].x>dom[i].x+dom[i].h-1) break;
				dom[i].dp+=dom[j].dp;
			}
		}
		int[] sum=new int[N];
		for (int i=0; i<N; i++)
			sum[dom[i].ind]=dom[i].dp;
		System.out.print(sum[0]);
		for (int i=1; i<N; i++)
			System.out.print(" "+sum[i]);
		System.out.println();
    }
}